#!/usr/bin/env python3
"""Validate and reproducibly package the catalogued skills for plugin submission.

This is a local packaging check, not OpenAI's validator or a behavioral evaluation.
Only catalogued skill trees and the explicit release inputs below enter the ZIP.
"""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import sys
import tempfile
from urllib.parse import unquote, urlsplit
import zipfile


ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = {'research', 'writing', 'implementation'}
NAME = 'crypto-research-skills'
MANIFEST_SCHEMA = 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
FIXED_TIME = (2020, 1, 1, 0, 0, 0)
MAX_ARCHIVE_BYTES = 100_000_000
MAX_EXTRACTED_BYTES = 512 * 1024 * 1024
MAX_ENTRIES = 5000
MAX_DEPTH = 20
MAX_QUALIFIED_SKILL_NAME = 64
SLUG = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
SEMVER = re.compile(
    r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)'
    r'(?:-((?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)'
    r'(?:\.(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*))?'
    r'(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?\Z'
)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + '\n').encode('utf-8')


def read_regular(path, root):
    """Reject indirect inputs, including symlinked parent directories."""
    relative = path.relative_to(root)
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f'Symlink inputs are not permitted: {current}')
    if not path.is_file() or not stat.S_ISREG(path.stat().st_mode):
        raise ValueError(f'Missing or non-regular input: {path}')
    return path.read_bytes()


def tree_files(directory, root, exclude_caches=True):
    if directory.is_symlink() or not directory.is_dir():
        raise ValueError(f'Missing or indirect directory: {directory}')
    for path in sorted(directory.iterdir()):
        if path.is_symlink():
            raise ValueError(f'Symlink inputs are not permitted: {path}')
        if exclude_caches and (path.name in {'.DS_Store', '__pycache__'} or path.suffix in {'.pyc', '.pyo'}):
            continue
        if path.is_dir():
            yield from tree_files(path, root, exclude_caches)
        else:
            yield path, read_regular(path, root)


def load_catalog(root):
    catalog = json.loads(read_regular(root / 'collections.json', root))
    if not isinstance(catalog, dict) or set(catalog) != COLLECTIONS:
        raise ValueError('The catalog must contain exactly research, writing, and implementation')
    skills = {}
    for collection, names in sorted(catalog.items()):
        collection_path = root / collection
        if collection_path.is_symlink() or not collection_path.is_dir():
            raise ValueError(f'Missing or indirect collection: {collection}')
        if not isinstance(names, list) or not names:
            raise ValueError(f'Invalid collection: {collection}')
        for name in names:
            if not isinstance(name, str) or not SLUG.fullmatch(name):
                raise ValueError(f'Invalid skill name: {name!r}')
            qualified = f'{NAME}:{name}'
            if len(qualified) > MAX_QUALIFIED_SKILL_NAME:
                raise ValueError(
                    f'Combined plugin-name:skill-name exceeds {MAX_QUALIFIED_SKILL_NAME} '
                    f'characters ({len(qualified)}): {qualified}'
                )
            if name in skills:
                raise ValueError(f'Duplicate skill name: {name}')
            source = collection_path / name
            read_regular(source / 'SKILL.md', root)
            skills[name] = (collection, source)
    return skills


def local_reference(target, source, files, boundary=None):
    """Check local file existence and containment; external URLs are not fetched."""
    target = target.strip()
    if target.startswith('<') and target.endswith('>'):
        target = target[1:-1]
    parsed = urlsplit(target)
    if parsed.scheme == 'file' or target.startswith('~/'):
        raise ValueError(f'Non-portable reference in {source}: {target}')
    if parsed.scheme or parsed.netloc or not parsed.path:
        return
    path = unquote(parsed.path)
    if path.startswith('/') or '\\' in path:
        raise ValueError(f'Non-portable reference in {source}: {target}')
    parts = list(PurePosixPath(source).parent.parts)
    for part in PurePosixPath(path).parts:
        if part == '..':
            if not parts:
                raise ValueError(f'Reference escapes package in {source}: {target}')
            parts.pop()
        elif part != '.':
            parts.append(part)
    destination = PurePosixPath(*parts).as_posix()
    if boundary and not (destination == boundary or destination.startswith(boundary + '/')):
        raise ValueError(f'Reference escapes skill in {source}: {target}')
    if destination not in files and not any(name.startswith(destination + '/') for name in files):
        raise ValueError(f'Missing local reference in {source}: {target}')


def validate_references(files):
    for name, data in files.items():
        if not name.startswith('skills/'):
            continue
        boundary = '/'.join(PurePosixPath(name).parts[:2])
        if name.endswith('.md'):
            # This deliberately supports the repository's inline/reference-style
            # Markdown links, not arbitrary Markdown extensions or code examples.
            text = re.sub(r'(?ms)^\s*(```|~~~).*?^\s*\1\s*$', '', data.decode('utf-8'))
            text = re.sub(r'`+[^`]*`+', '', text)
            targets = re.findall(r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)', text)
            targets += re.findall(r'(?m)^\s*\[[^\]\n]+\]:\s*(<[^>]+>|\S+)', text)
            for target in targets:
                local_reference(target, name, files, boundary)
        elif name.endswith(('.yaml', '.yml')):
            # Asset paths in agents/openai.yaml resolve from the skill root.
            # These scalar fields are the only YAML paths used by skill UIs.
            text = data.decode('utf-8')
            for match in re.finditer(r'(?m)^\s*(?:icon_small|icon_large):\s*(.+?)\s*$', text):
                target = match.group(1).strip('"\'')
                local_reference(target, boundary + '/SKILL.md', files, boundary)


