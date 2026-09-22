#!/usr/bin/env python3
"""Install shared skills for Codex or Claude Code using directory symlinks."""

import argparse
import json
import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENT_SKILL_PATHS = {
    'codex': ('.agents', 'skills'),
    'claude': ('.claude', 'skills'),
}
COLLECTIONS = ('research', 'writing', 'implementation')
# Keep explicit legacy selections stable while their source directories move.
LEGACY_COLLECTIONS = {
    'paper-writing': (
        'crypto-research-framing', 'cryptography-writing',
        'crypto-literature-evidence', 'crypto-proof-auditor',
        'crypto-prior-work-comparison', 'crypto-correlation-accounting',
        'crypto-manuscript-qa', 'crypto-ai-acknowledgements',
    ),
    'implementation-and-artifacts': (
        'crypto-protocol-implementation', 'crypto-benchmarking',
        'crypto-implementation-evaluation-writing', 'crypto-research-artifacts',
    ),
}


def load_skills(root):
    catalog = json.loads((root / 'collections.json').read_text(encoding='utf-8'))
    if set(catalog) != set(COLLECTIONS):
        raise ValueError('The catalog must contain research, writing, and implementation')
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


def previous_source_link(target, name, root):
    """Recognize only this checkout's old source path for the same skill."""
    if not target.is_symlink():
        return None
    previous = os.readlink(target)
    linked_path = Path(previous)
    if not linked_path.is_absolute():
        linked_path = target.parent / linked_path
    # Follow intermediate symlinks before interpreting '..'; lexical normalization
    # can otherwise mistake an unrelated target for this checkout's former source.
    linked_path = linked_path.resolve()
    for collection, names in LEGACY_COLLECTIONS.items():
        if name in names and linked_path == root.resolve() / collection / name:
            return previous
    return None


def install(skills, destination, dry_run=False, root=ROOT):
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
        elif (previous := previous_source_link(target, name, root)) is not None:
            pending.append((source, target, previous))
        elif target.exists() or target.is_symlink():
            conflicts.append(str(target))
        else:
            pending.append((source, target, None))
    if conflicts:
        raise ValueError('Existing destinations would be overwritten; nothing changed:\n' + '\n'.join(conflicts))
    if dry_run:
        for source, target, previous in pending:
            action = 'retarget' if previous is not None else 'link'
            print(f'Would {action} {target} -> {source}')
    elif pending:
        destination.mkdir(parents=True, exist_ok=True)
        changed = []
        try:
            for source, target, previous in pending:
                if previous is not None:
                    if not target.is_symlink() or os.readlink(target) != previous:
                        raise ValueError(f'Destination changed during installation: {target}')
                    target.unlink()
                    # Record the removal before creation so a failed retarget restores it.
                    changed.append((source, target, previous))
                target.symlink_to(source, target_is_directory=True)
                if previous is None:
                    changed.append((source, target, None))
        except (OSError, ValueError):
            for source, target, previous in reversed(changed):
                if target.is_symlink() and os.readlink(target) == str(source):
                    target.unlink()
                if previous is not None and not target.exists() and not target.is_symlink():
                    target.symlink_to(previous, target_is_directory=True)
            raise
    action = 'planned' if dry_run else 'installed'
    print(f'{len(pending)} {action}; {len(unchanged)} already linked.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', choices=AGENT_SKILL_PATHS, default='codex',
                        help='Agent whose personal skills directory to use (default: codex)')
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument(
        '--collection', choices=[*COLLECTIONS, 'all', *LEGACY_COLLECTIONS],
        help='Collection to install (default: research); old collection names are deprecated '
             'but retain their original memberships',
    )
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
            collection = args.collection or 'research'
            if collection in LEGACY_COLLECTIONS:
                print(f'Warning: --collection {collection} is deprecated; '
                      'installing its original skill selection.', file=sys.stderr)
                skills = {name: skills[name] for name in LEGACY_COLLECTIONS[collection]}
            else:
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
