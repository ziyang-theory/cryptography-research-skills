# Cryptography Research Skills

Reusable agent skills for cryptography research in **Codex and Claude Code**, organized into two independently selectable collections.

**Paper Writing** supports a theoretical project from literature and definitions through constructions, proofs, symbolic cost analysis, comparisons and manuscript preparation. It does not require an implementation, experiments or a software artifact.

**Implementation & Artifacts** is an optional companion for translating constructions into code, running and interpreting experiments, writing the evaluation, and preparing reproducible releases.

## Paper Writing

| Skill | Use |
| --- | --- |
| [cryptography-writing](paper-writing/cryptography-writing/SKILL.md) | Draft and edit prose, definitions, constructions, theorem statements and security arguments |
| [crypto-literature-evidence](paper-writing/crypto-literature-evidence/SKILL.md) | Establish what primary sources say, under which definitions, models and versions |
| [crypto-proof-auditor](paper-writing/crypto-proof-auditor/SKILL.md) | Review proofs, reductions, simulations and extraction arguments for concrete gaps |
| [crypto-prior-work-comparison](paper-writing/crypto-prior-work-comparison/SKILL.md) | Position contributions using supported, comparable claims |
| [crypto-correlation-accounting](paper-writing/crypto-correlation-accounting/SKILL.md) | Define algebraic correlations, party holdings, units and symbolic cost conversions |
| [crypto-manuscript-qa](paper-writing/crypto-manuscript-qa/SKILL.md) | Resolve live sources and check notation, references, LaTeX builds and rendered PDFs |
| [crypto-ai-acknowledgements](paper-writing/crypto-ai-acknowledgements/SKILL.md) | Describe AI contributions and human checks from the actual research process |

Correlation accounting belongs here because definitions and analytical costs matter even when no implementation exists. Its measurement guidance is conditional on a task involving measurements.

## Implementation & Artifacts

| Skill | Use |
| --- | --- |
| [crypto-protocol-implementation](implementation-and-artifacts/crypto-protocol-implementation/SKILL.md) | Implement or review protocol code against its specification, distributions and state machine |
| [crypto-benchmarking](implementation-and-artifacts/crypto-benchmarking/SKILL.md) | Design, run and interpret experiments with explicit timing, communication and statistical accounting |
| [crypto-implementation-evaluation-writing](implementation-and-artifacts/crypto-implementation-evaluation-writing/SKILL.md) | Turn implementation and experimental evidence into a supported evaluation section |
| [crypto-research-artifacts](implementation-and-artifacts/crypto-research-artifacts/SKILL.md) | Prepare reviewer workflows and validate reproducible research packages |

Evaluation writing belongs here because its methods depend on experimental design and interpretation. Skills can recommend companions from either collection when useful; a missing companion does not prevent the skill's own scoped task. Each skill has one source directory.

## Choose a collection or a skill

| Request | Start with |
| --- | --- |
| Find papers providing a particular functionality or security notion | `crypto-literature-evidence` |
| Audit this simulator and hybrid argument without editing the paper | `crypto-proof-auditor` |
| Compare correlation requirements and symbolic communication costs | `crypto-correlation-accounting`, then `crypto-prior-work-comparison` |
| Draft or improve the technical overview | `cryptography-writing` |
| Check whether protocol code matches the paper | `crypto-protocol-implementation` |
| Measure a prover or MPC protocol and interpret its performance | `crypto-benchmarking` |
| Write the implementation and evaluation section from supplied evidence | `crypto-implementation-evaluation-writing` |
| Prepare a reproducible reviewer artifact | `crypto-research-artifacts` |

The collection applies across MPC, zero knowledge and other cryptographic research. Construction-specific references are loaded only when relevant. Retained literature examples are primarily MPC-focused and carry their own source/verification qualifications; they do not establish comprehensive coverage of every subfield.

## How Codex and Claude Code use the same skills

Both tools read the shared `SKILL.md` files and their skill-local `references/`. The YAML `name` and `description` identify each skill; the Markdown body contains its research workflow. The installer links each selected skill into the chosen tool's personal skills directory, so both installations use one source copy in this checkout.

| Tool | Personal installation directory | Explicit invocation example |
| --- | --- | --- |
| Codex | `~/.agents/skills/<skill-name>/` | `$crypto-proof-auditor` |
| Claude Code | `~/.claude/skills/<skill-name>/` | `/crypto-proof-auditor` |

Both tools can select a skill from its description when the request matches. Codex's optional `agents/openai.yaml` files supply its display names and suggested prompts; the shared workflow does not depend on those files. Claude Code uses `SKILL.md` for these standalone skills. The collection directory names organize this repository; each installed skill is linked directly below the tool's skills directory.

See the official [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code skill documentation](https://code.claude.com/docs/en/skills) for discovery, invocation, and symlink support. This installer targets local personal skills. Claude account uploads, cloud sessions, and plugin-manager distribution use separate installation mechanisms.

## Installation

Clone this repository to a stable location, then run the commands from its root. The installer uses Python 3's standard library and requires permission to create directory symlinks. Install the agent you intend to use separately.

### Codex

Install Paper Writing for all your local Codex projects:

```sh
python3 scripts/install.py --agent codex --collection paper-writing
```

Omitting `--agent` preserves the original Codex default. Omitting `--collection` selects Paper Writing.

### Claude Code

Install Paper Writing for all your local Claude Code projects:

```sh
python3 scripts/install.py --agent claude --collection paper-writing
```

Start a fresh Claude Code session after the first installation and try:

```text
/crypto-proof-auditor Audit the security proof in this manuscript.
```

In Codex, use the corresponding `$crypto-proof-auditor` mention. You can also make a matching research request in either tool and allow it to select the relevant skill.

### Both tools and other selections

To use the same Paper Writing collection in both tools, run both installation commands above. Each tool's links point to the same source folders. Installing for Claude Code leaves the Codex links intact.

For either agent, select only the optional implementation collection, all eleven skills, or one individual skill. These examples use Claude Code; replace `claude` with `codex` for Codex:

```sh
python3 scripts/install.py --agent claude --collection implementation-and-artifacts
python3 scripts/install.py --agent claude --collection all
python3 scripts/install.py --agent claude --skill crypto-proof-auditor
```

Preview an installation without creating files:

```sh
python3 scripts/install.py --agent claude --collection all --dry-run
```

An explicit `--destination` overrides the agent's personal directory. For example, install Paper Writing into a particular research project's Claude Code skills directory:

```sh
python3 scripts/install.py --agent claude --collection paper-writing \
  --destination /path/to/research-project/.claude/skills
```

The earlier `--destination "$HOME/.claude/skills"` form also works without `--agent`. An arbitrary destination only makes skills available if the agent discovers that directory.

The installer refuses to overwrite an existing directory, file, or different link, including a broken link. It checks all selected destinations before creating links, and repeating a successful installation leaves matching links intact. Resolve a reported conflict by reviewing the existing installation before moving or removing it. Selecting a smaller collection later adds any missing selected skills; it does not uninstall skills already present.

Keep the checkout at a stable path while its links are installed. Updating this checkout updates the files used by both tools; start a fresh session to pick up changed skills. If you prefer copied installations, copy individual skill folders intact with their references and update those copies yourself. Companion skills are optional, and no skill requires a file from another skill folder.

## Organization and maintenance

```text
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
