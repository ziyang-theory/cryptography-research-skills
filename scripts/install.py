#!/usr/bin/env python3
"""Install shared skills for Codex or Claude Code using directory symlinks."""

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENT_SKILL_PATHS = {
    'codex': ('.agents', 'skills'),
    'claude': ('.claude', 'skills'),
}


def load_skills(root):
    catalog = json.loads((root / 'collections.json').read_text(encoding='utf-8'))
    expected = {'paper-writing', 'implementation-and-artifacts'}
    if set(catalog) != expected:
        raise ValueError('The catalog must contain the two documented collections')
    skills = {}
    for collection, names in catalog.items():
        if not isinstance(names, list) or not names:
            raise ValueError(f'Invalid collection: {collection}')
        for name in names:
            if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
                raise ValueError(f'Invalid skill name: {name!r}')
            if name in skills:
                raise ValueError(f'Duplicate skill name: {name}')
            source = root / collection / name
            if source.is_symlink() or not (source / 'SKILL.md').is_file():
                raise ValueError(f'Missing or indirect source skill: {source}')
            skills[name] = (collection, source.resolve())
    return skills


def install(skills, destination, dry_run=False):
    destination = destination.expanduser().absolute()
    if destination.exists() and not destination.is_dir():
        raise ValueError(f'Destination is not a directory: {destination}')
    pending = []
    unchanged = []
    conflicts = []
    for name, (_, source) in skills.items():
        target = destination / name
        if target.is_symlink() and target.resolve() == source:
            unchanged.append(name)
        elif target.exists() or target.is_symlink():
            conflicts.append(str(target))
        else:
            pending.append((source, target))
    if conflicts:
        raise ValueError('Existing destinations would be overwritten; nothing changed:\n' + '\n'.join(conflicts))
    if dry_run:
        for source, target in pending:
            print(f'Would link {target} -> {source}')
    elif pending:
        destination.mkdir(parents=True, exist_ok=True)
        created = []
        try:
            for source, target in pending:
                target.symlink_to(source, target_is_directory=True)
                created.append((source, target))
        except OSError:
            for source, target in reversed(created):
                if target.is_symlink() and target.resolve() == source:
                    target.unlink()
            raise
    action = 'planned' if dry_run else 'installed'
    print(f'{len(pending)} {action}; {len(unchanged)} already linked.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', choices=AGENT_SKILL_PATHS, default='codex',
                        help='Agent whose personal skills directory to use (default: codex)')
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument('--collection', choices=['paper-writing', 'implementation-and-artifacts', 'all'])
    selection.add_argument('--skill', help='Install one skill by name')
    parser.add_argument('--destination', type=Path,
                        help='Explicit discovery directory; overrides the --agent destination')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        skills = load_skills(ROOT)
        if args.skill:
            if args.skill not in skills:
                raise ValueError(f'Unknown skill: {args.skill}')
            skills = {args.skill: skills[args.skill]}
        else:
            collection = args.collection or 'paper-writing'
            skills = {name: entry for name, entry in skills.items()
                      if collection == 'all' or entry[0] == collection}
        destination = args.destination or Path.home().joinpath(*AGENT_SKILL_PATHS[args.agent])
        install(skills, destination, args.dry_run)
    except (OSError, ValueError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
