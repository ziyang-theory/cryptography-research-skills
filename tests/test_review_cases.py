"""Fixture/staging checks and finite supporting oracles, not behavioral grades."""

from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
import importlib.util
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('review_case_checks', ROOT / 'submission/tests/review_cases.py')
CASES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CASES)


class ReviewCaseTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='crypto-review-case-test-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.submission = self.root / 'submission'
        self.submission.mkdir()
        for name in ('review-cases.json', 'development-cases.json'):
            shutil.copyfile(ROOT / 'submission' / name, self.submission / name)
        shutil.copytree(ROOT / 'submission/tests/fixtures', self.submission / 'tests/fixtures')
        for attribute, value in (('SUBMISSION', self.submission),
                                 ('CASE_FILE', self.submission / 'review-cases.json')):
            patcher = mock.patch.object(CASES, attribute, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        mkdtemp = tempfile.mkdtemp
        patcher = mock.patch.object(CASES.tempfile, 'mkdtemp',
                                   side_effect=lambda **kwargs: mkdtemp(dir=self.root, **kwargs))
        patcher.start()
        self.addCleanup(patcher.stop)

    def stage(self, case_id, suite='submission'):
        case = CASES.select(CASES.validate(suite), case_id)
        output = io.StringIO()
        with redirect_stdout(output):
            CASES.prepare(case, suite)
        staging = json.loads(output.getvalue())
        return case, Path(staging['workspace']), Path(staging['snapshot'])

    def check(self, case, workspace, snapshot, suite='submission'):
        output = io.StringIO()
        with redirect_stdout(output):
            result = CASES.check(case, workspace, snapshot, suite)
        return result, json.loads(output.getvalue())

    def test_submission_remains_the_api_and_cli_default(self):
        self.assertEqual(CASES.read_cases(), CASES.read_cases('submission'))
        self.assertEqual([case['id'] for case in CASES.validate()],
                         ['P01', 'P02', 'P03', 'P04', 'P05', 'N01', 'N02', 'N03'])
        with mock.patch.object(sys, 'argv', ['review_cases.py', 'validate']), redirect_stdout(io.StringIO()):
            self.assertEqual(CASES.main(), 0)
        case, workspace, snapshot = self.stage('P01')
        self.assertEqual(self.check(case, workspace, snapshot)[0], 0)

    def test_all_development_cases_validate_and_cli_selects_them(self):
        self.assertEqual([case['id'] for case in CASES.validate('development')],
                         [f'D{i:02}' for i in range(1, 9)])
        with mock.patch.object(sys, 'argv', ['review_cases.py', '--suite', 'development', 'validate']), \
                redirect_stdout(io.StringIO()):
            self.assertEqual(CASES.main(), 0)
        with self.assertRaisesRegex(ValueError, 'Unknown review suite'):
            CASES.read_cases('other')

    def test_staging_copies_only_inputs_and_keeps_rubrics_outside(self):
        for suite in CASES.SUITES:
            for case in CASES.validate(suite):
                with self.subTest(suite=suite, case=case['id']):
                    _, workspace, snapshot = self.stage(case['id'], suite)
                    self.assertEqual(CASES.file_bytes(workspace), CASES.file_bytes(CASES.fixture_path(case)))
                    self.assertFalse(snapshot.is_relative_to(workspace))
                    self.assertFalse(any(path.name.endswith('-cases.json') for path in workspace.rglob('*')))
                    record = json.loads(snapshot.read_text())
                    self.assertEqual(record['suite'], suite)
                    self.assertNotIn('required_rubric', record)

    def test_exact_replacement_still_requires_the_original_one_word_edit(self):
        case, workspace, snapshot = self.stage('P02')
        self.assertEqual(self.check(case, workspace, snapshot)[0], 1)
        rule = case['filesystem_rule']
        source = workspace / rule['path']
        source.write_bytes(source.read_bytes().replace(rule['old'].encode(), rule['new'].encode(), 1))
        self.assertEqual(self.check(case, workspace, snapshot)[0], 0)
        source.write_bytes(source.read_bytes() + b'\n')
        self.assertEqual(self.check(case, workspace, snapshot)[0], 1)

    def test_unchanged_rule_detects_content_addition_and_deletion(self):
        for change in ('edit', 'add', 'delete'):
            with self.subTest(change=change):
                case, workspace, snapshot = self.stage('P01')
                original = next(path for path in workspace.rglob('*') if path.is_file())
                if change == 'edit':
                    original.write_bytes(original.read_bytes() + b'changed')
                elif change == 'add':
                    (workspace / 'new.txt').write_text('unexpected')
                else:
                    original.unlink()
                self.assertEqual(self.check(case, workspace, snapshot)[0], 1)

    def test_allowed_changes_permits_only_existing_named_content(self):
        case = CASES.select(CASES.validate('development'), 'D08')
        (CASES.fixture_path(case) / 'protected.txt').write_text('must remain unchanged')
        for change in ('none', 'permitted', 'unrelated', 'add', 'delete', 'symlink'):
            with self.subTest(change=change):
                case, workspace, snapshot = self.stage('D08', 'development')
                source = workspace / 'lemma.md'
                if change == 'permitted':
                    source.write_bytes(source.read_bytes() + b'\nA proposed proof.\n')
                elif change == 'unrelated':
                    (workspace / 'protected.txt').write_text('changed')
                elif change == 'add':
                    (workspace / 'new.txt').write_text('unexpected')
                elif change == 'delete':
                    source.unlink()
                elif change == 'symlink':
                    source.unlink()
                    source.symlink_to(workspace / 'protected.txt')
                    with self.assertRaisesRegex(ValueError, 'Symlink'):
                        self.check(case, workspace, snapshot, 'development')
                    continue
                code, result = self.check(case, workspace, snapshot, 'development')
                self.assertEqual(code, 0 if change in ('none', 'permitted') else 1)
                self.assertTrue(result['behavioral_grade'].startswith('NOT ASSESSED'))
                if change == 'permitted':
                    self.assertEqual(result['permitted_content_changes'], ['lemma.md'])

    def test_allowed_change_paths_must_name_distinct_existing_files(self):
        case = CASES.select(CASES.validate('development'), 'D08')
        for paths in ([], ['absent.md'], ['../lemma.md'], ['/lemma.md'], ['lemma.md', 'lemma.md'], [42]):
            with self.subTest(paths=paths):
                changed = dict(case, filesystem_rule={'mode': 'allowed_changes', 'paths': paths})
                with self.assertRaisesRegex(ValueError, 'distinct existing fixture files'):
                    CASES.expected_files(changed)

    def test_snapshot_is_bound_to_suite_workspace_and_case_definition(self):
        case, workspace, snapshot = self.stage('D08', 'development')
        with self.assertRaisesRegex(ValueError, 'Snapshot does not belong'):
            self.check(case, workspace, snapshot)
        CASES.case_file('development').write_text(CASES.case_file('development').read_text() + '\n')
        with self.assertRaisesRegex(ValueError, 'Case definitions changed'):
            self.check(case, workspace, snapshot, 'development')


class DevelopmentOracleTests(unittest.TestCase):
    def test_d01_accounting_oracle_uses_declared_units(self):
        data = json.loads((ROOT / 'submission/tests/fixtures/development/d01/correlations.json').read_text())
        calls = data['calls']
        coordinates = sum(call['coordinates'] for call in calls)
        generated = sum(call['coordinates'] * call['width'] for call in calls)
        usable = sum(call['usable_entries'] for call in calls)
        online = usable * data['encoding_bits_per_field_element'] * sum(
            data['online_field_elements_per_usable_entry'].values())
        self.assertEqual((coordinates, generated, usable, generated - usable, online), (11, 22, 20, 2, 200))
        self.assertEqual(len(calls), 3)  # Total is 3 * alpha + 200 logical bits.
        self.assertEqual(data['setup_bits_per_call'], 'alpha')

    def test_d02_like_for_like_synthetic_comparisons(self):
        data = json.loads((ROOT / 'submission/tests/fixtures/development/d02/observations.json').read_text())
        a, b = data['records']
        for row in (a, b):
            self.assertEqual(row['setup_ms'] + row['online_ms'], row['total_wall_ms'])
        self.assertEqual(Fraction(b['online_ms'], a['online_ms']), Fraction(5, 4))
        self.assertEqual(Fraction(a['total_wall_ms'], b['total_wall_ms']), Fraction(10, 7))
        sent_a = a['p0_sent_online_bytes'] + a['p1_sent_online_bytes']
        sent_b = b['p0_sent_online_bytes'] + b['p1_sent_online_bytes']
        self.assertEqual((sent_a, sent_b), (20000, 18000))
        self.assertEqual(Fraction(sent_a - sent_b, sent_a), Fraction(1, 10))

    def test_d03_intentional_invalid_input_discrepancy(self):
        path = ROOT / 'submission/tests/fixtures/development/d03/protocol.py'
        namespace = {}
        exec(compile(path.read_text(), str(path), 'exec'), namespace)
        operation = namespace['OneUseMask'](3)
        self.assertEqual(operation.apply('17'), 3)  # The specification requires rejection.
        self.assertTrue(operation.used)
        retry = namespace['OneUseMask'](3)
        with self.assertRaises(ValueError):
            retry.apply(' 1')
        self.assertFalse(retry.used)
        self.assertEqual(retry.apply('16'), 2)

    def test_d05_d06_joint_distribution_oracles(self):
        # Finite supporting checks of the fixture's symbolic arguments. These
        # checks neither grade model responses nor prove the all-q statements.
        for q in (2, 3, 5):
            simulated = Counter((u, v, (u + v) % q) for u in range(q) for v in range(q))
            for x in range(q):
                valid = Counter((r, (x + s) % q, (r + x + s) % q)
                                for r in range(q) for s in range(q))
                self.assertEqual(valid, simulated)
                invalid = Counter((r, (x + r) % q, (2 * r + x) % q) for r in range(q))
                support = invalid.keys() | simulated.keys()
                distance = sum(abs(Fraction(invalid[v], q) - Fraction(simulated[v], q * q))
                               for v in support) / 2
                self.assertEqual(distance, 1 - Fraction(1, q))
                self.assertEqual(sum(count for (a, b, _), count in invalid.items()
                                     if (b - a) % q == x), q)
            invalid_zero = {(r, r, (2 * r) % q) for r in range(q)}
            invalid_one = {(r, (1 + r) % q, (2 * r + 1) % q) for r in range(q)}
            self.assertFalse(invalid_zero & invalid_one)

    def test_d07_d08_affine_uniformity_oracle(self):
        for q in (2, 3, 5):
            for a in range(1, q):
                inverse = pow(a, -1, q)
                for b in range(q):
                    images = Counter((a * r + b) % q for r in range(q))
                    self.assertEqual(images, Counter(range(q)))
                    for target in range(q):
                        preimage = inverse * (target - b) % q
                        self.assertEqual((a * preimage + b) % q, target)


if __name__ == '__main__':
    unittest.main()
