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
        self.skill = self.root / 'research' / self.catalog['research'][0]
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
        expected_catalog = {
            'research': {
                'crypto-research-framing', 'crypto-literature-evidence',
                'crypto-proof-auditor', 'crypto-correlation-accounting',
            },
            'writing': {
                'cryptography-writing', 'crypto-prior-work-comparison',
                'crypto-implementation-evaluation-writing', 'crypto-manuscript-qa',
                'crypto-ai-acknowledgements',
            },
            'implementation': {
                'crypto-protocol-implementation', 'crypto-benchmarking',
                'crypto-research-artifacts',
            },
        }
        self.assertEqual({group: set(names) for group, names in self.catalog.items()}, expected_catalog)
        (self.root / 'private-notes.md').write_text('must not be published', encoding='utf-8')
        (self.root / '.env').write_text('NOT_A_REAL_SECRET=test', encoding='utf-8')
        (self.skill / '__pycache__').mkdir(exist_ok=True)
        (self.skill / '__pycache__' / 'test.pyc').write_bytes(b'ignored')
        (self.skill / '.DS_Store').write_bytes(b'ignored')
        result = BUILDER.build(self.root)
        expected_skills = {name for names in self.catalog.values() for name in names}
        self.assertEqual(result['skills'], len(expected_skills))
        inventory = json.loads((self.root / 'dist' / f'{BUILDER.NAME}-build.json').read_text(encoding='utf-8'))
        self.assertEqual(inventory['skills'], {
            name: f'{group}/{name}' for group, names in expected_catalog.items() for name in names
        })
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
        collection = self.root / 'research'
        moved = self.root / 'moved'
        collection.rename(moved)
        collection.symlink_to(moved, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'indirect collection'):
            BUILDER.build(self.root)

    def test_catalog_rejects_unsafe_unknown_and_duplicate_entries(self):
        for name in ('../outside', 'no-such-skill', self.catalog['research'][0]):
            with self.subTest(name=name):
                catalog = json.loads(json.dumps(self.catalog))
                catalog['research'].append(name)
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
            catalog['research'].append(name)
            source = self.root / 'research' / name
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

    def test_windows_drive_references_are_rejected_before_outputs(self):
        source = self.skill / 'SKILL.md'
        original = source.read_text(encoding='utf-8')
        for target in ('C:/Users/example/private.md', r'C:\Users\example\private.md',
                       'c:relative.md', '%43%3A/Users/example/private.md'):
            with self.subTest(target=target):
                source.write_text(original + f'\n[Private]({target})\n', encoding='utf-8')
                with self.assertRaisesRegex(ValueError, 'Non-portable reference'):
                    BUILDER.build(self.root)
                self.assertFalse((self.root / 'dist').exists())
        source.write_text(original + '\n[Source](https://example.org/paper.pdf#page=2)\n',
                          encoding='utf-8')
        self.assertEqual(BUILDER.build(self.root, check=True)['skills'], 12)

    def test_frontmatter_requires_mapping_and_nonempty_string_fields(self):
        name = self.skill.name
        cases = [
            ('[]', 'must be a YAML mapping'),
            ('null', 'must be a YAML mapping'),
            ('42', 'must be a YAML mapping'),
            ('name: []\ndescription: text', 'name must be a nonempty string'),
            ('name: null\ndescription: text', 'name must be a nonempty string'),
            ('name: 42\ndescription: text', 'name must be a nonempty string'),
            ('name: true\ndescription: text', 'name must be a nonempty string'),
            ('name: ""\ndescription: text', 'name must be a nonempty string'),
            ('name: different-skill\ndescription: text', 'name differs from catalog'),
            (f'name: {name}', 'description must be a nonempty string'),
        ]
        for description in ('[]', '{}', 'null', '42', 'true', '""', '"   "', '|\n  '):
            cases.append((f'name: {name}\ndescription: {description}',
                          'description must be a nonempty string'))
        for frontmatter, error in cases:
            with self.subTest(frontmatter=frontmatter):
                (self.skill / 'SKILL.md').write_text(
                    f'---\n{frontmatter}\n---\n# Fixture\n', encoding='utf-8',
                )
                with self.assertRaisesRegex(ValueError, error):
                    BUILDER.build(self.root)
                self.assertFalse((self.root / 'dist').exists())

    def test_frontmatter_accepts_quoted_and_multiline_yaml_without_rewriting(self):
        for description in ('"A description: with punctuation."',
                            '>\n  A folded description\n  spanning two lines.',
                            '|\n  A literal description.\n  A second line.'):
            with self.subTest(description=description):
                source = (f'---\nname: "{self.skill.name}" # inline comment\n'
                          f'description: {description}\n'
                          'custom_metadata: {enabled: true}\n---\n# Fixture\n')
                (self.skill / 'SKILL.md').write_text(source, encoding='utf-8')
                _, _, files = BUILDER.collect_package(self.root)
                self.assertEqual(files[f'skills/{self.skill.name}/SKILL.md'], source.encode())

    def test_metadata_rejects_malformed_yaml_and_python_object_tags(self):
        original = (self.skill / 'SKILL.md').read_bytes()
        ui = self.skill / 'agents' / 'openai.yaml'
        ui.parent.mkdir(exist_ok=True)
        for content in ('description: [unterminated',
                        'description: !!python/object/apply:builtins.str [unsafe]'):
            with self.subTest(frontmatter=content):
                (self.skill / 'SKILL.md').write_text(
                    f'---\nname: {self.skill.name}\n{content}\n---\n', encoding='utf-8',
                )
                with self.assertRaisesRegex(ValueError, 'Invalid YAML.*SKILL.md frontmatter'):
                    BUILDER.build(self.root)
                self.assertFalse((self.root / 'dist').exists())
        (self.skill / 'SKILL.md').write_bytes(original)
        for content in ('interface: [unterminated',
                        'interface: !!python/object/apply:builtins.dict []'):
            with self.subTest(ui=content):
                ui.write_text(content, encoding='utf-8')
                with self.assertRaisesRegex(ValueError, 'Invalid YAML.*agents/openai.yaml'):
                    BUILDER.build(self.root)
                self.assertFalse((self.root / 'dist').exists())

    def test_optional_ui_metadata_checks_mapping_and_known_field_types(self):
        ui = self.skill / 'agents' / 'openai.yaml'
        ui.parent.mkdir(exist_ok=True)
        for content in ('', 'null', '[]', '42', 'interface: null',
                        'interface: []', 'interface: text'):
            with self.subTest(content=content):
                ui.write_text(content, encoding='utf-8')
                with self.assertRaisesRegex(ValueError, 'must be a (?:YAML )?mapping'):
                    BUILDER.build(self.root)
                self.assertFalse((self.root / 'dist').exists())
        for field in ('display_name', 'short_description', 'default_prompt',
                      'brand_color', 'icon_small', 'icon_large'):
            for value in ('[]', 'null', '42', 'true', '""'):
                with self.subTest(field=field, value=value):
                    ui.write_text(f'interface:\n  {field}: {value}\n', encoding='utf-8')
                    with self.assertRaisesRegex(ValueError, f'{field} must be a nonempty string'):
                        BUILDER.build(self.root)
                    self.assertFalse((self.root / 'dist').exists())

    def test_ui_metadata_is_optional_and_unknown_fields_are_preserved(self):
        ui = self.skill / 'agents' / 'openai.yaml'
        ui.unlink(missing_ok=True)
        self.assertEqual(BUILDER.build(self.root, check=True)['skills'], 12)
        ui.parent.mkdir(exist_ok=True)
        for source in ('{}\n', 'custom_metadata: {enabled: true}\n',
                       'interface:\n  display_name: "Fixture"\n'
                       '  default_prompt: >\n    Read this\n    supplied fixture.\n'
                       '  future_field: [one, two]\n'):
            with self.subTest(source=source):
                ui.write_text(source, encoding='utf-8')
                _, _, files = BUILDER.collect_package(self.root)
                self.assertEqual(files[f'skills/{self.skill.name}/agents/openai.yaml'], source.encode())
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

    def test_yaml_icons_support_flow_mappings_and_reject_non_file_paths(self):
        ui = self.skill / 'agents' / 'openai.yaml'
        ui.parent.mkdir(exist_ok=True)
        assets = self.skill / 'assets'
        assets.mkdir()
        (assets / 'icon.png').write_bytes(b'fixture')
        ui.write_text('interface: {icon_small: "./assets/icon.png"} # a YAML comment\n',
                      encoding='utf-8')
        self.assertGreater(BUILDER.build(self.root, check=True)['files'], 0)
        for target in ('./assets/', '../other-skill/icon.png', '/tmp/icon.png',
                       'https://example.org/icon.png', '#icon', './assets/icon.png?raw=1',
                       '<https://example.org/icon.png>', '<//example.org/icon.png>',
                       '<./assets/icon.png>', '  <https://example.org/icon.png>  '):
            with self.subTest(target=target):
                ui.write_text(f'interface: {{icon_large: {json.dumps(target)}}}\n', encoding='utf-8')
                with self.assertRaises(ValueError):
                    BUILDER.build(self.root)
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

    def test_listing_images_require_packaged_file_paths(self):
        interface = self.manifest['extensions']['com.openai']['interface']
        for field in ('composerIcon', 'logo'):
            for target in ('./assets/', '#missing-logo', './assets/logo.png#part',
                           './assets/logo.png?raw=1', 'https://example.org/logo.png',
                           '/tmp/logo.png', 'C:/Users/example/logo.png', './missing.png',
                           '<https://example.org/logo.png>', '<//example.org/logo.png>',
                           '<./assets/logo.png>', '  <https://example.org/logo.png>  '):
                with self.subTest(field=field, target=target):
                    interface[field] = target
                    self.write_manifest()
                    with self.assertRaises(ValueError):
                        BUILDER.build(self.root)
                    self.assertFalse((self.root / 'dist').exists())
            interface[field] = './assets/logo.png'
        self.write_manifest()
        self.assertEqual(BUILDER.build(self.root, check=True)['skills'], 12)

    def test_modified_existing_stage_is_preserved(self):
        BUILDER.build(self.root)
        sentinel = self.root / 'dist' / BUILDER.NAME / 'user-notes.md'
        sentinel.write_text('preserve this file', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'modified or additional'):
            BUILDER.build(self.root)
        self.assertEqual(sentinel.read_text(encoding='utf-8'), 'preserve this file')

    def test_non_file_output_collision_preserves_stage_and_allows_retry(self):
        output_names = (f'{BUILDER.NAME}-0.1.0.zip', f'{BUILDER.NAME}-build.json', 'SHA256SUMS')
        for index, name in enumerate(output_names):
            with self.subTest(output=name):
                output = self.root / f'collision-{index}'
                first = BUILDER.build(self.root, output)
                collision = output / name
                previous = collision.read_bytes()
                collision.unlink()
                collision.mkdir()
                before = dict(BUILDER.tree_files(output, output, exclude_caches=False))
                source = self.skill / 'SKILL.md'
                source.write_text(source.read_text() + '\nA changed source for the next build.\n')
                with self.assertRaises(ValueError):
                    BUILDER.build(self.root, output)
                self.assertTrue(collision.is_dir())
                self.assertEqual(dict(BUILDER.tree_files(output, output, exclude_caches=False)), before)
                collision.rmdir()
                collision.write_bytes(previous)
                retry = BUILDER.build(self.root, output)
                self.assertNotEqual(retry['sha256'], first['sha256'])

    def test_failed_output_replacement_restores_previous_build_and_allows_retry(self):
        names = (BUILDER.NAME, f'{BUILDER.NAME}-0.1.0.zip',
                 f'{BUILDER.NAME}-build.json', 'SHA256SUMS')
        original_replace = Path.replace
        for index, name in enumerate(names):
            with self.subTest(output=name):
                output = self.root / f'failure-{index}'
                first = BUILDER.build(self.root, output)
                before = dict(BUILDER.tree_files(output, output, exclude_caches=False))
                source = self.skill / 'SKILL.md'
                source.write_text(source.read_text() + '\nA changed source for the next build.\n')

                def fail_publication(path, target):
                    if path.parent.name.startswith('.plugin-build-') and Path(target).name == name:
                        raise PermissionError('simulated finalization failure')
                    return original_replace(path, target)

                with mock.patch.object(Path, 'replace', fail_publication):
                    with self.assertRaisesRegex(PermissionError, 'simulated finalization failure'):
                        BUILDER.build(self.root, output)
                self.assertEqual(dict(BUILDER.tree_files(output, output, exclude_caches=False)), before)
                self.assertEqual({p.name for p in output.iterdir()}, set(names))
                retry = BUILDER.build(self.root, output)
                self.assertNotEqual(retry['sha256'], first['sha256'])

    def test_failed_first_publication_leaves_no_partial_outputs(self):
        output = self.root / 'first-failure'
        original_replace = Path.replace

        def fail_archive(path, target):
            if path.parent.name.startswith('.plugin-build-') and Path(target).suffix == '.zip':
                raise PermissionError('simulated finalization failure')
            return original_replace(path, target)

        with mock.patch.object(Path, 'replace', fail_archive):
            with self.assertRaises(PermissionError):
                BUILDER.build(self.root, output)
        self.assertEqual(list(output.iterdir()), [])
        self.assertEqual(BUILDER.build(self.root, output)['skills'], 12)

    def test_failed_recovery_retains_previous_stage_backup(self):
        output = self.root / 'recovery-failure'
        BUILDER.build(self.root, output)
        stage = output / BUILDER.NAME
        before = {p.relative_to(stage): data for p, data in BUILDER.tree_files(stage, stage)}
        source = self.skill / 'SKILL.md'
        source.write_text(source.read_text() + '\nA changed source for the next build.\n')
        original_replace = Path.replace

        def fail_publication_and_recovery(path, target):
            if path.parent.name.startswith('.plugin-build-') and Path(target).suffix == '.zip':
                raise PermissionError('simulated finalization failure')
            if path.parent.name.startswith('.plugin-backup-') and Path(target) == stage:
                raise PermissionError('simulated recovery failure')
            return original_replace(path, target)

        with mock.patch.object(Path, 'replace', fail_publication_and_recovery):
            with self.assertRaisesRegex(OSError, 'recovery is incomplete.*retained'):
                BUILDER.build(self.root, output)
        backups = list(output.glob('.plugin-backup-*'))
        self.assertEqual(len(backups), 1)
        saved_stage = backups[0] / BUILDER.NAME
        self.assertEqual({p.relative_to(saved_stage): data
                          for p, data in BUILDER.tree_files(saved_stage, saved_stage)}, before)

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
