#!/usr/bin/env python3
"""Run prepared review prompts through an installed plugin; do not auto-grade prose.

Requires a working, authenticated Codex CLI and the personal plugin installation.
Uses per-invocation configuration; does not change the user's saved skill settings.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import review_cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--codex', default='codex', help='Codex CLI executable')
    parser.add_argument('--suite', choices=review_cases.SUITES, default='submission')
    parser.add_argument('--case', action='append', dest='case_ids', help='Case ID; repeat to select multiple')
    parser.add_argument('--output-dir', type=Path, help='Directory for traces and results; default: new temporary directory')
    parser.add_argument('--candidate-archive', type=Path,
                        help='Candidate ZIP to hash (default: dist/<plugin>-<version>.zip); does not install it')
    args = parser.parse_args()
    cases = review_cases.validate(args.suite)
    if args.case_ids:
        cases = [review_cases.select(cases, case_id) for case_id in args.case_ids]
    output = args.output_dir or Path(tempfile.mkdtemp(prefix='crypto-plugin-behavior-'))
    output = output.absolute()
    output.mkdir(parents=True, exist_ok=True)
    root = review_cases.SUBMISSION.parent
    manifest = json.loads((review_cases.SUBMISSION / 'plugin.json').read_text())
    archive = (args.candidate_archive or root / 'dist' / f'{manifest["name"]}-{manifest["version"]}.zip')
    archive = archive.expanduser().absolute()
    startup_path = output / 'startup.json'
    version_command = [args.codex, '--version']
    startup = {
        'suite': args.suite, 'started_at': datetime.now(timezone.utc).isoformat(),
        'finished_at': None, 'status': 'STARTING', 'phase': 'candidate_archive',
        'cases': [{'case_id': case['id'], 'status': 'NOT STARTED'} for case in cases],
        'source_manifest_version': manifest['version'], 'candidate_plugin_version': None,
        'candidate_archive_path': str(archive), 'candidate_archive_sha256': None,
        'codex_version': None, 'command': version_command,
        'exit_code': None, 'error_type': None, 'error': None,
        'stdout': None, 'stderr': None,
        'loaded_package_binding': 'UNVERIFIED', 'loaded_package_content_identity': None,
        'behavioral_grade': 'NOT RUN: no case has started at initialization',
    }
    try:
        with startup_path.open('x', encoding='utf-8') as stream:
            stream.write(json.dumps(startup, indent=2) + '\n')
    except OSError as error:
        print(f'Cannot create startup record {startup_path}: {error}. Use a new output directory.', file=sys.stderr)
        return 1
    try:
        if not archive.is_file():
            raise ValueError(f'Candidate archive is missing or is not a regular file: {archive}')
        archive_hash = hashlib.sha256(archive.read_bytes()).hexdigest()
        startup['candidate_archive_sha256'] = archive_hash
        startup['phase'] = 'codex_version'
        version = subprocess.run(version_command, capture_output=True, text=True, check=True).stdout.strip()
        startup['codex_version'] = version
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        startup.update({
            'status': 'FAILED', 'finished_at': datetime.now(timezone.utc).isoformat(),
            'error_type': type(error).__name__, 'error': str(error),
            'exit_code': getattr(error, 'returncode', None),
            'stdout': getattr(error, 'stdout', None), 'stderr': getattr(error, 'stderr', None),
        })
        startup_path.write_text(json.dumps(startup, indent=2) + '\n', encoding='utf-8')
        if startup['phase'] == 'candidate_archive':
            remedy = ('Build the default candidate with python3 scripts/build_plugin.py '
                      'from the repository root, or pass --candidate-archive PATH to a readable ZIP.')
        else:
            remedy = 'Check --codex and confirm that the executable runs successfully with --version.'
        print(f'Startup failed: {error}. {remedy} Inspect {startup_path}.', file=sys.stderr)
        return getattr(error, 'returncode', None) or 1
    startup.update({'status': 'PASSED', 'finished_at': datetime.now(timezone.utc).isoformat(), 'exit_code': 0})
    startup_path.write_text(json.dumps(startup, indent=2) + '\n', encoding='utf-8')
    # Suppress discovered default personal .agents copies and their resolved
    # targets only. Other skill discovery locations are not inspected here.
    catalog = json.loads((root / 'collections.json').read_text())
    disabled = set()
    for names in catalog.values():
        for name in names:
            path = Path.home() / '.agents' / 'skills' / name / 'SKILL.md'
            if path.is_file():
                disabled.update((str(path), str(path.resolve())))
    skill_config = 'skills.config=[' + ','.join(
        '{path=' + json.dumps(path) + ',enabled=false}' for path in sorted(disabled)
    ) + ']'
    for case in cases:
        case_root = output / case['id']
        case_root.mkdir(exist_ok=False)
        prepared = subprocess.run(
            [sys.executable, str(Path(__file__).with_name('review_cases.py')),
             '--suite', args.suite, 'prepare', case['id']],
            capture_output=True, text=True, check=True,
        )
        staging = json.loads(prepared.stdout)
        (case_root / 'staging.json').write_text(prepared.stdout)
        command = [args.codex, 'exec', '--ignore-user-config', '--strict-config',
                   '-c', 'plugins={' + json.dumps(manifest['name'] + '@personal') + '={enabled=true}}',
                   '-c', skill_config, '--ephemeral', '--skip-git-repo-check',
                   '--sandbox', 'workspace-write', '--cd', staging['workspace'],
                   '--json', '--output-last-message', str(case_root / 'response.md'), '-']
        started = datetime.now(timezone.utc).isoformat()
        print(f'RUN {case["id"]}: {case_root}', flush=True)
        model_exit_code = None
        model_launch_error = None
        with (case_root / 'events.jsonl').open('w') as events, (case_root / 'stderr.log').open('w') as errors:
            try:
                result = subprocess.run(command, input=staging['prompt'], text=True, stdout=events, stderr=errors)
                model_exit_code = result.returncode
            except OSError as error:
                model_launch_error = str(error)
                errors.write(model_launch_error + '\n')
        check_exit_code = None
        check_output = None
        check_stderr = None
        check_launch_error = None
        try:
            check = subprocess.run(
                [sys.executable, str(Path(__file__).with_name('review_cases.py')),
                 '--suite', args.suite, 'check', case['id'],
                 staging['workspace'], staging['snapshot']], capture_output=True, text=True,
            )
            check_exit_code = check.returncode
            check_output = check.stdout.strip()
            check_stderr = check.stderr.strip()
        except OSError as error:
            check_launch_error = str(error)
        record = {
            'suite': args.suite, 'case_id': case['id'], 'started_at': started,
            'finished_at': datetime.now(timezone.utc).isoformat(),
            'codex_version': version, 'source_manifest_version': manifest['version'],
            'candidate_plugin_version': None,
            'candidate_archive_sha256': archive_hash, 'candidate_archive_path': str(archive),
            'loaded_package_binding': 'UNVERIFIED', 'loaded_package_content_identity': None,
            'loaded_package_binding_reason': 'The runner enables the installed plugin by name; it does not establish its loading origin or content.',
            'model_selection': 'cli_default', 'requested_model': None, 'resolved_model': None,
            'disabled_default_personal_skill_paths': sorted(disabled), 'command': command,
            'exit_code': model_exit_code, 'model_launch_error': model_launch_error,
            'filesystem_check_exit_code': check_exit_code,
            'filesystem_check': check_output, 'filesystem_check_stderr': check_stderr,
            'filesystem_check_launch_error': check_launch_error,
            'behavioral_grade': 'NOT ASSESSED: manually review response and visible tool trace',
            'environment_note': 'Fresh case workspace and ephemeral session; user config ignored. Only discovered ~/.agents/skills/<name>/SKILL.md paths and their resolved targets are disabled per invocation; other discovery locations and system/global instructions may still apply. CLI default model used; resolved model unknown. Candidate archive identity is not bound to loaded instructions.',
        }
        (case_root / 'run.json').write_text(json.dumps(record, indent=2) + '\n')
        print(f'DONE {case["id"]}: cli={model_exit_code}, filesystem={check_exit_code}', flush=True)
        if model_exit_code != 0 or check_exit_code != 0:
            print(f'Inspect {case_root / "run.json"} and stderr.log before continuing.', flush=True)
            return model_exit_code or check_exit_code or 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
