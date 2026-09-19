---
name: crypto-literature-evidence
description: Discover, version, extract, and synthesize primary-source cryptography literature with exact theorem, definition, equation, figure, table, section, and page locators. Use for multi-paper surveys, citation verification, paper-exact claims, or learning how papers formalize a concept; not for proof-validity auditing, benchmark execution, or prose revision alone.
---

# Cryptography Literature Evidence

Turn cryptography sources into a traceable evidence map before drawing conclusions or drafting prose. Apply this to MPC, zero knowledge, proof systems, commitments, correlation generators, and other primitives; select the technical axes required by the question rather than assuming a particular protocol family. Treat titles, search snippets, secondary surveys, manuscript citations, and other agents' summaries as discovery aids rather than authoritative evidence.

For prose and reports, avoid vague uses of “loss,” “resource,” “ledger,” “boundary,” and “bridge”; name the precise quantity, primitive, assumption, phase, or implication. Preserve established technical meanings, such as reduction loss, and quoted or formally defined terminology. The optional `cryptography-writing` skill provides further terminology guidance.

## Authorization and routing

Literature discovery and review do not themselves authorize manuscript changes. If the request also asks for edits, perform those edits within its stated scope; otherwise report conflicts and the smallest defensible correction.

This workflow supports theory-only research without code, experiments, or artifacts. Companion skills below are optional: use them when available and relevant; otherwise continue from the primary sources and these evidence checks, keeping proof validity separate from source attribution.

- Read [references/evidence-method.md](references/evidence-method.md) for a multi-paper review, ambiguous version, exact numerical/technical attribution, or corpus-completeness claim.
- For a proof-validity question, also use `crypto-proof-auditor` when available; this skill establishes the cited claim and dependency, not whether the proof is sound.
- For prior-work comparison prose, use `crypto-prior-work-comparison` when available after the evidence map is stable.
- For requested implementation/evaluation prose, use `crypto-implementation-evaluation-writing` when available after measurements and evidence classes are fixed.
- For cryptographic definitions, theorem statements, or manuscript wording, use `cryptography-writing` when available; follow manuscript guidance for the active project when available.

## Core invariants

- Fix the research question and extraction axes before searching. A keyword hit is not evidence that a paper has a dedicated subsection, formal definition, theorem, implementation, or reported measurement.
- Identify the exact paper version and publication date. Reconcile ePrint revisions, proceedings versions, appendices, full versions, and local filenames before comparing numbering or claims.
- Prefer the primary paper and, for implementation or empirical claims, its official artifact when available. Use a later paper's attribution only as a lead unless the task explicitly studies reception or citation history.
- Give every material claim an exact source locator and evidence status. Separate verbatim source content, faithful paraphrase, algebraic derivation, interpretation, and unresolved inference.
- Check equations, symbols, subscripts, table headers, captions, footnotes, and cross-references visually when extraction can corrupt them.
- Reconcile abstract, main text, theorem, appendix, and tables. Published papers can contain swapped columns, stale values, inconsistent formulas, or incomplete informal definitions.
- Never upgrade a source's model, guarantee, implementation status, or evidence class. “Discusses UC” is not “defines UC”; a component estimate is not a measured protocol throughput; security against specified attacks is not a lower bound against all attacks.
- Check applicability independently of attribution: a faithfully quoted rate or theorem can concern a different field, relation, setup, adversary, or parameter distribution. Put any assumption needed to transfer it beside the resulting claim.

## Expected result

Scale the result to the question. For a single claim, give the conclusion, exact source/version and locator, and any decisive qualification. For a survey, report corpus coverage, strict matches versus related discussions, claims and supporting sources, source disagreements, derivations with assumptions, and unresolved dependencies. If drafting follows, distinguish source-supported conclusions from proposed formulations or judgments.
