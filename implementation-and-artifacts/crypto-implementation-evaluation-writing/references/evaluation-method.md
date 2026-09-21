# Evaluation records and accounting

Use the sections needed to resolve a result's configuration, metric or provenance. For narrative and comparison design, use [argument and experiments](argument-and-experiments.md); for setup and resource lifetimes, use [setup, phases and amortization](setup-phases-and-amortization.md).

## Result record

Keep the fields that affect the claim, in existing notes or a compact working table:

| Field | Record |
| --- | --- |
| Artifact | Repository/revision, build profile, dependencies and enabled features |
| Construction | Protocol/version, implemented optimizations, omissions and deviations |
| Functionality | Task, input/output ownership, leakage and numerical correctness/approximation target |
| Security | Corruption model, setup/trust, delivery guarantee, parameters and primitive choices |
| Workload | Circuit/relation and version, field, dimensions, parties, inputs/outputs and batch |
| Environment | Actual CPU/GPU, memory, OS/compiler, topology, link properties and concurrency |
| Procedure | Warmups, trials, experimental unit/order, exclusion rule, timeouts and statistic/dispersion |
| Metric | Units, included operations, start/stop events, prepared state, aggregation and denominator |
| Evidence | Raw file/command or exact primary-source locator, value/formula and evidence class |
| Limitation | Failures, excluded work, unknowns, mismatches and uncertainty |

A cloud instance label does not fully specify hardware. Distinguish configured workers, process-visible capacity and observed effective workers; a hardware-adaptive default is not a measured optimum. State whether budgets are per party or total. Distinguish logical parties, machines per party and processors per machine, including how the budget changes with party count. Localhost, shaped links and geographic deployments are different environments; configured limits are not measured RTT/bandwidth.

For Boolean workloads, include gate composition and depth when relevant. For proof systems, identify arithmetization, constraints/domain, public-input/witness sizes and any recursion or aggregation. Equal gate or constraint counts need not define an equivalent workload. Explain synthetic workload distributions and any change of workload between phase plots.

## Implementation and parameter scope

Describe material optimizations as `baseline operation -> change -> affected cost`, using the version that generated the data. Keep original artifacts, reproductions, ports and transformations distinct. Fiat–Shamir, seeded and literal challenges have separate variant identities and proof obligations.

State where parameters come from: theorem, attack analysis/estimator, cited script or heuristic search. Identify the actual sampler and any conditioning, certification, expansion or reuse. Explain supported parameter-selection reasons and uncertainty without inventing an assumption or lower security target. Historical parameters are not current recommendations.

For tuning, state the search range, budget and objective; use “best found under this search” for a heuristic result. An insecure diagnostic configuration must remain labeled in every affected table/figure and outside security-qualified rankings. A project-selected default is not original-author endorsement or transferred proof support.

## Metric semantics

### Time and repetitions

Name the experimental unit and start/stop events. For protocol latency, a complete execution is one trial; its parties are not independent repetitions. Record process restart and cache policy: warmup processes do not warm first-use initialization in later fresh processes. Preserve slow runs and failures unless a disclosed, justified rule excludes them. One observation does not measure run-to-run variation.

Distinguish continuous wall time, CPU work, local-party time and assembled totals. For party durations `T_i,p`, `sum_p max_i(T_i,p)` and `max_i(sum_p T_i,p)` generally differ; neither replaces a measured complete interval without a justified schedule. A maximum of local durations represents completion time only with aligned starts and matching completion events. Summing wall durations does not yield CPU work; CPU times can be summed with a scope that avoids double counting.

Derive each execution's metric before aggregating trials: `median(a_i+b_i)` need not equal `median(a_i)+median(b_i)`. State the statistic and supported dispersion/uncertainty. Moving initialization, checks or cleanup across the timer changes the metric.

Define throughput as completed useful units divided by the included interval. `B/T_batch` does not determine individual latency. Distinguish total-output/total-time from mean-of-rates aggregation, and report startup/batch treatment. Use an explicit prepared state for online or warm-start measurements; consult the [phase guide](setup-phases-and-amortization.md) when preparation, reuse or overlap matters.

### Communication and rounds

Specify logical bits/field elements, framed bytes or transport bytes; included phases; direction; party aggregation; and broadcast convention. For aggregate sent traffic, `C_total = sum_{i != j} C_{i->j}` counts each directed transmission once. Adding matching receive counters counts it twice. State broadcast realization and retransmission policy when relevant, and distinguish decimal KB/MB from binary KiB/MiB.

Retain fixed/input/output terms in finite-instance formulas. Explain differences between logical counts and wire counters; unavailable transport data is not zero overhead. Logical rounds, simultaneous layers, messages, primitive calls and network round trips are different quantities.

### Memory and failures

Identify allocated/resident/peak memory, party/process and included shared, mapped, device and preprocessing storage. Source-derived allocation estimates are not measured peak RSS. Freeing an allocation, wiping controlled buffers and system-wide erasure are distinct claims.

Use distinct statuses for timeout, out of memory, unsupported, not implemented and not run, with applicable limits. Do not infer a failure cause from an empty cell.

## Evidence classes

Use full words or a compact legend consistent with the manuscript:

| Class | Meaning |
| --- | --- |
| Measured | Observed in the present artifact/configuration |
| Rerun | Baseline executed locally |
| Inherited | Reported by an identified source under its conditions |
| Derived | Exact formula or counted-operation calculation |
| Estimated/extrapolated | Model using stated inputs and assumptions |
| Projected | Proposed, unimplemented optimization |

Mark cells or columns when one row mixes classes. Retain source version/locator, original conditions and conversion formula. Cross-machine component rates do not form a measured wall time. A measured proxy is an upper bound only with a justified cost-dominance mapping under aligned conditions; otherwise label it as a proxy or sensitivity estimate.

Label hardware simulation and synthesis with target/frequency, memory and transfer assumptions; simulated cycles, area and modeled power differ from device measurements. A failed build or resource limit does not show a slower protocol, and a smoke run covers only its tested behavior.

## Results and verification

Adapt the order to the claim: primary result, explanatory phase/component costs, comparisons, tradeoffs and limitations. Analytical or component work need not invent an end-to-end result. Show absolute values alongside ratios, and compute speedups only for aligned scopes. For geometric-mean speedups, define the workload population and expose variation and slowdowns.

Keep the principal result, metric meaning and material qualifications beside the table/figure. A caption can reference shared setup. Use specific appendix references for procedure and detail, preserve user-fixed table order, and explain measured inputs and modeling steps behind derived columns. Keep parameter tradeoffs visible beside their metrics.

Before delivery, check the affected claims:

- Trace values to raw evidence or exact primary passages; source notes alone do not verify a new attribution.
- Recompute totals, ratios, amortization and units; reconcile table headers, captions, legends, formulas and prose.
- Confirm evidence classes, security qualifications, failures and exclusions remain visible where needed.
- Verify available revision, command and parameter pointers, including claimed hardware/build features in the measured executable.
- Narrow unsupported claims of security, optimality, practicality or end-to-end performance.

A mismatch can be reported or corrected within the requested scope. It does not itself require a benchmark rerun, code change or parameter change.
