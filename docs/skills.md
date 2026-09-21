# Skill catalog

[Introduction and installation](../README.md)

Reusable agent skills for cryptography research in **Codex and Claude Code**, organized into two independently selectable collections.

**Paper Writing** supports a theoretical project from literature and definitions through constructions, proofs, symbolic cost analysis, comparisons and manuscript preparation. It does not require an implementation, experiments or a software artifact.

**Implementation & Artifacts** is an optional companion for translating constructions into code, running and interpreting experiments, writing the evaluation, and preparing reproducible releases.

## Paper Writing

| Skill | Use |
| --- | --- |
| [cryptography-writing](../paper-writing/cryptography-writing/SKILL.md) | Draft and edit prose, definitions, constructions, theorem statements and security arguments |
| [crypto-literature-evidence](../paper-writing/crypto-literature-evidence/SKILL.md) | Establish what primary sources say, under which definitions, models and versions |
| [crypto-proof-auditor](../paper-writing/crypto-proof-auditor/SKILL.md) | Review proofs, reductions, simulations and extraction arguments for concrete gaps |
| [crypto-prior-work-comparison](../paper-writing/crypto-prior-work-comparison/SKILL.md) | Position contributions using supported, comparable claims |
| [crypto-correlation-accounting](../paper-writing/crypto-correlation-accounting/SKILL.md) | Define algebraic correlations, party holdings, units and symbolic cost conversions |
| [crypto-manuscript-qa](../paper-writing/crypto-manuscript-qa/SKILL.md) | Resolve live sources and check notation, references, LaTeX builds and rendered PDFs |
| [crypto-ai-acknowledgements](../paper-writing/crypto-ai-acknowledgements/SKILL.md) | Describe AI contributions and human checks from the actual research process |

Correlation accounting belongs here because definitions and analytical costs matter even when no implementation exists. Its measurement guidance is conditional on a task involving measurements.

## Implementation & Artifacts

| Skill | Use |
| --- | --- |
| [crypto-protocol-implementation](../implementation-and-artifacts/crypto-protocol-implementation/SKILL.md) | Implement, optimize or review protocol code against its specification and identify affected security contracts and proof obligations |
| [crypto-benchmarking](../implementation-and-artifacts/crypto-benchmarking/SKILL.md) | Design, run and interpret experiments with explicit timing, communication and statistical accounting |
| [crypto-implementation-evaluation-writing](../implementation-and-artifacts/crypto-implementation-evaluation-writing/SKILL.md) | Turn implementation and experimental evidence into a supported evaluation section |
| [crypto-research-artifacts](../implementation-and-artifacts/crypto-research-artifacts/SKILL.md) | Prepare reviewer workflows and validate reproducible research packages |

Evaluation writing belongs here because its methods depend on experimental design and interpretation. Skills can recommend companions from either collection when useful; a missing companion does not prevent the skill's own scoped task. Each skill has one source directory.

## Choose a collection or a skill

| Request | Start with |
| --- | --- |
| Find papers providing a particular functionality or security notion | `crypto-literature-evidence` |
| Audit this simulator and hybrid argument without editing the paper | `crypto-proof-auditor` |
| Compare correlation requirements and symbolic communication costs | `crypto-correlation-accounting`, then `crypto-prior-work-comparison` |
| Draft or improve the technical overview | `cryptography-writing` |
| Check whether protocol code matches the paper | `crypto-protocol-implementation` |
| Optimize protocol code and identify which security arguments need updating | `crypto-protocol-implementation` |
| Choose MPC or ZK optimization techniques for a measured bottleneck | `crypto-protocol-implementation`, then `crypto-benchmarking` for measurements |
| Measure a prover or MPC protocol and interpret its performance | `crypto-benchmarking` |
| Write the implementation and evaluation section from supplied evidence | `crypto-implementation-evaluation-writing` |
| Prepare a reproducible reviewer artifact | `crypto-research-artifacts` |

The collection applies across MPC, zero knowledge and other cryptographic research. Construction-specific references are loaded only when relevant. Retained literature examples are primarily MPC-focused and carry their own source/verification qualifications; they do not establish comprehensive coverage of every subfield.

