# Maintenance

[Introduction and installation](../README.md)

```text
README.md                         Introduction and quick installation
LICENSE                           MIT license and copyright notice
CITATION.cff                      Optional academic citation metadata
docs/skills.md                    Skill catalog and selection guide
docs/installation.md              Agent compatibility and installation options
docs/maintenance.md               Repository layout and validation
paper-writing/                    Seven paper-writing skills
implementation-and-artifacts/     Four implementation and artifact skills
collections.json                  Collection membership
scripts/install.py                Selective installation for Codex or Claude Code
tests/test_install.py              Isolated installer regression tests
```

Each skill retains its `SKILL.md`, selectively loaded `references/`, and optional `agents/openai.yaml`. The collection folders are navigation and installation groups, not additional catch-all skills. Installation defaults to Paper Writing when no collection is specified.

Run the installer tests with:

```sh
python3 -m unittest discover -s tests -v
```

The tests isolate both personal directories in temporary homes and check selection, shared targets, repeated installation, dry-run, and conflict protection. They validate installation behavior; actual skill discovery and response quality should also be checked in each agent.

Keep technical requirements distinct from editorial preferences. A preferred proof organization or label style can be adapted to the author and venue while preserving the governing definition and proof obligations. Proof validity, functional testing, analytical costs, empirical performance and publication readiness remain distinct conclusions.

Changes should preserve the selected skill's scope, keep its references self-contained, and check both collection-only and individual use. Test representative behavior when routing or substantive instructions change. Private conversation exports, local provenance reports and backups are not part of this source collection.
