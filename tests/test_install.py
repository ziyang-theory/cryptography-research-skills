"""Exercise the installer CLI using temporary homes and real skill sources.

Run from the repository root with ``python3 -m unittest discover -s tests -v``.
No test writes to the user's home or changes the source skills.
"""

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / 'scripts' / 'install.py'
SPEC = importlib.util.spec_from_file_location('skill_installer', INSTALLER)
INSTALL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSTALL)
LEGACY_SELECTIONS = {
    'paper-writing': {
        'crypto-research-framing', 'cryptography-writing',
        'crypto-literature-evidence', 'crypto-proof-auditor',
        'crypto-prior-work-comparison', 'crypto-correlation-accounting',
        'crypto-manuscript-qa', 'crypto-ai-acknowledgements',
    },
    'implementation-and-artifacts': {
        'crypto-protocol-implementation', 'crypto-benchmarking',
        'crypto-implementation-evaluation-writing', 'crypto-research-artifacts',
    },
}


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='crypto-skills-test-')
        self.addCleanup(self.temporary.cleanup)
        # Relative fixture links must use the actual directory, including on
        # systems where the temporary directory's ancestors are symlinks.
        self.work = Path(self.temporary.name).resolve()
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

    def old_source(self, name):
        collection = next(key for key, names in LEGACY_SELECTIONS.items() if name in names)
        return ROOT / collection / name

    def test_default_is_codex_research(self):
        self.assert_success(self.run_cli())
        self.assert_links(self.destination('codex'), self.catalog['research'])
        self.assertFalse((self.home / '.claude').exists())

    def test_claude_defaults_to_its_personal_research_directory(self):
        self.assert_success(self.run_cli('--agent', 'claude'))
        self.assert_links(self.destination('claude'), self.catalog['research'])
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

    def test_each_collection_can_be_installed_alone(self):
        for agent in ('codex', 'claude'):
            for collection in ('research', 'writing', 'implementation'):
                with self.subTest(agent=agent, collection=collection):
                    home = self.work / f'{agent}-{collection}'
                    self.assert_success(self.run_cli(
                        '--agent', agent, '--collection', collection, home=home,
                    ))
                    self.assert_links(self.destination(agent, home), self.catalog[collection])

    def test_legacy_selections_keep_exact_original_membership(self):
        for collection, names in LEGACY_SELECTIONS.items():
            with self.subTest(collection=collection):
                destination = self.work / collection
                result = self.run_cli('--collection', collection, '--destination', destination)
                self.assert_success(result)
                self.assertIn('deprecated', result.stderr)
                self.assert_links(destination, names)

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
                self.assert_links(destination, self.catalog['research'])
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
                self.assert_links(destination, self.catalog['research'])
                self.assertEqual(
                    {path.name: path.lstat().st_ino for path in destination.iterdir()},
                    original,
                )

    def test_late_conflict_prevents_all_new_links_for_either_agent(self):
        name = self.catalog['research'][-1]
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

    def test_existing_old_source_links_are_retargeted_for_all_skills(self):
        destination = self.destination('codex')
        destination.mkdir(parents=True)
        for index, name in enumerate(self.sources):
            old = self.old_source(name)
            # Both absolute and relative links installed before the move are supported.
            value = old if index % 2 else os.path.relpath(old, destination)
            (destination / name).symlink_to(value, target_is_directory=True)
        self.assert_success(self.run_cli('--collection', 'all'))
        self.assert_links(destination, self.sources)

    def test_migration_dry_run_preserves_links_and_creates_nothing(self):
        destination = self.destination('codex')
        destination.mkdir(parents=True)
        name = self.catalog['research'][0]
        link = destination / name
        old = os.path.relpath(self.old_source(name), destination)
        link.symlink_to(old, target_is_directory=True)
        original_inode = link.lstat().st_ino
        result = self.run_cli('--dry-run')
        self.assert_success(result)
        self.assertIn('Would retarget', result.stdout)
        self.assertEqual(os.readlink(link), old)
        self.assertEqual(link.lstat().st_ino, original_inode)
        self.assertEqual(list(destination.iterdir()), [link])

    def test_old_path_from_another_checkout_or_wrong_skill_is_a_conflict(self):
        name = self.catalog['research'][0]
        other = self.catalog['research'][1]
        for label, source in (
            ('other-checkout', self.work / 'other-checkout' / 'paper-writing' / name),
            ('wrong-skill', self.old_source(other)),
            ('wrong-collection', ROOT / 'implementation-and-artifacts' / name),
        ):
            with self.subTest(link=label):
                destination = self.work / label
                destination.mkdir()
                link = destination / name
                link.symlink_to(source, target_is_directory=True)
                original_inode = link.lstat().st_ino
                result = self.run_cli('--destination', destination)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(os.readlink(link), str(source))
                self.assertEqual(link.lstat().st_ino, original_inode)
                self.assertEqual(list(destination.iterdir()), [link])

    def test_late_conflict_prevents_retargeting_earlier_old_link(self):
        destination = self.destination('codex')
        destination.mkdir(parents=True)
        name = self.catalog['research'][0]
        link = destination / name
        link.symlink_to(self.old_source(name), target_is_directory=True)
        original_inode = link.lstat().st_ino
        conflict = destination / self.catalog['research'][-1]
        conflict.write_text('keep me', encoding='utf-8')
        result = self.run_cli()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(os.readlink(link), str(self.old_source(name)))
        self.assertEqual(link.lstat().st_ino, original_inode)
        self.assertEqual(conflict.read_text(encoding='utf-8'), 'keep me')
        self.assertEqual(set(destination.iterdir()), {link, conflict})

    def test_symlink_ancestor_followed_by_parent_is_not_mistaken_for_old_source(self):
        name = self.catalog['research'][0]
        checkout = self.work / 'checkout'
        source = checkout / 'research' / name
        source.mkdir(parents=True)
        (source / 'SKILL.md').write_text('temporary source', encoding='utf-8')
        elsewhere = self.work / 'elsewhere' / 'nested'
        elsewhere.mkdir(parents=True)
        (checkout / 'alias').symlink_to(elsewhere, target_is_directory=True)
        destination = self.work / 'installed'
        destination.mkdir()
        link = destination / name
        unrelated = checkout / 'alias' / '..' / 'paper-writing' / name
        link.symlink_to(unrelated, target_is_directory=True)
        original_inode = link.lstat().st_ino
        self.assertEqual(Path(os.path.abspath(unrelated)), checkout / 'paper-writing' / name)
        self.assertEqual(unrelated.resolve(), elsewhere.parent / 'paper-writing' / name)
        with self.assertRaisesRegex(ValueError, 'nothing changed'):
            INSTALL.install({name: ('research', source.resolve())}, destination, root=checkout)
        self.assertEqual(os.readlink(link), str(unrelated))
        self.assertEqual(link.lstat().st_ino, original_inode)
        self.assertEqual(list(destination.iterdir()), [link])

    def test_creation_failure_rolls_back_new_and_migrated_links(self):
        skills = INSTALL.load_skills(ROOT)
        selected = {name: skills[name] for name in self.catalog['research']}
        names = list(selected)
        # Exercise both failure after a completed migration and failure during retargeting.
        for failure_index in (2, 0):
            with self.subTest(failure_index=failure_index):
                destination = self.work / f'rollback-{failure_index}'
                destination.mkdir()
                old_link = destination / names[0]
                previous = os.path.relpath(self.old_source(names[0]), destination)
                old_link.symlink_to(previous, target_is_directory=True)
                unchanged = destination / names[-1]
                unchanged.symlink_to(self.sources[names[-1]], target_is_directory=True)
                unchanged_inode = unchanged.lstat().st_ino
                failure_target = destination / names[failure_index]
                original_symlink_to = Path.symlink_to
                failures = []

                def fail_once(path, target, target_is_directory=False):
                    if path == failure_target and not failures:
                        failures.append(path)
                        raise OSError('injected creation failure')
                    return original_symlink_to(path, target, target_is_directory)

                with mock.patch.object(Path, 'symlink_to', fail_once):
                    with self.assertRaisesRegex(OSError, 'injected creation failure'):
                        INSTALL.install(selected, destination)
                self.assertEqual(failures, [failure_target])
                self.assertEqual(set(destination.iterdir()), {old_link, unchanged})
                self.assertEqual(os.readlink(old_link), previous)
                self.assertEqual(unchanged.lstat().st_ino, unchanged_inode)


if __name__ == '__main__':
    unittest.main()
