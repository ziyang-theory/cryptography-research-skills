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
    parser.add_argument('--case', action='append', dest='case_ids', help='Case ID; repeat to select multiple')
    parser.add_argument('--output-dir', type=Path, help='Directory for traces and results; default: new temporary directory')
    args = parser.parse_args()
    cases = review_cases.validate()
    if args.case_ids:
        cases = [review_cases.select(cases, case_id) for case_id in args.case_ids]
    output = args.output_dir or Path(tempfile.mkdtemp(prefix='crypto-plugin-behavior-'))
    output = output.absolute()
    output.mkdir(parents=True, exist_ok=True)
    root = review_cases.SUBMISSION.parent
    manifest = json.loads((review_cases.SUBMISSION / 'plugin.json').read_text())
    archive = root / 'dist' / f'{manifest["name"]}-{manifest["version"]}.zip'
    archive_hash = hashlib.sha256(archive.read_bytes()).hexdigest()
    version = subprocess.run([args.codex, '--version'], capture_output=True, text=True, check=True).stdout.strip()
    # Disable only the standalone duplicates, including both the link and its
    # resolved source path, for this invocation. The plugin cache stays enabled.
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
            [sys.executable, str(Path(__file__).with_name('review_cases.py')), 'prepare', case['id']],
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
        with (case_root / 'events.jsonl').open('w') as events, (case_root / 'stderr.log').open('w') as errors:
            result = subprocess.run(command, input=staging['prompt'], text=True, stdout=events, stderr=errors)
        check = subprocess.run(
            [sys.executable, str(Path(__file__).with_name('review_cases.py')), 'check', case['id'],
             staging['workspace'], staging['snapshot']], capture_output=True, text=True,
        )
        record = {
            'case_id': case['id'], 'started_at': started,
            'finished_at': datetime.now(timezone.utc).isoformat(),
            'codex_version': version, 'plugin_version': manifest['version'],
            'archive_sha256': archive_hash, 'command': command,
            'exit_code': result.returncode, 'filesystem_check_exit_code': check.returncode,
            'filesystem_check': check.stdout.strip(), 'filesystem_check_stderr': check.stderr.strip(),
            'behavioral_grade': 'NOT ASSESSED: manually review response and visible tool trace',
            'environment_note': 'Fresh case workspace and ephemeral session; user config ignored; standalone duplicates disabled per invocation. System/global instructions may still apply. CLI default model used.',
        }
        (case_root / 'run.json').write_text(json.dumps(record, indent=2) + '\n')
        print(f'DONE {case["id"]}: cli={result.returncode}, filesystem={check.returncode}', flush=True)
        if result.returncode:
            print(f'Inspect {case_root / "stderr.log"} before continuing.', flush=True)
            return result.returncode
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
