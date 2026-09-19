---
name: cryptography-writing
description: Draft or minimally edit cryptography manuscripts, including abstracts, introductions, definitions, theorem statements, security arguments, and efficiency claims, while preserving the construction, model, and guarantee. Use crypto-proof-auditor for proof-validity audits; not for code, raw benchmarks, or PDF-only layout.
---

# Cryptography Writing

Use established cryptographic terms of art when they express the exact formal meaning. Do not add jargon for tone, silently strengthen a claim, or import assumptions absent from the source. Apply this guidance across MPC, zero knowledge, proof systems, and other cryptographic research; construction-specific examples are conditional, not defaults for a new project.

Theory-only work needs no implementation, benchmark, or artifact. Use the manuscript and relevant mathematical sources; consult empirical evidence only for claims that use it. Companion skills are optional: if absent, continue the authorized task with the guidance here and in its references, without treating prose quality as proof validation.

When writing, prefer established cryptographic terminology and concrete descriptions. Avoid vague or metaphorical uses of “loss,” “resource,” “ledger,” “boundary,” and “bridge”; name the actual quantity, primitive, assumption, protocol phase, or implication. Preserve technically necessary uses, such as “reduction loss,” and formally defined terminology. Follow the [shared terminology guidance](references/terminology.md) for context-specific alternatives.

## Authorization and scope

A request to review, explain, proofread, or suggest wording is read-only unless it explicitly asks for file edits. When editing is authorized, preserve unrelated worktree changes and stay within the requested surface.

## Route the task

- Read [references/abstracts-and-introductions.md](references/abstracts-and-introductions.md) for a new abstract or introduction, an authorized rewrite, or a review of their organization. It gives contribution-dependent structures and links to a citation-selected MPC writing corpus; do not impose a new structure during a local wording edit.

- Read [references/technical-overviews.md](references/technical-overviews.md) for a technical overview, overview of techniques, approach section, or explanatory proof outline, whether inside or after the introduction. Use it for new writing, an authorized structural rewrite, or review of exposition; preserve local-edit boundaries.
- Read [references/terminology.md](references/terminology.md) for any cryptography-facing draft or terminology edit.
- Read [references/security-claims.md](references/security-claims.md) for formal security claims, definitions or experiments, assumptions, reductions, hybrid arguments, advantage bounds, and concrete or asymptotic claims.
- Read [references/secure-computation.md](references/secure-computation.md) for real/ideal security, MPC or 2PC, corruption, composition, output guarantees, leakage, secret sharing, reactive or reusable resources, and MPC or 2PC preprocessing.
- Read [references/proof-systems-and-oracles.md](references/proof-systems-and-oracles.md) for proofs and arguments, PCPs and IOPs, soundness, knowledge extraction, zero knowledge, Fiat--Shamir transformations, commitments, random oracles, proof-system setup or preprocessing, and succinctness.
- Read [references/constructions-and-costs.md](references/constructions-and-costs.md) for primitives or ideal resources, black-box constructions, OLE/VOLE/OT correlations, PCGs, garbling, FSS, NISC, compilers, setup and phase boundaries, rounds, communication, amortization, or performance comparisons.
- Read [references/conservative-editing.md](references/conservative-editing.md) before editing any existing prose or LaTeX.
- For technical proof-validity audits, theorem-to-proof consistency checks, or proof-gap searches, use `crypto-proof-auditor` when available. This skill supplies terminology and claim-definition discipline; writing alone does not validate a proof.
- Read only the specialized references implicated by the task. Read multiple references when a formal claim crosses their boundaries.
- For manuscript source selection, LaTeX builds, cross-references, and rendered PDF checks, use `crypto-manuscript-qa` when available.
- Follow applicable project-local guidance for source selection, notation, construction invariants, and document checks. This skill requires no particular repository, manuscript layout, protocol, or parameter profile.

## Proof organization

For a new simulation-based security proof, or an authorized substantial rewrite or completion of one, describe each simulator's permitted information, interfaces, state, and behavior; then present explicit real-to-simulated hybrids and accumulate the distinguishing bound. Use consecutive `Hyb_0:`, `Hyb_1:`, ... labels (`$\mathsf{Hyb}_0$:` in LaTeX), introducing each hybrid and justifying its transition before proceeding. Read [references/security-claims.md](references/security-claims.md) for the complete experiment, surrounding-view, repeated-family, and reduction obligations.

This organization also applies to perfect-security proofs. Exact distributional equalities and conditional-distribution arguments can justify hybrid transitions; do not omit hybrids merely because a direct equality-of-distributions argument is available. Depart from this organization only when it conflicts with the governing definition or would require vacuous or ill-defined intermediate experiments, and explain the specific reason. Never invent a simulator, assumption, or proof step to satisfy the format.

For claims whose governing definition does not call for simulation, follow the appropriate game-, reduction-, relation-, extraction-, or other proof form. Preserve the source's proof organization during local edits. This presentation requirement does not establish validity or authorize a changed theorem.

## Working method

1. Resolve the requested source version and active text, then locate its definitions, notation, role names, phase boundaries, and nearby usage. Comments, superseded drafts, and prior chat proposals are not current theorem statements.
2. Identify the claim's independent axes: security notion, adversary and corruption model, target functionality and leakage, setup or oracle model and resource lifetime, quantifiers and bounds, assumptions, composition scope, and output guarantee.
3. Draft the narrowest wording supported by those axes. Distinguish the author's intended target, the current theorem, the argument actually supplied, and any implemented variant. If an axis is unspecified, flag it rather than silently filling it in.
4. For an existing write-up, apply the smallest local repair and leave correct surrounding prose untouched.
5. Audit the result against the relevant reference and the manuscript's validation workflow.

## Non-negotiable invariants

Keep these distinctions explicit whenever they matter:

- correctness versus security;
- prescribed output versus separately declared leakage;
- perfect, statistical, and computational guarantees, and the exact use of information-theoretic or unconditional terminology;
- concrete resource bounds versus asymptotic PPT or QPT security and negligible functions;
- exact equality, identical distribution, statistical distance, and computational indistinguishability;
- success probability or failure probability versus advantage relative to a stated baseline;
- passive versus active behavior, static versus adaptive corruption, and what the word *adaptive* modifies;
- proof versus argument, and completeness, soundness, knowledge soundness, and zero knowledge;
- security with abort, source-defined weakened abort notions, fairness, simultaneous output, and guaranteed output delivery;
- stand-alone, sequential, concurrent, and universally composable security;
- one-shot, bounded-reuse, multi-session, and reactive or stateful resources;
- setup, ideal or hybrid resources, preprocessing, offline work, online work, and concrete instantiation;
- ideal-functionality access, primitive-algorithm access, black-box reductions, and implementation-code access;
- simultaneous message flows, messages, logical rounds, causal protocol steps, and implementation or network layers;
- total, directional, per-party, per-unit, phase-specific, end-to-end, and amortized costs, with their stated unit and denominator;
- PPT versus QPT adversaries and classical versus quantum oracle access.

Never invent a citation, theorem, proof step, assumption, experiment, definition, or numerical result. If the smallest technically correct edit requires authorial judgment or could change the security model, theorem, construction version, leakage, cost boundary, or guarantee, leave the source unchanged and report the ambiguity with a narrow proposed alternative.

## Expected result

For new writing, produce precise prose in the conventional register of cryptography papers and textbooks, with assumptions and scope visible. For edits, make the smallest local repair, inspect ordinary and word-level diffs, and report any unresolved technical ambiguity instead of hiding it through stylistic rewriting.
