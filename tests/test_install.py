"""Exercise the installer CLI using temporary homes and real skill sources.

Run from the repository root with ``python3 -m unittest discover -s tests -v``.
No test writes to the user's home or changes the source skills.
"""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / 'scripts' / 'install.py'


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='crypto-skills-test-')
        self.addCleanup(self.temporary.cleanup)
        self.work = Path(self.temporary.name)
        self.home = self.work / 'home'
        self.home.mkdir()
        self.catalog = json.loads((ROOT / 'collections.json').read_text(encoding='utf-8'))
        self.sources = {
            name: ROOT / collection / name
            for collection, names in self.catalog.items()
            for name in names
        }

    def run_cli(self, *args, home=None):
        environment = os.environ.copy()
        environment['HOME'] = str(home or self.home)
        environment['USERPROFILE'] = environment['HOME']
        return subprocess.run(
            [sys.executable, str(INSTALLER), *map(str, args)],
            cwd=self.work,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )

    def destination(self, agent, home=None):
        directory = '.agents' if agent == 'codex' else '.claude'
        return (home or self.home) / directory / 'skills'

    def assert_success(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def assert_links(self, destination, names):
        self.assertEqual({path.name for path in destination.iterdir()}, set(names))
        for name in names:
            with self.subTest(skill=name):
                link = destination / name
                self.assertTrue(link.is_symlink(), str(link))
                self.assertEqual(link.resolve(), self.sources[name].resolve())
                self.assertEqual(
                    (link / 'SKILL.md').read_bytes(),
                    (self.sources[name] / 'SKILL.md').read_bytes(),
                )

    def test_default_remains_codex_paper_writing(self):
        self.assert_success(self.run_cli())
        self.assert_links(self.destination('codex'), self.catalog['paper-writing'])
        self.assertFalse((self.home / '.claude').exists())

    def test_claude_defaults_to_its_personal_paper_writing_directory(self):
        self.assert_success(self.run_cli('--agent', 'claude'))
        self.assert_links(self.destination('claude'), self.catalog['paper-writing'])
        self.assertFalse((self.home / '.agents').exists())

    def test_both_agents_share_sources_and_can_read_references(self):
        for agent in ('codex', 'claude'):
            self.assert_success(self.run_cli('--agent', agent, '--collection', 'all'))
            self.assert_links(self.destination(agent), self.sources)
        references_checked = 0
        for name, source in self.sources.items():
            for reference in (source / 'references').rglob('*'):
                if reference.is_file():
                    relative = reference.relative_to(source)
                    codex = self.destination('codex') / name / relative
                    claude = self.destination('claude') / name / relative
                    self.assertEqual(codex.resolve(), reference.resolve())
                    self.assertEqual(claude.resolve(), reference.resolve())
                    self.assertEqual(codex.read_bytes(), claude.read_bytes())
                    references_checked += 1
        self.assertGreater(references_checked, 0)

    def test_implementation_collection_can_be_installed_alone(self):
        for agent in ('codex', 'claude'):
            with self.subTest(agent=agent):
                self.assert_success(self.run_cli(
                    '--agent', agent, '--collection', 'implementation-and-artifacts',
                ))
                self.assert_links(
                    self.destination(agent), self.catalog['implementation-and-artifacts'],
                )

    def test_explicit_destination_overrides_defaults_and_preserves_old_syntax(self):
        for label, agent_arguments in (
            ('original', ()),
            ('codex', ('--agent', 'codex')),
            ('claude', ('--agent', 'claude')),
        ):
            with self.subTest(syntax=label):
                destination = self.work / label / 'custom skills'
                self.assert_success(self.run_cli(
                    *agent_arguments, '--destination', destination,
                ))
                self.assert_links(destination, self.catalog['paper-writing'])
        self.assertFalse((self.home / '.agents').exists())
        self.assertFalse((self.home / '.claude').exists())

    def test_one_skill_selection_works_for_either_agent(self):
        name = 'crypto-benchmarking'
        for agent in ('codex', 'claude'):
            with self.subTest(agent=agent):
                self.assert_success(self.run_cli('--agent', agent, '--skill', name))
                self.assert_links(self.destination(agent), [name])

    def test_dry_run_creates_no_destination(self):
        for agent in ('codex', 'claude'):
            with self.subTest(agent=agent):
                result = self.run_cli('--agent', agent, '--dry-run')
                self.assert_success(result)
                self.assertIn(str(self.destination(agent)), result.stdout)
                self.assertFalse(self.destination(agent).parent.exists())
        custom = self.work / 'not-created' / 'skills'
        self.assert_success(self.run_cli(
            '--agent', 'claude', '--destination', custom, '--dry-run',
        ))
        self.assertFalse(custom.parent.exists())

    def test_reinstall_preserves_existing_matching_links(self):
        for agent in ('codex', 'claude'):
            with self.subTest(agent=agent):
                self.assert_success(self.run_cli('--agent', agent))
                destination = self.destination(agent)
                original = {path.name: path.lstat().st_ino for path in destination.iterdir()}
                result = self.run_cli('--agent', agent)
                self.assert_success(result)
                self.assertIn('already linked', result.stdout)
                self.assert_links(destination, self.catalog['paper-writing'])
                self.assertEqual(
                    {path.name: path.lstat().st_ino for path in destination.iterdir()},
                    original,
                )

    def test_late_conflict_prevents_all_new_links_for_either_agent(self):
        name = self.catalog['paper-writing'][-1]
        for agent in ('codex', 'claude'):
            for kind in ('file', 'directory', 'broken-symlink', 'different-symlink'):
                with self.subTest(agent=agent, conflict=kind):
                    home = self.work / f'{agent}-{kind}'
                    destination = self.destination(agent, home)
                    destination.mkdir(parents=True)
                    conflict = destination / name
                    if kind == 'file':
                        conflict.write_text('keep this file', encoding='utf-8')
                    elif kind == 'directory':
                        conflict.mkdir()
                        (conflict / 'sentinel').write_text('keep this directory', encoding='utf-8')
                    elif kind == 'broken-symlink':
                        conflict.symlink_to(home / 'missing')
                    else:
                        other = home / 'other-source'
                        other.mkdir()
                        conflict.symlink_to(other, target_is_directory=True)
                    original_inode = conflict.lstat().st_ino
                    result = self.run_cli('--agent', agent, home=home)
                    self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertIn(str(conflict), result.stderr)
                    self.assertEqual({path.name for path in destination.iterdir()}, {name})
                    self.assertEqual(conflict.lstat().st_ino, original_inode)
                    if kind == 'file':
                        self.assertEqual(conflict.read_text(encoding='utf-8'), 'keep this file')
                    elif kind == 'directory':
                        self.assertEqual(
                            (conflict / 'sentinel').read_text(encoding='utf-8'),
                            'keep this directory',
                        )


if __name__ == '__main__':
    unittest.main()
