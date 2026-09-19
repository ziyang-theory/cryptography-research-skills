# Cryptography Research Skills

Reusable agent skills for cryptography research, organized into two independently selectable collections.

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

## Local installation in Codex

From this checkout, install only Paper Writing:

```sh
python3 scripts/install.py --collection paper-writing
```

Install the optional implementation collection, or both collections:

```sh
python3 scripts/install.py --collection implementation-and-artifacts
python3 scripts/install.py --collection all
```

Preview the operation without creating files:

```sh
python3 scripts/install.py --collection all --dry-run
```

The installer uses Python 3's standard library and creates one symlink per selected skill in `~/.agents/skills`. It keeps the grouped checkout as the source of truth, retains skill names and invocation policies, and refuses to overwrite an existing directory or a different link. Existing correct links are left intact. All destination conflicts are checked before any links are created. Keep the checkout at a stable path while those links are installed.

Use `--skill crypto-proof-auditor` to install one skill, or `--destination /chosen/skills` to select a different discovery directory. Individual skill folders can also be copied intact, including their references, using the installation mechanism of the intended agent. Companion skills are optional and there are no required file links into another skill.

Codex documents support for [personal skills and symlinked skill folders](https://learn.chatgpt.com/docs/build-skills). Other agents' discovery paths and metadata support should be checked against their documentation.

## Organization and maintenance

```text
paper-writing/                    Seven paper-writing skills
implementation-and-artifacts/     Four implementation and artifact skills
collections.json                  Collection membership
scripts/install.py                Selective local installation
```

Each skill retains its `SKILL.md`, selectively loaded `references/`, and optional `agents/openai.yaml`. The collection folders are navigation and installation groups, not additional catch-all skills. Installation defaults to Paper Writing when no collection is specified.

Keep technical requirements distinct from editorial preferences. A preferred proof organization or label style can be adapted to the author and venue while preserving the governing definition and proof obligations. Proof validity, functional testing, analytical costs, empirical performance and publication readiness remain distinct conclusions.

Changes should preserve the selected skill's scope, keep its references self-contained, and check both collection-only and individual use. Test representative behavior when routing or substantive instructions change. Private conversation exports, local provenance reports and backups are not part of this source collection.
