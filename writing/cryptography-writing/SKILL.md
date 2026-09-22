---
name: cryptography-writing
description: Draft or minimally edit cryptography manuscripts, including definitions, theorem statements, security arguments, abstracts, and technical overviews. Preserve the construction and guarantee; use crypto-proof-auditor for substantive proof-validity review.
---

# Cryptography Writing

Make the contribution and argument precise and readable. Use established terms when they express the intended formal meaning; otherwise name the object or relationship plainly. Theory-only writing needs no implementation or experiments.

## Work from the active claim

1. Resolve the requested source version and active text. Read the relevant definitions, notation, theorem, and nearby argument before changing a technical claim.
2. Identify what the sentence relies on: the experiment or functionality, adversary and corruption, setup and oracle access, quantifiers and bounds, assumptions, composition, leakage, and output guarantee. State the material conditions or point to a definition fixing them; do not repeat the whole model in every sentence.
3. Distinguish the intended target, the theorem stated, the reasoning supplied, and any implemented variant. Draft only what the available material supports; never invent a citation, proof step, assumption, or result.
4. Match the work to the request. Reviewing or suggesting wording does not authorize file edits. For authorized edits, preserve unrelated changes and make the smallest technically correct repair unless a rewrite is requested. Keep notation, macros, labels, comments, wrapping, and the author's voice.
5. Check the resulting claim against its sources and inspect the diff. Follow applicable manuscript checks when editing source files. If a repair requires a new model, theorem, or authorial choice, report the ambiguity and a narrow alternative rather than silently changing it.

Local definitions take precedence over generic terminology. Keep correctness, security, and implementation evidence distinct; likewise joint distributions versus marginals, success probability versus advantage, concrete versus asymptotic bounds, and ideal-resource guarantees versus concrete instantiations. A stylistic edit cannot establish a missing theorem.

## Load details only for the current task

Use the entrypoint alone for a straightforward edit with fixed meaning. Read the relevant reference when drafting substantial material or resolving an uncertainty:

| Task | Reference |
| --- | --- |
| Abstract/introduction structure or consistency with a technical overview | [Abstracts and introductions](references/abstracts-and-introductions.md) |
| Explain a construction or proof idea | [Technical overviews](references/technical-overviews.md) |
| Ambiguous cryptographic word or claim verb | [Terminology](references/terminology.md) |
| Security statements, experiments, reductions, or full proofs | [Security claims](references/security-claims.md) |
| MPC, simulation, corruption, composition, or output guarantees | [Secure computation](references/secure-computation.md) |
| Proof systems, extraction, commitments, or oracle models | [Proof systems and oracles](references/proof-systems-and-oracles.md) |
| Construction interfaces, preprocessing, rounds, or costs | [Constructions and costs](references/constructions-and-costs.md) |
| Mixed edit authorization or multiple manuscript variants | [Conservative editing](references/conservative-editing.md) |

The narrative guides link optional source examples; those corpora are not required reading. Load multiple references only when the claim actually crosses their topics.

## Full proof drafting

For a new simulation-based proof or an authorized substantial rewrite, a useful default is to describe the simulator's information, interfaces, state, and behavior, then justify meaningful real-to-ideal transitions and accumulate their bounds. Preserve the complete joint view and conditional distributions, including for perfect security. A direct equality-of-distributions argument can suffice; do not invent intermediate experiments or impose particular labels. Follow the governing definition and the author's organization when another presentation is clearer.

A requested substantive validity audit or proof completion may need `crypto-proof-auditor`; source/PDF verification may need `crypto-manuscript-qa`. Use companions only for those additional tasks, not automatically during prose editing. Deliver the prose or minimal patch, with only material unresolved technical questions.