def require_string(value, label, maximum=None):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label} must be a nonempty string')
    if maximum and len(value) > maximum:
        raise ValueError(f'{label} exceeds {maximum} characters')


def validate_manifest(manifest, files):
    if not isinstance(manifest, dict) or manifest.get('name') != NAME:
        raise ValueError(f'Plugin name must be {NAME}')
    if manifest.get('$schema') != MANIFEST_SCHEMA:
        raise ValueError(f'Portable manifest $schema must be {MANIFEST_SCHEMA}')
    if not isinstance(manifest.get('version'), str) or not SEMVER.fullmatch(manifest['version']):
        raise ValueError('Plugin version must be a semantic version')
    require_string(manifest.get('description'), 'description')
    author = manifest.get('author')
    if not isinstance(author, dict):
        raise ValueError('author must identify the publisher using an object')
    require_string(author.get('name'), 'author.name')
    extensions = manifest.get('extensions', {})
    if not isinstance(extensions, dict) or not isinstance(extensions.get('com.openai', {}), dict):
        raise ValueError('extensions.com.openai must be an object')
    overlay = extensions.get('com.openai', {})
    for scope, metadata in (('portable manifest', manifest), ('OpenAI overlay', overlay)):
        for key in ('apps', 'mcpServers', 'hooks', 'commands', 'agents'):
            if key in metadata:
                raise ValueError(f'{scope}.{key} is outside this skills-only package')
        if 'skills' in metadata and metadata['skills'] != './skills/':
            raise ValueError(f'{scope}.skills must use the packaged ./skills/ directory')
    interface = overlay.get('interface', {})
    if not isinstance(interface, dict):
        raise ValueError('extensions.com.openai.interface must be an object')
    for key, maximum in [('displayName', 30), ('shortDescription', 30), ('longDescription', 4000)]:
        require_string(interface.get(key), f'interface.{key}', maximum)
    require_string(interface.get('developerName'), 'interface.developerName')
    if interface['developerName'] != author['name']:
        raise ValueError('interface.developerName must agree with author.name')
    if 'screenshots' in interface:
        raise ValueError('interface.screenshots is outside this skills-only package')
    prompts = interface.get('defaultPrompt', [])
    if isinstance(prompts, str):
        prompts = [prompts]
    if not isinstance(prompts, list) or not prompts:
        raise ValueError('interface.defaultPrompt must contain at least one starter prompt')
    if len(prompts) > 3:
        raise ValueError('interface.defaultPrompt must contain at most 3 starter prompts')
    for prompt in prompts:
        require_string(prompt, 'interface.defaultPrompt', 128)
    if len(set(prompt.strip() for prompt in prompts)) != len(prompts):
        raise ValueError('interface.defaultPrompt must not contain duplicate starter prompts')
    for key in ('composerIcon', 'logo'):
        require_string(interface.get(key), f'interface.{key}')
        local_reference(interface[key], 'plugin.json', files)
    return overlay


def collect_package(root):
    root = root.absolute()
    skills = load_catalog(root)
    files = {}
    for name, (_, directory) in sorted(skills.items()):
        for source, data in tree_files(directory, root):
            destination = f'skills/{name}/{source.relative_to(directory).as_posix()}'
            files[destination] = data
        skill_text = files[f'skills/{name}/SKILL.md'].decode('utf-8')
        frontmatter = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', skill_text, re.DOTALL)
        if not frontmatter:
            raise ValueError(f'Missing SKILL.md frontmatter: {name}')
        found_name = re.search(r'(?m)^name:\s*["\']?([^\s"\']+)["\']?\s*$', frontmatter.group(1))
        if not found_name or found_name.group(1) != name:
            raise ValueError(f'SKILL.md name differs from catalog: {name}')
        if not re.search(r'(?m)^description:\s*\S', frontmatter.group(1)):
            raise ValueError(f'Missing skill description: {name}')
    for name in ('LICENSE', 'CITATION.cff'):
        files[name] = read_regular(root / name, root)
    files['README.md'] = read_regular(root / 'submission' / 'PLUGIN_README.md', root)
    for source, data in tree_files(root / 'submission' / 'assets', root):
        files[f'assets/{source.relative_to(root / "submission" / "assets").as_posix()}'] = data
    files['plugin.json'] = read_regular(root / 'submission' / 'plugin.json', root)
    manifest = json.loads(files['plugin.json'])
    overlay = validate_manifest(manifest, files)
    # Keep only portable fields supported by the legacy Codex manifest, then
    # apply its OpenAI-specific overlay. Portable identity cannot be overridden.
    identity_fields = ('name', 'version', 'description', 'author', 'homepage', 'repository', 'license', 'keywords')
    legacy = {key: manifest[key] for key in identity_fields if key in manifest}
    for key in identity_fields:
        if key in overlay and overlay[key] != legacy.get(key):
            raise ValueError(f'OpenAI overlay changes portable identity: {key}')
    legacy.update(overlay)
    legacy['skills'] = './skills/'
    files['.codex-plugin/plugin.json'] = json_bytes(legacy)
    validate_references(files)
    if len(files) > MAX_ENTRIES:
        raise ValueError(f'Package exceeds {MAX_ENTRIES} file entries')
    if sum(map(len, files.values())) > MAX_EXTRACTED_BYTES:
        raise ValueError('Package exceeds 512 MiB extracted')
    if any(len(PurePosixPath(NAME, name).parts) > MAX_DEPTH for name in files):
        raise ValueError(f'Package exceeds {MAX_DEPTH} path components')
    return manifest, skills, dict(sorted(files.items()))


