"""Runner status/provenance tests using real staging and mocked model processes."""

from contextlib import redirect_stdout
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
CASE_SPEC = importlib.util.spec_from_file_location('review_cases', ROOT / 'submission/tests/review_cases.py')
CASES = importlib.util.module_from_spec(CASE_SPEC)
CASE_SPEC.loader.exec_module(CASES)
RUN_SPEC = importlib.util.spec_from_file_location('run_review_checks', ROOT / 'submission/tests/run_codex_review.py')
RUNNER = importlib.util.module_from_spec(RUN_SPEC)
with mock.patch.dict(sys.modules, {'review_cases': CASES}):
    RUN_SPEC.loader.exec_module(RUNNER)


class ReviewRunnerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='crypto-review-runner-test-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.submission = self.root / 'submission'
        self.submission.mkdir()
        for name in ('review-cases.json', 'development-cases.json', 'plugin.json'):
            shutil.copyfile(ROOT / 'submission' / name, self.submission / name)
        shutil.copyfile(ROOT / 'collections.json', self.root / 'collections.json')
        shutil.copytree(ROOT / 'submission/tests/fixtures', self.submission / 'tests/fixtures')
        manifest = json.loads((self.submission / 'plugin.json').read_text())
        self.archive = self.root / 'dist' / f'{manifest["name"]}-{manifest["version"]}.zip'
        self.archive.parent.mkdir()
        self.archive.write_bytes(b'synthetic candidate archive A')
        self.home = self.root / 'home'
        self.home.mkdir()
        self.output = self.root / 'results'
        self.calls = []
        self.model_exit = 0
        self.model_error = None
        self.model_effect = None
        self.check_exit = None
        self.check_error = None
        mkdtemp = tempfile.mkdtemp
        patches = [
            mock.patch.object(CASES, 'SUBMISSION', self.submission),
            mock.patch.object(CASES, 'CASE_FILE', self.submission / 'review-cases.json'),
            mock.patch.object(CASES.tempfile, 'mkdtemp',
                              side_effect=lambda **kwargs: mkdtemp(dir=self.root, **kwargs)),
            mock.patch.object(Path, 'home', return_value=self.home),
            mock.patch.object(RUNNER.subprocess, 'run', side_effect=self.run_process),
        ]
        for patcher in patches:
            patcher.start()
            self.addCleanup(patcher.stop)

    def run_process(self, command, **kwargs):
        self.calls.append(command)
        if command[1] == '--version':
            return subprocess.CompletedProcess(command, 0, stdout='codex test-version\n')
        if command[1] == 'exec':
            if self.model_error:
                raise self.model_error
            workspace = Path(command[command.index('--cd') + 1])
            if self.model_effect:
                self.model_effect(workspace)
            kwargs['stdout'].write('{"synthetic_event": true}\n')
            return subprocess.CompletedProcess(command, self.model_exit)
        self.assertEqual(Path(command[1]).name, 'review_cases.py')
        self.assertEqual(command[2], '--suite')
        suite, action, case_id = command[3:6]
        case = CASES.select(CASES.validate(suite), case_id)
        output = io.StringIO()
        if action == 'prepare':
            with redirect_stdout(output):
                CASES.prepare(case, suite)
            return subprocess.CompletedProcess(command, 0, stdout=output.getvalue())
        self.assertEqual(action, 'check')
        if self.check_error:
            raise self.check_error
        if self.check_exit is not None:
            return subprocess.CompletedProcess(command, self.check_exit, stdout='', stderr='synthetic checker error')
        with redirect_stdout(output):
            status = CASES.check(case, Path(command[6]), Path(command[7]), suite)
        return subprocess.CompletedProcess(command, status, stdout=output.getvalue(), stderr='')

    def run_cases(self, *arguments):
        argv = ['run_codex_review.py', '--output-dir', str(self.output), *arguments]
        with mock.patch.object(sys, 'argv', argv), redirect_stdout(io.StringIO()):
            return RUNNER.main()

    def record(self, case_id='P01'):
        return json.loads((self.output / case_id / 'run.json').read_text())

    def assert_unassessed(self, record):
        self.assertTrue(record['behavioral_grade'].startswith('NOT ASSESSED'))

    def test_success_keeps_mechanical_results_separate_from_behavioral_grade(self):
        self.assertEqual(self.run_cases('--case', 'P01'), 0)
        record = self.record()
        self.assertEqual(record['suite'], 'submission')
        self.assertEqual(record['exit_code'], 0)
        self.assertEqual(record['filesystem_check_exit_code'], 0)
        self.assertIsNone(record['filesystem_check_launch_error'])
        self.assert_unassessed(record)

    def test_codex_failure_retains_record_and_stops_before_next_case(self):
        self.model_exit = 7
        self.assertEqual(self.run_cases('--case', 'P01', '--case', 'P02'), 7)
        record = self.record()
        self.assertEqual(record['exit_code'], 7)
        self.assertEqual(record['filesystem_check_exit_code'], 0)
        self.assertFalse((self.output / 'P02').exists())
        self.assert_unassessed(record)

    def test_filesystem_violation_retains_record_and_returns_failure(self):
        self.model_effect = lambda workspace: (workspace / 'unrequested.txt').write_text('unexpected')
        self.assertEqual(self.run_cases('--case', 'P01'), 1)
        record = self.record()
        self.assertEqual(record['exit_code'], 0)
        self.assertEqual(record['filesystem_check_exit_code'], 1)
        self.assertEqual(json.loads(record['filesystem_check'])['added'], ['unrequested.txt'])
        self.assert_unassessed(record)

    def test_checker_execution_error_is_not_a_pass(self):
        self.check_exit = 2
        self.assertEqual(self.run_cases('--case', 'P01'), 2)
        record = self.record()
        self.assertEqual(record['filesystem_check_exit_code'], 2)
        self.assertEqual(record['filesystem_check_stderr'], 'synthetic checker error')
        self.assert_unassessed(record)

    def test_checker_launch_error_is_recorded_and_fails(self):
        self.check_error = OSError('synthetic checker launch failure')
        self.assertEqual(self.run_cases('--case', 'P01'), 1)
        record = self.record()
        self.assertIsNone(record['filesystem_check_exit_code'])
        self.assertIsNone(record['filesystem_check'])
        self.assertEqual(record['filesystem_check_launch_error'], 'synthetic checker launch failure')
        self.assert_unassessed(record)

    def test_model_launch_error_is_recorded_and_still_checks_workspace(self):
        self.model_error = OSError('synthetic model launch failure')
        self.assertEqual(self.run_cases('--case', 'P01'), 1)
        record = self.record()
        self.assertIsNone(record['exit_code'])
        self.assertEqual(record['model_launch_error'], 'synthetic model launch failure')
        self.assertEqual(record['filesystem_check_exit_code'], 0)
        self.assert_unassessed(record)

    def test_candidate_identity_does_not_claim_loaded_bytes_or_resolved_model(self):
        self.assertEqual(self.run_cases('--case', 'P01'), 0)
        first = self.record()
        self.assertEqual(first['candidate_archive_sha256'], hashlib.sha256(self.archive.read_bytes()).hexdigest())
        self.assertIn('candidate_plugin_version', first)
        self.assertNotIn('plugin_version', first)
        self.assertNotIn('archive_sha256', first)
        self.assertEqual(first['loaded_package_binding'], 'UNVERIFIED')
        self.assertIsNone(first['loaded_package_content_identity'])
        self.assertEqual(first['model_selection'], 'cli_default')
        self.assertIsNone(first['requested_model'])
        self.assertIsNone(first['resolved_model'])
        self.archive.write_bytes(b'synthetic candidate archive B')
        self.output = self.root / 'second-results'
        self.assertEqual(self.run_cases('--case', 'P01'), 0)
        second = self.record()
        self.assertNotEqual(first['candidate_archive_sha256'], second['candidate_archive_sha256'])
        self.assertEqual(second['loaded_package_binding'], 'UNVERIFIED')
        self.assertIsNone(second['loaded_package_content_identity'])

    def test_duplicate_suppression_records_only_discovered_default_personal_paths(self):
        skill = 'crypto-proof-auditor'
        source = self.root / 'standalone-source'
        source.mkdir()
        (source / 'SKILL.md').write_text('synthetic standalone skill')
        personal = self.home / '.agents/skills' / skill
        personal.parent.mkdir(parents=True)
        personal.symlink_to(source, target_is_directory=True)
        alternate = self.home / '.codex/skills' / skill
        alternate.mkdir(parents=True)
        (alternate / 'SKILL.md').write_text('uninspected alternate copy')
        self.assertEqual(self.run_cases('--case', 'P01'), 0)
        record = self.record()
        self.assertEqual(set(record['disabled_default_personal_skill_paths']),
                         {str(personal / 'SKILL.md'), str(source / 'SKILL.md')})
        self.assertIn('other discovery locations', record['environment_note'])
        self.assertNotIn(str(alternate), ' '.join(record['command']))

    def test_development_suite_is_forwarded_to_preparation_and_checking(self):
        self.model_effect = lambda workspace: (workspace / 'lemma.md').write_text('proposed proof')
        self.assertEqual(self.run_cases('--suite', 'development', '--case', 'D08'), 0)
        record = self.record('D08')
        self.assertEqual(record['suite'], 'development')
        self.assertEqual(record['filesystem_check_exit_code'], 0)
        self.assertEqual(json.loads(record['filesystem_check'])['permitted_content_changes'], ['lemma.md'])
        self.assert_unassessed(record)


if __name__ == '__main__':
    unittest.main()
