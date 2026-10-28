"""Check the source checkout's Claude plugin discovers the release catalog."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('sync_claude_plugin', ROOT / 'scripts' / 'sync_claude_plugin.py')
SYNC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SYNC)


class ClaudePluginTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='crypto-claude-plugin-test-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / 'submission').mkdir()
        self.source = {
            'name': 'crypto-research-skills', 'version': '0.2.0',
            'description': 'Cryptography workflows.',
            'author': {'name': 'Test Author', 'email': 'test@example.org'},
            'license': 'MIT', 'extensions': {'com.openai': {'interface': {}}},
        }
        self.catalog = {name: [f'{name}-example'] for name in SYNC.COLLECTIONS}
        self.write_inputs()
        for collection, names in self.catalog.items():
            for name in names:
                path = self.root / collection / name
                path.mkdir(parents=True)
                (path / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: A fixture.\n---\n')

    def write_inputs(self):
        (self.root / 'submission' / 'plugin.json').write_text(json.dumps(self.source))
        (self.root / 'collections.json').write_text(json.dumps(self.catalog))

    def test_generated_manifests_share_identity_without_openai_overlay(self):
        generated = SYNC.sync(self.root)
        plugin = generated['plugin.json']
        marketplace = generated['marketplace.json']
        self.assertEqual(plugin['version'], self.source['version'])
        self.assertEqual(plugin['author'], self.source['author'])
        self.assertNotIn('extensions', plugin)
        self.assertEqual(marketplace['plugins'][0]['name'], plugin['name'])
        self.assertEqual(marketplace['plugins'][0]['source'], './')
        self.assertEqual(marketplace['owner'], self.source['author'])
        SYNC.sync(self.root, check=True)

    def test_manifest_scans_each_catalog_skill_once(self):
        generated = SYNC.expected_manifests(self.root)['plugin.json']
        discovered = []
        for path in generated['skills']:
            discovered.extend(entry.parent.name for entry in (self.root / path).glob('*/SKILL.md'))
        self.assertCountEqual(discovered, [name for names in self.catalog.values() for name in names])
        self.assertEqual(len(discovered), len(set(discovered)))

    def test_checked_in_manifests_are_current_and_cover_real_catalog(self):
        generated = SYNC.sync(ROOT, check=True)['plugin.json']
        catalog = json.loads((ROOT / 'collections.json').read_text())
        discovered = [entry.parent.name for path in generated['skills']
                      for entry in (ROOT / path).glob('*/SKILL.md')]
        self.assertCountEqual(discovered, [name for names in catalog.values() for name in names])

    def test_check_missing_malformed_and_stale_files_without_writing(self):
        with self.assertRaisesRegex(ValueError, 'Missing'):
            SYNC.sync(self.root, check=True)
        self.assertFalse((self.root / '.claude-plugin').exists())
        SYNC.sync(self.root)
        path = self.root / '.claude-plugin' / 'plugin.json'
        path.write_text('{')
        with self.assertRaisesRegex(ValueError, 'Invalid JSON'):
            SYNC.sync(self.root, check=True)
        self.assertEqual(path.read_text(), '{')
        SYNC.sync(self.root)
        before = path.read_bytes()
        self.source['version'] = '0.3.0'
        self.write_inputs()
        with self.assertRaisesRegex(ValueError, 'Stale'):
            SYNC.sync(self.root, check=True)
        self.assertEqual(path.read_bytes(), before)
        SYNC.sync(self.root)
        self.assertEqual(json.loads(path.read_text())['version'], '0.3.0')

    def test_missing_and_uncatalogued_skills_are_rejected(self):
        entry = self.root / 'research' / 'research-example' / 'SKILL.md'
        original = entry.read_bytes()
        entry.unlink()
        with self.assertRaisesRegex(ValueError, 'Missing or indirect skill'):
            SYNC.sync(self.root)
        entry.write_bytes(original)
        extra = self.root / 'research' / 'extra-skill'
        extra.mkdir()
        (extra / 'SKILL.md').write_text('extra')
        with self.assertRaisesRegex(ValueError, 'Uncatalogued skill'):
            SYNC.sync(self.root)
        self.assertFalse((self.root / '.claude-plugin').exists())

    def test_duplicate_and_unsafe_catalog_names_are_rejected(self):
        for name, message in [('research-example', 'Duplicate'), ('../outside', 'Invalid skill name')]:
            with self.subTest(name=name):
                self.catalog['research'].append(name)
                self.write_inputs()
                with self.assertRaisesRegex(ValueError, message):
                    SYNC.sync(self.root)
                self.catalog['research'].pop()

    def test_default_skill_directory_cannot_add_uncatalogued_skills(self):
        (self.root / 'skills').mkdir()
        with self.assertRaisesRegex(ValueError, 'Unexpected root skills/'):
            SYNC.sync(self.root)

    def test_indirect_inputs_and_outputs_are_rejected(self):
        directory = self.root / '.claude-plugin'
        directory.symlink_to(self.root / 'submission', target_is_directory=True)
        before = (self.root / 'submission' / 'plugin.json').read_bytes()
        with self.assertRaisesRegex(ValueError, 'must not be a symlink'):
            SYNC.sync(self.root)
        self.assertEqual((self.root / 'submission' / 'plugin.json').read_bytes(), before)
        directory.unlink()
        entry = self.root / 'research' / 'research-example' / 'SKILL.md'
        entry.unlink()
        entry.symlink_to(self.root / 'submission' / 'plugin.json')
        with self.assertRaisesRegex(ValueError, 'Missing or indirect skill'):
            SYNC.sync(self.root)

    def test_malformed_release_inputs_fail_before_generating_files(self):
        self.source['author'] = []
        self.write_inputs()
        with self.assertRaisesRegex(ValueError, 'author must be an object'):
            SYNC.sync(self.root)
        self.assertFalse((self.root / '.claude-plugin').exists())


if __name__ == '__main__':
    unittest.main()
