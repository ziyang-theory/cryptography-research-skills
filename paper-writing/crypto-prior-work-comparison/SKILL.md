---
name: crypto-prior-work-comparison
description: Draft or review cryptography prior-work comparisons and comparison tables by aligning models, construction variants, costs, and evidence. Use for positioning results, not literature discovery alone or benchmark execution.
---

# Crypto Prior-Work Comparison

Make clear what improves, under which conditions, and at what cost. Compare complete supported variants: one theorem's guarantee and another's efficiency do not form a new result.

## Fix what is being compared

Recover the target claim before selecting baselines. Identify the task and output guarantee; adversary, corruption, assumptions and setup; construction version and parameter regime; and the cost's phase, unit, aggregation, denominator, and exclusions. Include only axes that matter to this comparison. Theory-only comparisons use definitions, theorems, and analytical bounds; they need no code or benchmarks.

Select the smallest baseline set that answers the claim: the closest predecessor, the strongest relevant result on each claimed axis, and other work that changes the interpretation. Use relevance, not the largest available ratio. A separate literature search is needed only if the supplied sources cannot support that choice.

## Build and write the comparison

1. Map each substantive claim or table cell to a primary-source version and locator. Verify attributions against that source; distinguish unverified supplied evidence. Preserve author implementations, independent reproductions, ports, and transformed variants as different lineages.
2. Separate theorem-level, asymptotic, concrete analytical, and empirical results. Label numbers as measured, rerun, inherited, derived, estimated, or projected as applicable. A component rate or ideal-resource proxy is not end-to-end performance.
3. Normalize comparable axes and disclose differences affecting the conclusion next to it. Missing or unreported work is not zero. A measured configuration without established concrete security cannot support a security-matched ranking merely from its parameter width.
4. State the result and its mechanism or tradeoff under the aligned conditions. Give absolute values before ratios; recompute totals, conversions, amortization, and break-even points. Reconcile text, headers, captions, and formulas.
5. Use the narrowest supported conclusion. Preserve prior work's remaining advantages and state incomparability where a conversion is unsupported.

Review or suggested wording is read-only unless edits are requested. When editing, preserve the manuscript's notation and voice. Do not strengthen security, performance, or priority claims for rhetorical effect.

## Optional detail

- [Comparison method](references/comparison-method.md): substantial sections/tables, uncertain normalization, or mixed numerical provenance.
- [Source patterns](references/source-patterns.md): examples of comparison structures and known table-consistency pitfalls.
- [Theorem variant cases](references/theorem-variant-cases.md): properties drawn from incompatible variants or compressed quantitative premises.

Use `cryptography-writing` only when the task also requires broader narrative organization, and `crypto-literature-evidence` when additional source research is needed. The comparison itself should remain self-contained. Return reconstructible claims and material unresolved mismatches, without forcing a fixed paragraph order or evidence template onto a small edit.