def check_owned_stage(stage, inventory_path):
    """Never replace an unrecognized or locally modified output directory."""
    if stage.is_symlink():
        raise ValueError(f'Refusing to replace symlink output: {stage}')
    if not stage.exists():
        return
    if inventory_path.is_symlink() or not inventory_path.is_file():
        raise ValueError(f'Existing stage has no build inventory: {stage}')
    previous = json.loads(inventory_path.read_text(encoding='utf-8'))
    if previous.get('schema') != 1 or previous.get('plugin') != NAME:
        raise ValueError(f'Existing stage has an unrecognized build inventory: {stage}')
    expected = {entry['path']: entry['sha256'] for entry in previous['files']}
    actual = {path.relative_to(stage).as_posix(): sha256(data)
              for path, data in tree_files(stage, stage, exclude_caches=False)}
    if actual != expected:
        raise ValueError(f'Existing stage contains modified or additional files: {stage}')


def build(root=ROOT, output_dir=None, check=False):
    root = Path(root).absolute()
    manifest, skills, files = collect_package(root)
    if check:
        return {'plugin': NAME, 'version': manifest['version'], 'skills': len(skills), 'files': len(files)}
    output_dir = Path(output_dir or root / 'dist').absolute()
    if output_dir.is_symlink():
        raise ValueError(f'Symlink output directory is not permitted: {output_dir}')
    for protected in [root / 'submission', *(source for _, source in skills.values())]:
        if output_dir.resolve().is_relative_to(protected.resolve()):
            raise ValueError(f'Output directory is inside release inputs: {output_dir}')
    output_dir.mkdir(parents=True, exist_ok=True)
    stage = output_dir / NAME
    inventory_path = output_dir / f'{NAME}-build.json'
    check_owned_stage(stage, inventory_path)
    archive_name = f'{NAME}-{manifest["version"]}.zip'
    archive = output_dir / archive_name
    for output in (archive, inventory_path, output_dir / 'SHA256SUMS'):
        if output.is_symlink():
            raise ValueError(f'Symlink output is not permitted: {output}')
    with tempfile.TemporaryDirectory(prefix='.plugin-build-', dir=output_dir) as temporary:
        temporary = Path(temporary)
        staged = temporary / NAME
        staged.mkdir()
        for name, data in files.items():
            target = staged / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            target.chmod(0o644)
        temporary_archive = temporary / archive_name
        with zipfile.ZipFile(temporary_archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
            for name, data in files.items():
                info = zipfile.ZipInfo(f'{NAME}/{name}', FIXED_TIME)
                info.create_system = 3
                info.external_attr = (stat.S_IFREG | 0o644) << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                bundle.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        if temporary_archive.stat().st_size > MAX_ARCHIVE_BYTES:
            raise ValueError('Compressed plugin exceeds 100 MB')
        digest = sha256(temporary_archive.read_bytes())
        inventory = {
            'schema': 1, 'plugin': NAME, 'version': manifest['version'],
            'archive': archive_name, 'archive_sha256': digest,
            'archive_bytes': temporary_archive.stat().st_size,
            'extracted_bytes': sum(map(len, files.values())),
            'skills': {name: f'{collection}/{name}' for name, (collection, _) in sorted(skills.items())},
            'files': [{'path': name, 'bytes': len(data), 'sha256': sha256(data)} for name, data in files.items()],
        }
        if stage.exists():
            shutil.rmtree(stage)
        staged.replace(stage)
        temporary_archive.replace(archive)
        inventory_path.write_bytes(json_bytes(inventory))
        (output_dir / 'SHA256SUMS').write_text(f'{digest}  {archive_name}\n', encoding='utf-8')
    return {'archive': str(archive), 'sha256': digest, 'skills': len(skills), 'files': len(files)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, help='Generated outputs directory (default: dist/)')
    parser.add_argument('--check', action='store_true', help='Validate release inputs without writing outputs')
    args = parser.parse_args()
    try:
        result = build(output_dir=args.output_dir, check=args.check)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
