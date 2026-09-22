# Installation details

See the [README](../README.md#installation) for the basic Codex and Claude Code installation commands. Run the examples below from the repository root.

## How Codex and Claude Code use the same skills

Both tools read the shared `SKILL.md` files and their skill-local `references/`. The YAML `name` and `description` identify each skill; the Markdown body contains its research workflow. The installer links each selected skill into the chosen tool's personal skills directory, so both installations use one source copy in this checkout.

| Tool | Personal installation directory | Explicit invocation example |
| --- | --- | --- |
| Codex | `~/.agents/skills/<skill-name>/` | `$crypto-proof-auditor` |
| Claude Code | `~/.claude/skills/<skill-name>/` | `/crypto-proof-auditor` |

Both tools can select a skill from its description when the request matches. Codex's optional `agents/openai.yaml` files supply its display names and suggested prompts; the shared workflow does not depend on those files. Claude Code uses `SKILL.md` for these standalone skills. The collection directory names organize this repository; each installed skill is linked directly below the tool's skills directory.

See the official [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code skill documentation](https://code.claude.com/docs/en/skills) for discovery, invocation, and symlink support. This installer targets local personal skills. Claude account uploads, cloud sessions, and plugin-manager distribution use separate installation mechanisms.

## Both tools and other selections

To use the same Research collection in both tools, run both installation commands in the [README](../README.md#installation). Each tool's links point to the same source folders. Installing for Claude Code leaves the Codex links intact.

For either agent, select `research`, `writing`, `implementation`, all twelve skills, or one individual skill. The default collection is Research. These examples use Claude Code; replace `claude` with `codex` for Codex:

```sh
python3 scripts/install.py --agent claude --collection writing
python3 scripts/install.py --agent claude --collection implementation
python3 scripts/install.py --agent claude --collection all
python3 scripts/install.py --agent claude --skill crypto-proof-auditor
```

Preview an installation without creating files:

```sh
python3 scripts/install.py --agent claude --collection all --dry-run
```

An explicit `--destination` overrides the agent's personal directory. For example, install Research into a particular research project's Claude Code skills directory:

```sh
python3 scripts/install.py --agent claude --collection research \
  --destination /path/to/research-project/.claude/skills
```

The earlier `--destination "$HOME/.claude/skills"` form also works without `--agent`. An arbitrary destination only makes skills available if the agent discovers that directory.

The installer refuses to overwrite an existing directory, file, or unrelated link, including an unrelated broken link. It checks all selected destinations before creating or migrating links, and repeating a successful installation leaves matching links intact. Resolve a reported conflict by reviewing the existing installation before moving or removing it. Selecting a smaller collection later adds any missing selected skills; it does not uninstall skills already present.

## Migrating from the two-collection layout

The source folders moved from `paper-writing/` and `implementation-and-artifacts/` into the three collections. Rerun the installer for the skills you already use; it recognizes links to this checkout's exact former path for the same skill and retargets them. Other links and copied installations remain protected. `--dry-run` previews migrations without changing links.

The former `--collection paper-writing` and `--collection implementation-and-artifacts` selections remain compatibility options with their original eight and four skills, respectively. They are not aliases for only the new Writing and Implementation collections: proof auditing now belongs to Research, and evaluation writing belongs to Writing. New commands should use the three current names. The no-argument default is now Research.

Keep the checkout at a stable path while its links are installed. Updating this checkout updates the files used by both tools; start a fresh session to pick up changed skills. If you prefer copied installations, copy individual skill folders intact with their references and update those copies yourself. When copying or redistributing an individual skill, include a copy of the repository-root [LICENSE](../LICENSE) with the skill. Companion skills are optional, and no skill requires a file from another skill folder.
