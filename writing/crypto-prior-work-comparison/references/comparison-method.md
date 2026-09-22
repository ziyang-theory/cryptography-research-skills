# Comparison method

Use for substantial comparison sections or tables and uncertain numerical accounting. The entrypoint supplies the basic workflow; this reference addresses the alignment decisions that can change the conclusion.

## Record only the evidence the comparison needs

A useful internal contract is: compare **object/version**, under **model and setup**, in **parameter/workload regime**, measuring **metric and phase**, with **aggregation and exclusions**.

For each substantive claim or cell, retain its primary-source locator, guarantee and setup, parameters, units, provenance, and material caveat. Omit empirical fields for theorem-only work. Track artifact lineage separately from paper version: author implementation, independent reproduction, port, adapter, or transformed variant. Preserve historical variant identities when a local default changes.

## Choose the comparison layer

| Layer | What must align |
| --- | --- |
| Theorem or feature | Functionality, assumptions, corruption, output/leakage, setup, oracle, composition, reuse |
| Asymptotic | Variables and scaling regime, including additive terms and what is held fixed |
| Concrete analytical | Formula, chosen parameters, unit conversion, and excluded work |
| Empirical | Implemented behavior, platform, workload, measurement boundary, and concurrency |

A calculation can explain a measured result without becoming a measurement. A component rate is not end-to-end performance.

For `Adv_scheme(A) <= L * Adv_primitive(B) + delta`, compare `B`'s resources, usage limits, and additive errors before translating a smaller `L` into parameters or costs. Improved certified security for unchanged algorithms is different from lower runtime or an attack matching the older bound. A measured sampler outside the theorem's ensemble does not establish matched concrete security through its field/key width.

## Resolve material mismatches

**Model.** Preserve corruption timing and threshold, abort/fairness/delivery, oracle access, setup and reuse. Point-to-point versus broadcast or honest versus dishonest majority can change the ranking. For proof systems, distinguish soundness, knowledge soundness, zero knowledge, and any recursion or composition claim. Another use of a random oracle does not justify a Fiat–Shamir transformation.

**Workload.** Match circuit version and gate counts, domain/field, input/output sizes, batch size, parties, and execution count. A shared benchmark name such as AES does not imply the same circuit. For proof systems, match relation semantics, arithmetization, witness/public-input sizes, trace shape, and included witness computation; equal constraint counts alone are insufficient.

**Costs.** Separate seed/setup generation, function-independent and function-dependent preprocessing, expansion, input processing, and evaluation where applicable. Preserve fixed and input/output terms alongside per-gate coefficients. For proof systems, distinguish setup, compilation, witness generation, prover/verifier work, proof bytes, statement bytes, and CRS/key sizes. A prepared-state comparison is legitimate when its excluded preparation is explicit.

**Communication and rounds.** Specify units, direction/aggregation, logical payload versus transport, speaking topology, and excluded ideal calls or setup. Single execution, parallel amortization, sequential reuse, and per-party totals are not interchangeable.

**Time.** Distinguish wall time, CPU time, a sum of phase maxima, a maximum of party totals, and estimates from component rates. Retain critical-path overlap, network, initialization/check/cleanup, and setup exclusions. A localhost ranking does not establish performance under another network.

If an unsupported conversion is needed to align an axis, compare conditionally or state incomparability. Preserve a baseline's advantage on other axes. Unavailable reruns retain the original source conditions; they are neither zero costs nor negative results.

## Make provenance visible

Use labels or a compact legend only for categories present: measured, rerun, inherited, derived, estimated/extrapolated, projected. Put them in cells, row labels, captions, or adjacent prose. A quotient calculated from cited measurements is derived, not a rate reported by the source.

Rows should identify construction variants. Metric headers need units and denominators. Distinguish phase totals from their components; define unavailable values as not reported rather than zero. Highlight winners only among comparable entries. Separate theoretical and empirical tables when one table obscures their different conclusions.

## Explain and verify the result

Organize around the scientific distinction, such as setup/online, single/amortized, model, or regime, rather than chronology. Distinguish coauthored earlier work from external baselines when relevant. Give both absolute values and the ratio's direction; explain the operation removed, shared, or shifted and its compensating cost. A crossover calculation can be more informative than a favorable endpoint.

Recompute totals, ratios, conversions, amortization, and break-even values. Reconcile row/column labels, captions, formulas, and prose against the source. Published tables can contain arithmetic or labeling errors. Scope first/best/optimal/practical/free claims to the evidence actually established; missing phases or implementations cannot support an unqualified end-to-end winner.
