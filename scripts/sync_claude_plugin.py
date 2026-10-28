#!/usr/bin/env python3
"""Generate Claude Code manifests from the release metadata and skill catalog.

The checkout is the Claude plugin root; its existing collections are scanned
directly. This does not change the separately built OpenAI submission archive.
"""

import argparse
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = ('research', 'writing', 'implementation')
MARKETPLACE = 'cryptography-research-skills'
IDENTITY_FIELDS = ('name', 'version', 'description', 'author', 'homepage',
                   'repository', 'license', 'keywords')
SLUG = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')


def read_json(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError(f'Missing or indirect JSON file: {path}')
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as error:
        raise ValueError(f'Invalid JSON in {path}: {error.msg}') from error


def require_string(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label} must be a nonempty string')


def expected_manifests(root=ROOT):
    root = Path(root)
    if (root / 'submission').is_symlink():
        raise ValueError('The submission directory must not be a symlink')
    source = read_json(root / 'submission' / 'plugin.json')
    if not isinstance(source, dict):
        raise ValueError('Release manifest must be an object')
    for field in ('name', 'version', 'description'):
        require_string(source.get(field), field)
    if not SLUG.fullmatch(source['name']):
        raise ValueError('Plugin name must be kebab-case')
    author = source.get('author')
    if not isinstance(author, dict):
        raise ValueError('author must be an object')
    require_string(author.get('name'), 'author.name')
    for field in ('email', 'url'):
        if field in author:
            require_string(author[field], f'author.{field}')

    catalog = read_json(root / 'collections.json')
    if not isinstance(catalog, dict) or set(catalog) != set(COLLECTIONS):
        raise ValueError('Catalog must contain research, writing, and implementation')
    seen = set()
    for collection in COLLECTIONS:
        directory = root / collection
        if directory.is_symlink() or not directory.is_dir():
            raise ValueError(f'Missing or indirect collection: {collection}')
        names = catalog[collection]
        if not isinstance(names, list) or not names:
            raise ValueError(f'Invalid collection: {collection}')
        for name in names:
            if not isinstance(name, str) or not SLUG.fullmatch(name):
                raise ValueError(f'Invalid skill name: {name!r}')
            if name in seen:
                raise ValueError(f'Duplicate skill name: {name}')
            seen.add(name)
            skill = directory / name
            entry = skill / 'SKILL.md'
            if skill.is_symlink() or entry.is_symlink() or not entry.is_file():
                raise ValueError(f'Missing or indirect skill: {collection}/{name}')
        # Claude scans each collection, so an uncatalogued SKILL.md would also
        # become available even though the other release paths omit it.
        for child in directory.iterdir():
            if child.is_symlink():
                raise ValueError(f'Indirect collection entry: {child}')
            if child.is_dir():
                entry = child / 'SKILL.md'
                if entry.is_symlink():
                    raise ValueError(f'Indirect skill entry: {entry}')
                if entry.is_file() and child.name not in names:
                    raise ValueError(f'Uncatalogued skill: {collection}/{child.name}')

    # A conventional skills/ folder would be scanned as well as our custom
    # paths, potentially exposing duplicates or unreviewed extra skills.
    if (root / 'skills').is_symlink() or (root / 'skills').exists():
        raise ValueError('Unexpected root skills/ directory; use the catalogued collections')

    plugin = {key: source[key] for key in IDENTITY_FIELDS if key in source}
    plugin['skills'] = [f'./{collection}/' for collection in COLLECTIONS]
    marketplace = {
        'name': MARKETPLACE,
        'description': source['description'],
        'owner': {key: author[key] for key in ('name', 'email') if key in author},
        'plugins': [{
            'name': source['name'],
            'source': './',
            'description': source['description'],
        }],
    }
    return {'plugin.json': plugin, 'marketplace.json': marketplace}


def sync(root=ROOT, check=False):
    root = Path(root)
    manifests = expected_manifests(root)
    directory = root / '.claude-plugin'
    if directory.is_symlink():
        raise ValueError('The .claude-plugin directory must not be a symlink')
    encoded = {name: json.dumps(value, indent=2, ensure_ascii=False) + '\n'
               for name, value in manifests.items()}
    for name in encoded:
        path = directory / name
        if path.is_symlink() or (path.exists() and not path.is_file()):
            raise ValueError(f'Indirect or non-file manifest: {path}')
    if check:
        for name, content in encoded.items():
            path = directory / name
            read_json(path)
            if path.read_text(encoding='utf-8') != content:
                raise ValueError(f'Stale Claude manifest: {path}; run scripts/sync_claude_plugin.py')
    else:
        directory.mkdir(exist_ok=True)
        for name, content in encoded.items():
            (directory / name).write_text(content, encoding='utf-8')
    return manifests


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check generated manifests without writing')
    args = parser.parse_args()
    try:
        sync(check=args.check)
    except (OSError, ValueError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 1
    print('Claude manifests are current.' if args.check else 'Updated .claude-plugin manifests.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
