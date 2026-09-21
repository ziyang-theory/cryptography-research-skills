"""Packaging integrity checks; these do not evaluate agent behavior or proofs."""

import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest import mock
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('build_plugin', ROOT / 'scripts' / 'build_plugin.py')
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)


class BuildPluginTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='crypto-plugin-test-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / 'repo'
        self.root.mkdir()
        for collection in BUILDER.COLLECTIONS:
            shutil.copytree(ROOT / collection, self.root / collection)
        for name in ('collections.json', 'LICENSE', 'CITATION.cff'):
            shutil.copyfile(ROOT / name, self.root / name)
        self.catalog = json.loads((self.root / 'collections.json').read_text(encoding='utf-8'))
        self.skill = self.root / 'paper-writing' / self.catalog['paper-writing'][0]
        submission = self.root / 'submission'
        (submission / 'assets').mkdir(parents=True)
        (submission / 'assets' / 'logo.png').write_bytes(b'fixture asset')
        (submission / 'PLUGIN_README.md').write_text('# Fixture plugin\n', encoding='utf-8')
        self.manifest_path = submission / 'plugin.json'
        self.manifest = {
            '$schema': BUILDER.MANIFEST_SCHEMA,
            'name': BUILDER.NAME,
            'version': '0.1.0',
            'description': 'Test fixture for release packaging.',
            'author': {'name': 'Test Author'},
            'license': 'MIT',
            'extensions': {'com.openai': {'interface': {
                'displayName': 'Cryptography Research Skills',
                'shortDescription': 'Cryptography research support',
                'longDescription': 'A fixture describing this research assistance plugin.',
                'developerName': 'Test Author',
                'defaultPrompt': ['Review the supplied cryptographic proof.'],
                'composerIcon': './assets/logo.png',
                'logo': './assets/logo.png',
            }}},
        }
        self.write_manifest()

    def write_manifest(self):
        self.manifest_path.write_text(json.dumps(self.manifest), encoding='utf-8')

    def test_archive_contains_exact_catalog_and_explicit_release_inputs(self):
        (self.root / 'private-notes.md').write_text('must not be published', encoding='utf-8')
        (self.root / '.env').write_text('NOT_A_REAL_SECRET=test', encoding='utf-8')
        (self.skill / '__pycache__').mkdir(exist_ok=True)
        (self.skill / '__pycache__' / 'test.pyc').write_bytes(b'ignored')
        (self.skill / '.DS_Store').write_bytes(b'ignored')
        result = BUILDER.build(self.root)
        expected_skills = {name for names in self.catalog.values() for name in names}
        self.assertEqual(result['skills'], len(expected_skills))
        with zipfile.ZipFile(result['archive']) as archive:
            members = archive.namelist()
            self.assertEqual(members, sorted(members))
            self.assertTrue(all(name.startswith(BUILDER.NAME + '/') for name in members))
            names = {name.removeprefix(BUILDER.NAME + '/') for name in members}
            actual_skills = {name.split('/')[1] for name in names if name.startswith('skills/')}
            self.assertEqual(actual_skills, expected_skills)
            expected_files = {'plugin.json', '.codex-plugin/plugin.json', 'README.md',
                              'LICENSE', 'CITATION.cff', 'assets/logo.png'}
            for collection, skills in self.catalog.items():
                for name in skills:
                    source = self.root / collection / name
                    for path, data in BUILDER.tree_files(source, self.root):
                        package_path = f'skills/{name}/{path.relative_to(source).as_posix()}'
                        expected_files.add(package_path)
                        self.assertEqual(archive.read(BUILDER.NAME + '/' + package_path), data)
            self.assertEqual(names, expected_files)
            legacy = json.loads(archive.read(BUILDER.NAME + '/.codex-plugin/plugin.json'))
            self.assertEqual(legacy['skills'], './skills/')
            self.assertEqual(legacy['author'], self.manifest['author'])
            self.assertEqual(legacy['interface'], self.manifest['extensions']['com.openai']['interface'])

    def test_build_is_deterministic_across_output_paths_and_file_timestamps(self):
        first = BUILDER.build(self.root, self.root / 'first')
        for source in self.skill.rglob('*'):
            if source.is_file():
                source.touch()
        second = BUILDER.build(self.root, self.root / 'second')
        self.assertEqual(Path(first['archive']).read_bytes(), Path(second['archive']).read_bytes())
        self.assertEqual(first['sha256'], second['sha256'])
        third = BUILDER.build(self.root, self.root / 'first')
        self.assertEqual(first['sha256'], third['sha256'])
        with zipfile.ZipFile(third['archive']) as archive:
            self.assertTrue(all(info.date_time == BUILDER.FIXED_TIME for info in archive.infolist()))
            self.assertTrue(all((info.external_attr >> 16) & 0o777 == 0o644
                                for info in archive.infolist()))

    def test_symlink_resource_is_rejected_even_when_its_name_is_excluded(self):
        (self.skill / '.DS_Store').symlink_to(self.root / 'LICENSE')
        with self.assertRaisesRegex(ValueError, 'Symlink'):
            BUILDER.build(self.root)
        self.assertFalse((self.root / 'dist').exists())

    def test_symlink_parent_directory_is_rejected(self):
        collection = self.root / 'paper-writing'
        moved = self.root / 'moved'
        collection.rename(moved)
        collection.symlink_to(moved, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'indirect collection'):
            BUILDER.build(self.root)

    def test_catalog_rejects_unsafe_unknown_and_duplicate_entries(self):
        for name in ('../outside', 'no-such-skill', self.catalog['paper-writing'][0]):
            with self.subTest(name=name):
                catalog = json.loads(json.dumps(self.catalog))
                catalog['paper-writing'].append(name)
                (self.root / 'collections.json').write_text(json.dumps(catalog), encoding='utf-8')
                with self.assertRaises(ValueError):
                    BUILDER.build(self.root)
        self.assertFalse((self.root / 'dist').exists())

    def test_qualified_skill_names_fit_portal_limit_after_plugin_id_change(self):
        self.assertEqual(BUILDER.NAME, 'crypto-research-skills')
        skills = BUILDER.load_catalog(self.root)
        self.assertTrue(all(len(f'{BUILDER.NAME}:{name}') <= 64 for name in skills))
        with mock.patch.object(BUILDER, 'NAME', 'cryptography-research-skills'):
            with self.assertRaisesRegex(ValueError, 'Combined plugin-name:skill-name exceeds 64'):
                BUILDER.load_catalog(self.root)
        self.assertFalse((self.root / 'dist').exists())

    def test_qualified_skill_name_accepts_64_characters_and_rejects_65(self):
        for length in (64, 65):
            name = 'x' * (length - len(BUILDER.NAME) - 1)
            catalog = json.loads(json.dumps(self.catalog))
            catalog['paper-writing'].append(name)
            source = self.root / 'paper-writing' / name
            source.mkdir()
            (source / 'SKILL.md').write_text(
                f'---\nname: {name}\ndescription: A boundary fixture.\n---\n', encoding='utf-8',
            )
            (self.root / 'collections.json').write_text(json.dumps(catalog), encoding='utf-8')
            if length == 64:
                self.assertIn(name, BUILDER.load_catalog(self.root))
            else:
                with self.assertRaisesRegex(ValueError, r'exceeds 64 characters \(65\)'):
                    BUILDER.load_catalog(self.root)

    def test_missing_markdown_reference_is_rejected_before_outputs(self):
        path = self.skill / 'SKILL.md'
        path.write_text(path.read_text(encoding='utf-8') + '\n[Missing](references/absent.md)\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Missing local reference'):
            BUILDER.build(self.root)
        self.assertFalse((self.root / 'dist').exists())

    def test_yaml_icon_reference_is_checked_from_skill_root(self):
        agents = self.skill / 'agents'
        agents.mkdir(exist_ok=True)
        (agents / 'openai.yaml').write_text('interface:\n  icon_small: "./assets/missing.png"\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Missing local reference'):
            BUILDER.build(self.root)
        (self.skill / 'assets').mkdir()
        (self.skill / 'assets' / 'missing.png').write_bytes(b'fixture')
        self.assertGreater(BUILDER.build(self.root, check=True)['files'], 0)
        self.assertFalse((self.root / 'dist').exists())

    def test_manifest_limits_paths_and_semver_are_validated(self):
        for version in ('1', '01.0.0', '1.0.0-01'):
            with self.subTest(version=version):
                self.manifest['version'] = version
                self.write_manifest()
                with self.assertRaisesRegex(ValueError, 'semantic version'):
                    BUILDER.build(self.root, check=True)
        self.manifest['version'] = '1.0.0-rc.1+build.3'
        interface = self.manifest['extensions']['com.openai']['interface']
        interface['displayName'] = 'x' * 31
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, '30 characters'):
            BUILDER.build(self.root, check=True)
        interface['displayName'] = 'Test Plugin'
        interface['logo'] = './missing.png'
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, 'Missing local reference'):
            BUILDER.build(self.root, check=True)

    def test_modified_existing_stage_is_preserved(self):
        BUILDER.build(self.root)
        sentinel = self.root / 'dist' / BUILDER.NAME / 'user-notes.md'
        sentinel.write_text('preserve this file', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'modified or additional'):
            BUILDER.build(self.root)
        self.assertEqual(sentinel.read_text(encoding='utf-8'), 'preserve this file')

    def test_manifest_rejects_scope_expansion_and_inconsistent_listing(self):
        baseline = json.dumps(self.manifest)
        for location, key, value, error in (
            ('root', '$schema', 'https://example.org/other-schema.json', '\\$schema'),
            ('root', 'hooks', {}, 'skills-only'),
            ('overlay', 'apps', [], 'skills-only'),
            ('overlay', 'mcpServers', {}, 'skills-only'),
            ('interface', 'screenshots', [], 'skills-only'),
            ('interface', 'developerName', 'Different Author', 'agree'),
            ('interface', 'defaultPrompt', ['same', ' same '], 'duplicate'),
            ('interface', 'defaultPrompt', ['a', 'b', 'c', 'd'], 'at most 3'),
        ):
            with self.subTest(location=location, key=key):
                self.manifest = json.loads(baseline)
                target = self.manifest
                if location in ('overlay', 'interface'):
                    target = target['extensions']['com.openai']
                if location == 'interface':
                    target = target['interface']
                target[key] = value
                self.write_manifest()
                with self.assertRaisesRegex(ValueError, error):
                    BUILDER.build(self.root, check=True)


if __name__ == '__main__':
    unittest.main()
