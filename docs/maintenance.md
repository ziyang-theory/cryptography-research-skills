# Maintenance

[Introduction and installation](../README.md)

```text
README.md                         Introduction and quick installation
LICENSE                           MIT license and copyright notice
CITATION.cff                      Optional academic citation metadata
docs/skills.md                    Skill catalog and selection guide
docs/installation.md              Agent compatibility and installation options
docs/maintenance.md               Repository layout and validation
paper-writing/                    Eight research-framing and paper-writing skills
implementation-and-artifacts/     Four implementation and artifact skills
collections.json                  Collection membership
scripts/install.py                Selective installation for Codex or Claude Code
tests/test_install.py              Isolated installer regression tests
```

Each skill has a self-contained `SKILL.md`, optional task-specific `references/`, and optional `agents/openai.yaml`. The two collections are installation groups, not additional skills. Installation defaults to Paper Writing.

## Keep the collection small

Organize by the requested deliverable, as in the [catalog](skills.md). The common thread is a claim, its supporting evidence, and the scope of the conclusion. Keep proof validity, protocol correspondence, measurements, and publication checks distinct.

- Put the minimal usable workflow in `SKILL.md`. Load references for a concrete uncertainty or task mode, not for every invocation.
- Give each rule one home within a skill. Keep only essential safeguards in the entrypoint; do not repeat the same checklist in its references.
- Add a reference only for substantial reusable detail. A new example normally belongs in an existing reference, and a past failure does not automatically justify a universal rule.
- Keep paper-specific examples and source notes optional. Preserve their versions and verification limits; do not turn examples into defaults for other constructions.
- Recommend another skill only for a separate part of the user's task. An individual installation must remain usable without sibling folders or a shared mandatory guide.
- Match effort to scope: a sentence edit needs no full research ledger, and a preferred proof style is not a validity condition. For new simulation proofs, prefer a simulator followed by meaningful hybrids; preserve direct arguments and existing organization when appropriate.

Change existing guidance before adding a new skill. A new skill needs a distinct deliverable and a trigger that does not compete with an existing one. Keep generic agent instructions, private conversation exports, local provenance reports, and backups out of this collection.

## Validate changes

Run the installer tests with:

```sh
python3 -m unittest discover -s tests -v
```

The tests isolate personal directories in temporary homes and check selection, shared targets, repeated installation, dry-run, and conflict protection. Also validate changed skill frontmatter, UI metadata, and local links, including whether every reference is reachable and each skill works when copied alone. Run `git diff --check` and inspect the diff against the working state that preceded the edit.

For substantive routing or workflow changes, try representative requests with an independent reviewer. Include a narrow task that should stay narrow and a technical case whose safeguards must survive. These checks provide behavioral evidence, not proof of response quality across all tasks.
