# Skill catalog

[Introduction and installation](../README.md)

Choose by the result needed. The skills cover three stages of research; these are navigation themes, not a required sequence.

## Formulate and understand

| Result needed | Skill |
| --- | --- |
| A candidate definition, next lemma, or counterexample to pursue | [crypto-research-framing](../paper-writing/crypto-research-framing/SKILL.md) |
| What primary sources establish, with exact versions and locators | [crypto-literature-evidence](../paper-writing/crypto-literature-evidence/SKILL.md) |
| An algebraic correlation interface and comparable output/cost units | [crypto-correlation-accounting](../paper-writing/crypto-correlation-accounting/SKILL.md) |

## Write and examine

| Result needed | Skill |
| --- | --- |
| Manuscript prose, definitions, constructions, or an authorized proof draft | [cryptography-writing](../paper-writing/cryptography-writing/SKILL.md) |
| A diagnosis of whether a cryptographic proof establishes its theorem | [crypto-proof-auditor](../paper-writing/crypto-proof-auditor/SKILL.md) |
| A supported comparison with prior work | [crypto-prior-work-comparison](../paper-writing/crypto-prior-work-comparison/SKILL.md) |
| Consistent sources, notation, references, and rendered PDFs | [crypto-manuscript-qa](../paper-writing/crypto-manuscript-qa/SKILL.md) |
| An accurate account of AI contributions and human checking | [crypto-ai-acknowledgements](../paper-writing/crypto-ai-acknowledgements/SKILL.md) |

## Implement and substantiate

| Result needed | Skill |
| --- | --- |
| Protocol code or an optimization checked against its specification | [crypto-protocol-implementation](../implementation-and-artifacts/crypto-protocol-implementation/SKILL.md) |
| Reproducible measurements and calculations | [crypto-benchmarking](../implementation-and-artifacts/crypto-benchmarking/SKILL.md) |
| An evaluation section supported by experimental evidence | [crypto-implementation-evaluation-writing](../implementation-and-artifacts/crypto-implementation-evaluation-writing/SKILL.md) |
| A reproducible package and reviewer workflow | [crypto-research-artifacts](../implementation-and-artifacts/crypto-research-artifacts/SKILL.md) |

## Boundaries that matter

Start with the skill matching the requested deliverable; add another only for a distinct part of the task. Finding a paper belongs to literature evidence; positioning a result against it belongs to prior-work comparison. Explaining a supplied proof belongs to writing; assessing its validity belongs to proof auditing. Defining a correlation unit belongs to accounting; measuring its rate belongs to benchmarking. Writing an evaluation or packaging an artifact uses existing evidence unless new experiments are part of the request.

All skills follow the same principle: identify the claim, determine what evidence supports it, and keep the conclusion within that evidence. A plausible research direction, a polished proof, passing tests, measured speed, and a reproducible package establish different things.

## Installation and references

**Paper Writing** contains the first eight skills and works on its own for theoretical research. **Implementation & Artifacts** contains the last four. These two installation collections and the individual skill names are unchanged. Correlation accounting includes symbolic costs; it does not require measurements.

Each skill is self-contained. Its entrypoint supplies the core workflow and links to detail needed only for particular tasks. Companion skills are optional; reference links do not require reading the whole library. Literature examples retain their source and verification qualifications and are mainly MPC-focused, rather than comprehensive coverage of cryptography.
