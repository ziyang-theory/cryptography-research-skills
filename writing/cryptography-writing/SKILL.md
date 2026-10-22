---
name: cryptography-writing
description: Draft or minimally edit cryptography manuscripts, including definitions, theorem statements, security arguments, abstracts, and technical overviews. Preserve the construction and guarantee; use crypto-proof-auditor for substantive proof-validity review.
---

# Cryptography Writing

Make the contribution and argument precise and readable. Use established terms when they express the intended formal meaning; otherwise name the object or relationship plainly. Theory-only writing needs no implementation or experiments.

Use [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org/STE_faq.html) as plain-language style guidance: prefer clear, focused sentences and active voice where appropriate. Judge clarity by continuity, emphasis, and grammatical structure as well as length; a longer or passive sentence may keep the relationship clearer. Do not impose the standard's restricted vocabulary or dictionary-based word-use restrictions. Preserve mathematical precision, established cryptographic terminology, notation, and the author's explicit instructions.

Prefer concrete cryptographic nouns and operations over generic labels such as “endpoints,” “layer,” “interface,” “publish,” or “pad.” Name the parties, OT roles, protocol phase, primitive, PRF outputs, messages, broadcast, or reconstruction actually meant. Prefer “corrupted parties” to “coalition” when describing the corrupted set, and name supplied correlations rather than calling them “scalar correlations” or “OT state.” Explain what is sampled or causes an abort instead of relying on “marginal” or “cutoff” alone.

For drafting or terminology revision, use the wording defaults in [terminology](references/terminology.md). They express preferred prose, not claims that the avoided words are unknown in cryptography. Preserve exact mathematical distinctions, formal interfaces, complete retained state, source-defined terms, and technically meaningful uses such as “one-time pad.” Local author instructions can override these defaults.

## State results directly

State the strongest supported contribution directly. Remove apologies, repeated caveats, and imagined reviewer objections that add no information. Express limitations as precise scope conditions or tradeoffs, without turning a local negative result into a judgment on the whole construction. Keep qualifications that change the claim, including the corruption model, setup, leakage, abort guarantee, and unresolved proof obligations. Do not ban words mechanically: “only the output is revealed” can state an essential guarantee.

## Work from the active claim

Check project guidance for the author's explicit wording corrections and
accepted replacements. Preserve their scope and later reverts. When an
existing term already names the intended object, prefer it to inventing and
defining another label; a terminology question alone does not authorize
manuscript edits.

1. Resolve the requested source version and active text. Read the relevant definitions, notation, theorem, and nearby argument before changing a technical claim.
2. Identify what the sentence relies on: the experiment or functionality, adversary and corruption, setup and oracle access, quantifiers and bounds, assumptions, composition, leakage, and output guarantee. State the material conditions or point to a definition fixing them; do not repeat the whole model in every sentence.
3. Distinguish the intended target, the theorem stated, the reasoning supplied, and any implemented variant. Draft only what the available material supports; never invent a citation, proof step, assumption, or result.
4. Match the work to the request. Reviewing or suggesting wording does not authorize file edits. For authorized edits, preserve unrelated changes and make the smallest technically correct repair unless a rewrite is requested. Keep notation, macros, labels, comments, wrapping, and the author's voice.
5. Check the resulting claim against its sources and inspect the diff. Follow applicable manuscript checks when editing source files. If a repair requires a new model, theorem, or authorial choice, report the ambiguity and a narrow alternative rather than silently changing it.

Local definitions take precedence over generic terminology. Keep correctness, security, and implementation evidence distinct; likewise joint distributions versus marginals, success probability versus advantage, concrete versus asymptotic bounds, and ideal-resource guarantees versus concrete instantiations. A stylistic edit cannot establish a missing theorem.

## Load details only for the current task

Use the entrypoint alone for a straightforward grammar edit with fixed meaning. For drafting or terminology changes, use the terminology reference above; read other references only for the relevant task:

| Task | Reference |
| --- | --- |
| Abstract, introduction, or conclusion structure; consistency with a technical overview | [Abstracts, introductions, and conclusions](references/abstracts-and-introductions.md) |
| Explain a construction or proof idea | [Technical overviews](references/technical-overviews.md) |
| Sentence or paragraph coherence; substantial prose revision | [Prose and coherence](references/prose-and-coherence.md) |
| Exposition of definitions, notation, formulas, or lemmas | [Mathematical exposition](references/mathematical-exposition.md) |
| Preferred wording, an ambiguous cryptographic word, or a claim verb | [Terminology](references/terminology.md) |
| Security statements, experiments, reductions, or full proofs | [Security claims](references/security-claims.md) |
| MPC, simulation, corruption, composition, or output guarantees | [Secure computation](references/secure-computation.md) |
| Proof systems, extraction, commitments, or oracle models | [Proof systems and oracles](references/proof-systems-and-oracles.md) |
| Construction interfaces, preprocessing, rounds, or costs | [Constructions and costs](references/constructions-and-costs.md) |
| Mixed edit authorization or multiple manuscript variants | [Conservative editing](references/conservative-editing.md) |

The narrative guides link optional source examples; those corpora are not required reading. Load multiple references only when the claim actually crosses their topics.

## Full proof drafting

For a new simulation-based proof or an authorized substantial rewrite, a useful default is to describe the simulator's information, interfaces, state, and behavior, then justify meaningful real-to-ideal transitions and accumulate their bounds. Preserve the complete joint view and conditional distributions, including for perfect security. A direct equality-of-distributions argument can suffice; do not invent intermediate experiments or impose particular labels. Follow the governing definition and the author's organization when another presentation is clearer.

A requested substantive validity audit or proof completion may need `crypto-proof-auditor`; source/PDF verification may need `crypto-manuscript-qa`. Use companions only for those additional tasks, not automatically during prose editing. Deliver the prose or minimal patch, with only material unresolved technical questions.
