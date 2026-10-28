# Publishing for Claude

This repository is both a Claude Code plugin and a one-plugin marketplace. The plugin uses the twelve existing skills in `research/`, `writing/`, and `implementation/`; there is no second copy to maintain.

## Release metadata

- Repository: `ziyang-theory/cryptography-research-skills`.
- Marketplace: `cryptography-research-skills`.
- Plugin: `crypto-research-skills`.
- Plugin path: repository root.
- Source branch: `main`.
- Manifest: [`.claude-plugin/plugin.json`](../.claude-plugin/plugin.json).
- Marketplace: [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json).

The Claude manifest derives its identity and version from [the portable manifest](../submission/plugin.json). Its custom `skills` paths point to the three collections. Optional `agents/openai.yaml` files remain for Codex; the shared instructions do not depend on them. Claude metadata is outside the existing OpenAI ZIP build, so adding it does not change an already-submitted archive.

## Validate and publish the marketplace

From the repository root:

```sh
python3 scripts/sync_claude_plugin.py
python3 scripts/sync_claude_plugin.py --check
python3 scripts/build_plugin.py --check
python3 -m unittest discover -s tests -v
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
git diff --check
```

The Python packaging checks require `requirements-dev.txt`. The sync command uses only the Python standard library. Its check mode rejects stale metadata and skills that are missing from or additional to the catalog. Claude's validator checks host-specific manifest rules; neither validator establishes model behavior or directory approval.

Test installation from a local marketplace before pushing:

```sh
claude plugin marketplace add /absolute/path/to/cryptography-research-skills
claude plugin install crypto-research-skills@cryptography-research-skills
claude plugin list
```

In a fresh session, check that `/crypto-research-skills:crypto-proof-auditor` and the other catalog skills are available. After the validated files are pushed to `main`, the public installation commands in the [README](../README.md#claude-code) work. Increment the plugin version for subsequent releases; an unchanged version can keep installed copies from updating.

## Anthropic directory submission

Directory listing is separate from publishing this GitHub marketplace. As checked on October 27, 2026, the [developer portal](https://claude.ai/directory/manage) accepts a GitHub repository through **Submit new → Plugin bundle**. The submitting account needs an eligible paid plan and a connected GitHub account with push access. Publishing the marketplace does not establish directory submission or approval.

Use these source fields:

| Field | Value |
| --- | --- |
| Repository | `https://github.com/ziyang-theory/cryptography-research-skills` |
| Plugin path | Leave empty (repository root) |
| Branch or tag | `main` |
| Contact | `ziyang@cs.toronto.edu` |

Run the portal's validation against the published commit, fix any blocking findings, and review the listing it derives from the manifest and README. Complete its data-handling questions and compliance acknowledgements against their actual wording, then submit for review. Record the submission URL, validated commit, and observed status. A passing validation is not publication.

For data-handling answers, the package itself has no server, telemetry, authentication, storage service, or publisher-operated endpoint. The host may process user-supplied manuscripts, code, measurements, and other files, and may use browsing or external tools when requested. This is not a claim that the host never processes personal data. The [package README](../submission/PLUGIN_README.md#scope-and-tools) documents these boundaries. Audience statements and legal acknowledgements belong to the publisher and must reflect the live form.

Anthropic's current documentation distinguishes its directory from `claude-plugins-official`; directory submission does not itself put the plugin in that marketplace. Eligible directory installs can sync to Claude Code.

## Initial validation record

On October 27, 2026, all 65 repository tests passed with PyYAML 6.0.3, the Claude metadata check passed, and `git diff --check` passed. An independent rebuild of the OpenAI `0.2.0` archive retained SHA-256 `ec6cabc6259dbe9f10cc2fd1cebd347dd635e942ae1092b27f5922122b28c53f` (12 skills, 85 files).

Claude Code was unavailable in the validation environment, and package-registry access failed, so its native validator, plugin installation, and model behavior have not been tested. The Anthropic portal required sign-in; no directory submission or approval was established by these local checks.

## Official references

Living documentation, checked October 27, 2026 (the pages do not state a publication date):

- [Plugin manifest reference](https://code.claude.com/docs/en/plugins-reference).
- [Create a marketplace](https://code.claude.com/docs/en/plugin-marketplaces).
- [Publish and distribute a plugin](https://code.claude.com/docs/en/plugins/publish).
- [Submit your plugin](https://claude.com/docs/plugins/submit).
- [Plugin pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist).
