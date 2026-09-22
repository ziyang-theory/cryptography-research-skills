# Skill catalog

[Introduction and installation](../README.md)

Choose by the result needed. Research, Writing, and Implementation are independently installable collections, not a required sequence. Each skill has one home according to its main deliverable.

## Research

Use this group to formulate thoughts in a clean way: state the question, distinguish facts from assumptions and conjectures, expose the obstacle, and identify the next lemma, counterexample, or unresolved choice. Start with research framing for a rough idea; bring in the other skills when the question needs source evidence, proof review, or precise accounting.

| Result needed | Skill |
| --- | --- |
| A clear research question, candidate definition, next lemma, or counterexample | [crypto-research-framing](../research/crypto-research-framing/SKILL.md) |
| What primary sources establish, with exact versions and locators | [crypto-literature-evidence](../research/crypto-literature-evidence/SKILL.md) |
| A diagnosis of whether a cryptographic argument establishes its claim | [crypto-proof-auditor](../research/crypto-proof-auditor/SKILL.md) |
| An algebraic correlation interface and comparable output/cost units | [crypto-correlation-accounting](../research/crypto-correlation-accounting/SKILL.md) |

## Writing

Use this group to express ideas and supported results clearly and prepare the manuscript. It includes evaluation prose even when the underlying measurements come from implementation work.

| Result needed | Skill |
| --- | --- |
| Manuscript prose, definitions, constructions, or an authorized proof draft | [cryptography-writing](../writing/cryptography-writing/SKILL.md) |
| A supported comparison with prior work | [crypto-prior-work-comparison](../writing/crypto-prior-work-comparison/SKILL.md) |
| An evaluation section supported by experimental evidence | [crypto-implementation-evaluation-writing](../writing/crypto-implementation-evaluation-writing/SKILL.md) |
| Consistent sources, notation, references, and rendered PDFs | [crypto-manuscript-qa](../writing/crypto-manuscript-qa/SKILL.md) |
| An accurate account of AI contributions and human checking | [crypto-ai-acknowledgements](../writing/crypto-ai-acknowledgements/SKILL.md) |

## Implementation

Use this group to build protocols, collect reproducible measurements, and prepare runnable artifacts.

| Result needed | Skill |
| --- | --- |
| Protocol code or an optimization checked against its specification | [crypto-protocol-implementation](../implementation/crypto-protocol-implementation/SKILL.md) |
| Reproducible measurements and calculations | [crypto-benchmarking](../implementation/crypto-benchmarking/SKILL.md) |
| A reproducible package and reviewer workflow | [crypto-research-artifacts](../implementation/crypto-research-artifacts/SKILL.md) |

## Boundaries that matter

Start with the skill matching the requested deliverable; add another only for a distinct part of the task. Finding a paper belongs to literature evidence; positioning a result against it belongs to prior-work comparison. Explaining a supplied proof belongs to writing; assessing its validity belongs to proof auditing. Defining a correlation unit belongs to accounting; measuring its rate belongs to benchmarking. Writing an evaluation or packaging an artifact uses existing evidence unless new experiments are part of the request.

All skills follow the same principle: identify the claim, determine what evidence supports it, and keep the conclusion within that evidence. A plausible research direction, a polished proof, passing tests, measured speed, and a reproducible package establish different things.

## Installation and references

Select `research` (four skills), `writing` (five), `implementation` (three), or `all` (twelve). Individual skill names are unchanged. Research framing does not require a manuscript, and correlation accounting includes symbolic costs without measurements.

Each skill is self-contained. Its entrypoint supplies the core workflow and links to detail needed only for particular tasks. Companion skills are optional; reference links do not require reading the whole library. Literature examples retain their source and verification qualifications and are mainly MPC-focused, rather than comprehensive coverage of cryptography.
