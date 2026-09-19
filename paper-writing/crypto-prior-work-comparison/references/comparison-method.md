# Comparison method

Use this reference to turn primary-source evidence into introduction, related-work, contribution, table, or discussion prose.

## 1. Freeze the claim before choosing competitors

Write a one-sentence internal contract:

> We compare **object** under **security/model/setup** for **workload and parameter regime**, measuring **metric and phase** with **aggregation and exclusions**.

A fair comparison begins with the object, not the papers. Two results may solve nominally similar tasks while differing in corruption threshold, fairness or abort, setup, oracle, field, circuit model, amortization, or reuse. These differences can dominate an efficiency ranking.

## 2. Tabulate claims and supporting sources

Record one row per claim or numerical cell:

| Field | Record |
| --- | --- |
| Result | Exact construction and version |
| Source | Primary citation plus section, theorem, table, figure, or page |
| Guarantee | Security notion, adversary, corruption, abort/delivery, composition |
| Setup and ideal functionalities | Setup, hybrid functionalities, preprocessing, oracle, reuse |
| Workload | Circuit/relation, gates, field, inputs/outputs, batch size |
| Parameters | Computational/statistical security and construction parameters |
| Metric | Time, communication, rounds, memory, operation count, seed size, etc. |
| Included costs and aggregation | Phase, direction, per-party/aggregate, logical/transport, exclusions |
| Provenance | Measured, rerun, inherited, derived, estimated, extrapolated, projected |
| Value | Number/formula with units and denominator |
| Caveat | Remaining mismatch or uncertainty |

Record the paper version and, when implementation evidence is involved, artifact lineage separately: author-maintained implementation, local reproduction, port, adapter, or transformed construction. An independent reconstruction can be useful evidence if its implemented and omitted mechanisms remain explicit. Preserve historical variant identifiers when a new default is chosen. For a theorem-only comparison, omit empirical fields and compare the formal guarantees or analytical bounds directly.

Use `N/R` or prose such as "not reported" for unavailable values. A dash is ambiguous unless the caption defines it.

## 3. Separate comparison layers

Do not blend these layers in one ranking:

1. **Theorem and feature layer:** functionality, assumptions, corruption, output guarantee, setup, field, programmability, reuse, round topology.
2. **Asymptotic layer:** formulas with variables and regimes; retain additive terms and what is held fixed.
3. **Concrete analytical layer:** bytes, primitive calls, or predicted latency computed from formulas and chosen parameters.
4. **Empirical layer:** measured code on a stated platform and workload.

An analytical count may explain why an implementation should improve, but it is not a measured speedup. A component benchmark or throughput-derived projection is not end-to-end performance.

## 4. Align the axes

### Security and functionality

Check the exact task, outputs/leakage, passive versus malicious behavior, static versus adaptive corruption, threshold, setup or hybrid model, assumptions, oracle access, abort/fairness/delivery, composition, and reuse. If models differ, compare conditionally:

> Under the point-to-point and dishonest-majority setting, ...; the broadcast/honest-majority baseline has a different trust and corruption profile.

Do not hide a weaker model in a footnote while calling a result "best." For proof systems, align the claimed notion (for example, soundness versus knowledge soundness), zero-knowledge scope, setup/CRS, oracle model, and any recursion or composition claim. Using a random oracle elsewhere does not automatically justify replacing fresh interactive challenges by Fiat–Shamir challenges.

When a measured sampler or parameter regime differs from the theorem's ensemble, distinguish the formal construction from the evaluated instantiation. Key or field width does not establish a matching concrete security level; an illustrative performance comparison should not be sold as a security-matched ranking.

### Workload and parameters

Align circuit version and gate count, field or ring, input/output sizes, security parameters, bucket or batch size, number of parties, number of executions, and single versus amortized mode. A shared benchmark name such as AES is insufficient if circuits differ. For zero-knowledge, align the relation semantics, arithmetization, witness/public-input sizes, constraint or trace shape, and included witness computation; equal constraint counts alone are insufficient.

### Cost boundary

State what each phase may depend on. Separate setup or seed generation, function-independent preprocessing, function-dependent preprocessing, local expansion, input processing, and online evaluation when the construction distinguishes them.

