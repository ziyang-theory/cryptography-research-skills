---
name: crypto-prior-work-comparison
description: Draft or revise cryptography-paper comparisons with prior results using claim-aligned baselines, explicit models and cost measures, and traceable evidence. Use for introduction, contribution, related-work, comparison-table, and discussion prose. Do not use for literature discovery alone, proof-validity auditing, benchmark execution, or implementation work.
---

# Crypto Prior-Work Comparison

Position a result precisely enough that a reader can tell what is improved, under which model, and at what cost. A comparison is valid only on the axes that have actually been aligned.

Theory-only comparisons use theorem statements, definitions, assumptions, and analytical bounds. Code, experiments, and artifacts are needed only for claims about them. Companion skills are optional; if absent, continue with the source and comparison checks here.

## Authorization and evidence

- Treat review, explanation, or suggested wording as read-only unless the user explicitly requests edits.
- Verify each cited theorem, table entry, parameter, and benchmark against the primary source when the task permits source access. Do not propagate an attribution merely because another paper repeats it.
- Never turn missing, unreported, idealized, or non-comparable data into zero cost.
- Do not strengthen a theorem, security model, implementation claim, or priority claim for rhetorical force.
- Attribute author-maintained artifacts, independent reproductions, ports, hybrid backends, and transformed variants accurately. A local default or a shared codebase does not make a variant the authors' official implementation.
- If concrete security is unestablished for a measured sampler or configuration, preserve the absolute measurement and parameter rationale while qualifying any comparison at matched security.

## Before drafting

Freeze the target result and the comparison contract:

- task or functionality and output guarantee;
- adversary, corruption threshold and timing, setup or hybrid resources, assumptions, oracle model, and composition scope;
- construction version and supported parameter regime;
- compared cost object, phase, unit, direction or aggregation, denominator, and excluded work;
- whether each datum is asymptotic, analytically derived, measured, rerun, inherited, estimated, or projected.

If a difference on one of these axes materially affects the ranking, disclose it next to the comparison. If alignment would require an unsupported conversion, state that the results are incomparable on that axis.

## Working method

For the overall organization of an abstract or introduction, use `cryptography-writing` and its `references/abstracts-and-introductions.md` guide when available. That guide owns the narrative structure; this skill owns baseline selection, aligned comparisons, and evidence provenance. A contribution paragraph should establish the relevant gap before expanding the literature discussion.

Read [references/comparison-method.md](references/comparison-method.md) in full for a new or substantially revised comparison section/table, or whenever numerical provenance, model alignment, or cost accounting is uncertain. For a narrow local sentence edit whose evidence and comparison contract are already fixed, use only the invariants in this entrypoint; load the full method if the edit exposes an uncertainty that requires it.

1. Build a table of claims and supporting sources before drafting prose. Give every claim or table cell a source locator and provenance class.
2. Choose baselines by relevance, not by whichever gives the largest ratio. Include the closest predecessor, the strongest baseline on each claimed axis, and concurrent or orthogonal work when it changes the reader's interpretation.
3. Separate theorem-level, asymptotic, concrete analytical, and empirical comparisons. Never use a result from one layer as if it belonged to another.
4. Normalize comparable axes and expose material differences that remain.
5. Draft in the order: comparison contract, result, mechanism or tradeoff, scope limitation, then evidence.
6. Recompute ratios, totals, amortization, and break-even points. Reconcile table headers, captions, prose, and source formulas.
7. Use the narrowest supported conclusion. Prefer a conditional claim over an unqualified ranking.

Read [references/source-patterns.md](references/source-patterns.md) only when examples from the eight source papers or known failure patterns would help.

## Required distinctions

Keep these separate whenever relevant:

- security guarantee versus efficiency;
- asymptotic improvement versus concrete improvement;
- total, phase-specific, online-only, and setup-excluded cost;
- one-way maximum, per-party, aggregate, broadcast, and point-to-point communication;
- single execution, parallel amortization, sequential amortization, and reusable preprocessing;
- logical rounds, simultaneous layers, and measured latency;
- measured implementation results, calculated operation counts, and estimates from external throughput;
- end-to-end protocol performance and a component or ideal-resource proxy;
- best in one regime and best overall.

## Output standard

The finished section should let a skeptical reader reconstruct the comparison without reverse-engineering the paper. Report unresolved version, model, provenance, or unit ambiguities rather than smoothing them over. Preserve the manuscript's terminology, notation, citations, and voice when editing existing prose.