For communication, state units, direction and aggregation, broadcast assumptions, and logical payload versus transport bytes. Preserve finite-instance input/output and fixed terms alongside leading per-gate coefficients. For proof systems, distinguish proof bytes, statement bytes, CRS and key sizes, and full protocol traffic.

For rounds, state speaking topology and exclusions. For time, state wall-clock or CPU, critical-path aggregation, concurrency, network, initialization/check/cleanup policy, and excluded setup. A continuous execution time, a sum of per-phase maxima, a maximum of party totals, and a component-based estimate are different metrics. Fewer rounds or bytes can coexist with slower localhost time; a ranking under one network does not establish another.

Separate proof-system setup, relation compilation, witness generation, prover work, and verifier work. A fixed prepared-state comparison is legitimate when its conditions and excluded preparation are stated consistently.

### Provenance

Prefer a compact legend when a table mixes evidence:

- `M`: measured by the present implementation;
- `R`: baseline rerun under the present environment;
- `I`: inherited from a cited source;
- `D`: derived from a formula or operation count;
- `E`: estimated or extrapolated;
- `P`: projected for an unimplemented optimization.

Retain original conditions for cited data when a faithful local rerun is blocked by architecture, dependencies, memory, or time. An unavailable rerun is not a zero or a negative performance result. A derived quotient of cited measurements remains a derivation; do not attribute that quotient to the source as a reported rate.

Use only the categories present in the paper. Put provenance in the cell, row label, caption, or adjacent prose, not in an invisible workflow note.

## 5. Choose and organize baselines

Use the smallest set that answers the scientific question:

- the direct ancestor, to isolate the new mechanism;
- the best known result on each claimed metric;
- a qualitatively different approach when it exposes a tradeoff;
- concurrent work when priority, assumptions, or practical conclusions change.

Distinguish the authors' own earlier work from external baselines when authorship is relevant to the requested positioning; do not automatically describe coauthored prior work as a competitor.

Organize by the distinction that matters: single versus amortized, online versus total, field regime, party count, setup model, or measured versus unimplemented. Avoid a chronology dump.

## 6. Draft the argument

### Opening contract

> We compare against X, Y, and Z for [workload] at [parameters]. We report [metrics]; [phase/resource] is excluded or reported separately. Results for X are rerun, while values for Y and Z are inherited/derived.

### Aligned quantitative claim

> Under these aligned conditions, our [phase/metric] is `a`, compared with `b` for X, a `b/a`-fold reduction. The total cost is [qualification], because [mechanism or shifted cost].

### Tradeoff or incomparability

> X has lower [metric A], whereas our construction supports [feature/model] and lowers [metric B]. Because X does not report [missing phase] / assumes [different resource], an end-to-end ranking is not supported.

### Unimplemented baseline

> X has not been implemented. Its formula implies [operation count] at these parameters; translating that count using [explicit throughput] gives an estimate, not an end-to-end measurement.

### Regime and break-even point

> X is preferable below [regime], while our scaling becomes smaller above [threshold]. This threshold follows from [formula/table] and is sensitive to [parameter or cost model].

Use ratios to summarize already-visible absolute values, not to replace them. Give both values, units, direction, and whether smaller or larger is better.

## 7. Design comparison tables

Put the contract in the table or caption:

- rows identify construction versions, not only author-year labels;
- columns do not mix phase totals with subphase values;
- units and denominators appear in every metric header;
- model/resource differences have visible columns or adjacent qualifications;
- unavailable values are `N/R`, not zero;
- best-value highlighting applies only within genuinely comparable cells;
- footnotes state conversions, excluded costs, inherited values, and provenance.

When one table cannot support both theoretical and empirical claims, use separate tables.

## 8. Verification pass

Before delivery:

1. Trace every row and numerical claim to a primary-source locator.
2. Recompute totals, ratios, amortized values, unit conversions, and break-even points.
3. Check that the prose names the same row, column, version, and party count as the table.
4. Reconcile caption units with cell units and formulas.
5. Confirm that highlighted winners share the same model, phase, and evidence class.
6. Search for unsupported superlatives: `first`, `best`, `state of the art`, `optimal`, `practical`, `negligible`, and `free`.
7. Replace any unsupported global claim with a scoped claim or an explicit uncertainty.

Published material can contain arithmetic or labeling errors. Source status does not remove the need for internal consistency checks.
