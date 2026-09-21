# Implementation and evaluation method

Use this reference to organize implementation details, methodology, results, comparison, and limitations.

## 1. Build a results table

Record each result before prose:

| Field | Record |
| --- | --- |
| Artifact | Repository, revision, build profile, dependency versions |
| Construction | Exact protocol/version/path and implemented optimizations |
| Functionality | Task, input/output owners and recipients, leakage, approximation/correctness target |
| Security | Corruption model/threshold, setup/trust and relevant delivery guarantees, computational/statistical parameters, primitive instantiations, omitted checks or model deviations |
| Workload | Circuit/relation, size and composition, field, parties, inputs/outputs, batch |
| Environment | CPU/GPU, cores/threads, RAM, OS, compiler, network, topology |
| Procedure | Warmups, measured trials, experimental unit, execution order, independence, exclusion policy, timeout, statistic and dispersion |
| Timed operations | Start/stop events, phases, included setup, checks and cleanup, overlap and concurrency |
| Metric | Time, throughput, communication, memory, rounds, operations, seed size |
| Aggregation | Per party, maximum, sum, critical path, amortization denominator |
| Value | Number/formula with unit |
| Provenance | Measured, rerun, inherited, derived, estimated, extrapolated, projected |
| Evidence | Raw file/command or primary-source table/figure/formula |
| Caveat | Exclusions, failures, mismatch, uncertainty |

Use only claims supported by this table. Preserve raw evidence or a stable pointer to it when available.

Link each headline to the observation that supports it and any unresolved alternative explanation. Use the [argument and experiment guide](argument-and-experiments.md) when the claim needs additional evidence or a comparison needs redesign; a working note or extra columns suffice.

## 2. Describe implementation scope

Open with what exists, not with a speedup:

- implemented protocol variants and unimplemented variants;
- language, libraries, backend primitives, and code revision;
- correspondence between proof-level abstractions and concrete primitives;
- optimizations that materially change cost, memory, parallelism, or messages;
- deviations from the paper algorithm and their correctness/security status;
- artifact availability and reproduction entry point.

Distinguish the original artifact, a local reproduction, an architecture port, and a protocol transformation. Record optimizations by the version that actually produced the data. Fiat–Shamir challenges, seeded challenges, and literal challenges are different variants; shorter communication after a transformation does not transfer the original proof automatically, even when both use a random oracle.

Explain each material optimization as `baseline operation -> change -> affected cost`. Do not narrate ordinary code structure unless it changes interpretation or reproducibility.

If an insecure primitive or reduced-round configuration is used diagnostically, label it in every relevant table/figure and explain exactly what it is intended to approximate. Never include it in a security-qualified ranking.

## 3. State security and parameter selection

List computational and statistical security parameters, field/ring and key sizes, soundness/error targets, batch/bucket parameters, and construction-specific choices. Explain whether parameters come from a theorem, an attack estimator, a cited script, or a heuristic search.

Identify the actual sampling distribution and any conditioning, certification, seed expansion, or reuse. If it differs from the theorem's distribution, say which construction the theorem covers and which implementation the measurements cover. Do not add a new security assumption merely to make a performance section sound consistent. Explain supported parameter-selection reasons and the material uncertainty concisely; do not replace those reasons with repeated disclaimers or an invented lower security target.

State the search range, tuning budget, and objective (for example, bytes, latency, or throughput); these can select different parameters. If the search finds only a local or heuristic optimum, say `best found under this search`, not `optimal`. If security mapping is uncertain, propagate that uncertainty to the performance claim. A benchmark at one parameter set does not establish performance at another. Historical paper parameters are not current recommendations; check the applicable primary analysis before proposing a new instantiation.

## 4. Define the environment

Report fields that affect the claim:

- CPU model, physical/virtual cores used, frequency policy, accelerators, RAM;
- OS, compiler and flags, language/runtime, cryptographic library versions;
- machine count, placement, point-to-point or broadcast realization;
- measured latency and usable bandwidth, full/half duplex, traffic shaping;
- process/thread count, pinning, parallelism, overlap, and resource contention.

Do not copy a cloud instance label as if it fully specified the machine. If a field is unknown, state that rather than infer it.

Distinguish requested workers, detected hardware capacity, effective workers after memory/affinity limits, and the best worker count actually tested. A hardware-adaptive default is not a measured optimum. State whether a worker limit is per party or total; concurrent parties on one host contend for its cores and memory.

Distinguish logical parties, machines per party, and processors per machine. State whether the computation budget grows with party count. Separate localhost, shaped links, and geographic deployments; measured RTT/bandwidth and shaping settings are different facts. Topology and hardware changes can confound network or party-scaling claims.

## 5. Define workloads and phase boundaries

Name the workload completely: circuit source and version, AND/XOR/other gate counts, depth when round latency matters, input/output sizes, field/ring, number of parties, corruption threshold, batch size, and number of generated correlations.

For a proof system, identify the relation/arithmetization and its revision, constraints or trace dimensions, public inputs, witness size and generation method, field, security/soundness target, and any recursion or aggregation. Equal constraint counts across different arithmetizations do not by themselves establish an equivalent workload.

For synthetic workloads, state their distribution and why they stress the claimed property. If different workloads are used for offline and online plots, explain why.

Define phases by dependency and measured events. Depending on the construction, distinguish:

- key/setup or distributed seed generation;
- circuit-independent preprocessing;
- circuit-dependent preprocessing;
- local seed expansion;
- input processing;
- online evaluation and output;
- one-time initialization, transport setup, serialization, checks, secret erasure, and teardown.

For proof systems, separate universal setup, relation-specific preprocessing/key generation, witness generation, proving, proof serialization, verifier preprocessing, and verification as applicable. State whether verifier time includes loading the verification key and processing public inputs. CRS size, proving-key size, proof bytes, and transmitted transcript bytes are different objects.

State the initial state, start/stop events, dependencies on inputs/function/participants, and whether phases overlap. Define which setup is reusable and which outputs are consumed; input independence and an implementation cache do not establish permitted reuse. Input-dependent work remains input-dependent even if performed before the timer starts.

Cold-start cost includes work from the declared initial state through the declared output condition. Warm-start or online-only cost begins from an explicit prepared state; report or flag the preparation cost separately. For non-overlapping sequential executions with justified reusable setup, `(T_setup + sum_j T_fresh,j) / B` is the batch-average cost for `B` executions, not every request's latency. Measure the actual wall-clock interval when phases overlap.

A maximum of per-party wall-clock durations represents elapsed protocol latency only if the measured intervals share an aligned start and cover the required completion events. Otherwise retain them as local-party measurements. Summing party wall-clock durations does not yield CPU work; summing CPU times over the stated processes/threads gives CPU work when the accounting avoids double counting. Neither sum is generally protocol latency.

For asynchronous roles, PCGs, proof-system setup, or consumable correlations, read [setup, phases, and amortization](setup-phases-and-amortization.md).

## 6. Define measurement and accounting

### Time

Specify wall-clock versus CPU time, timer boundaries, warmups, independent measured trials, cold/warm cache state, timeout, and aggregation statistic. State whether repetitions restart processes: process-external warmups do not eliminate first-use initialization inside a newly started process. Moving initialization, transcript checks, or cleanup across a timer changes the metric, not necessarily the protocol performance. Report dispersion or uncertainty appropriate to the sample. Do not write `takes x ms` when `x` is a throughput-derived estimate.

For end-to-end latency, use a complete execution as the experimental unit; observations from its parties are not independent trials. Report execution ordering and any exclusion rule. Preserve slow runs and failures unless a justified, disclosed rule excludes them. A single observation cannot support a claim about measured run-to-run variation.

For a run with party durations `T_i,p` in phases `p`, `sum_p max_i(T_i,p)` and `max_i(sum_p T_i,p)` are generally different summaries; neither replaces a measured complete interval without a justified schedule. Derive each run's requested metric before computing medians or quantiles. An additive total assembled from measured components is not a continuously timed integrated execution.

Define throughput as completed units divided by the included interval. `B / T_batch` for a batch of `B` executions does not determine individual request latency. State startup, batching, and warm-state treatment. Separate mean-of-rates from total-output/total-time aggregation when they differ.

### Communication

State bits/bytes/field elements, logical payload or observed transport bytes, sent direction, per-party maximum or sum, broadcast accounting, and included phases. Check whether summing sent and received counters double-counts transmissions.

For aggregate sent traffic, count each directed-link transmission once: `C_total = sum_{i != j} C_{i->j}`. State the implemented broadcast realization and any retransmission policy when relevant. Distinguish decimal KB/MB from binary KiB/MiB. Reconcile formula-derived payload with observed bytes when both are available; unavailable transport counters are not zero overhead.

### Memory

State resident/allocated/peak definition, party/process, and whether shared resources, memory-mapped files, GPU memory, and preprocessing material are included. Distinguish a source-derived allocation estimate or lower bound from measured peak memory. State cleanup and erasure policy when comparing materialized and streaming paths: freeing an allocation, overwriting owned secret buffers, and a system-wide erasure guarantee are different claims. Record out-of-memory results rather than deleting those rows.

Use distinct labels for timeout, out of memory, unsupported, not implemented, and not run. State the applicable timeout and memory budgets; do not infer why a configuration failed from a blank cell.

### Rounds and operations

Keep logical rounds, simultaneous layers, messages, primitive calls, and network round trips separate. Operation counts are useful explanatory metrics but are not runtime measurements.

## 7. Label evidence provenance

When a section mixes evidence, use a visible legend:

- `M`: measured by the present artifact;
- `R`: baseline rerun locally;
- `I`: inherited from a cited source;
- `D`: derived exactly from a formula or counted operations;
- `E`: estimated or extrapolated under stated assumptions;
- `P`: projected for an unimplemented optimization.

A failed native build, unsupported instruction set, or resource limit can explain why a faithful rerun is unavailable; it is not evidence of a slower protocol. A successful port or bounded smoke run establishes only the tested behavior. If cited measurements remain in the comparison, retain their hardware, parallelism, parameters, and timed-operation qualifications.

An estimate that combines component rates from different machines is not a wall-clock result. A measured proxy supports an upper bound for the intended construction only when a justified cost-dominance mapping holds under aligned conditions; otherwise report it only as a labeled proxy or sensitivity estimate.

Label hardware simulation and synthesis explicitly, retaining target/frequency, memory and transfer assumptions. Simulated cycles, synthesized area and modeled power are distinct from measurements on a physical device; publication or artifact availability does not change that evidence class.

Use full words if a manuscript has conflicting legends. In this guide `P` means projected, not published; inherited publication values use `I`. Mark individual cells or columns when one row combines measured online time with estimated preprocessing. Preserve the exact source version, locator, original conditions, and conversion formula for reused values.

## 8. Organize results

A useful order is:

1. primary end-to-end result by phase;
2. communication and memory;
3. component breakdown or ablation tied to the claimed optimization;
4. scaling with workload, parties, or batch size;
5. aligned baseline comparison and crossover points;
6. bottlenecks, failures, exclusions, and projected improvements.

Do not force this order when the paper's main question is a component, parameter tradeoff, or analytical estimate. In all cases, show absolute values alongside ratios and keep measured and non-measured rows visually distinct. Compute speedups only for aligned scopes; a same-machine rerun alone does not align guarantees or timed work. Define the workload population and aggregation for a geometric-mean speedup, and expose variation and slowdowns as well as the aggregate.

When results span main text and appendix, keep the question, principal result, metric meaning, and material qualifications beside the result. Use specific appendix references for the parameters, procedure, accounting, or detailed analysis; introduce derived columns by naming the measured inputs and modeling step. Preserve user-fixed table order.

Keep qualifications discoverable from each table or figure. A caption can reference shared setup rather than repeat it, but should identify metric, configuration, statistic/uncertainty, included phases, communication convention, provenance markers, and failure codes as relevant.

Suggested table fields:

| Configuration | Security status | Workload | Phase/party | Time statistic | Communication | Peak memory | Provenance | Included/excluded |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

For parameter tradeoffs, place parameters beside metrics rather than in a detached appendix.

## 9. Write calibrated interpretation

### Setup paragraph

> We evaluate revision [id] implementing [variant and optimizations] at [parameters] on [machines/network]. Each workload is [definition]. After [warmups], we run [trials] and report [statistic and dispersion]. Timings include [phases] and exclude [costs]; communication is [direction/aggregation and payload/transport].

### Measured result

> For [workload], the measured [phase] takes [value/statistic] and communicates [value/unit]. The dominant component is [component], consistent with [measured breakdown or operation count].

### Mixed evidence

> Rows marked `M` are measured; `R` reruns the baseline locally; `I` comes from the cited source; `D` is formula-derived; and `E` extrapolates from [source rate]. Direct runtime comparisons here use aligned `M` and `R` configurations; other rows retain their stated conditions.

### Limitation

> The reported path excludes [resource/phase], assumes [setup/network], and does not measure [missing item]. Therefore, the result is [component/online/post-correlation] performance rather than an end-to-end deployment measurement.

### Projection

> The proposed optimization is not implemented. From [explicit model], it is projected to reduce [metric] by [amount] while increasing [other metric]; this remains to be validated empirically.

## 10. Verification pass

Before delivery:

1. Trace every displayed value to raw evidence or a cited primary source. Supplied source notes are pointers, not independent verification; check the exact primary passage before making a new paper-specific attribution. Re-run a benchmark only when the user's task authorizes benchmark execution.
2. Recompute totals, rates, ratios, amortization, units, and extrapolations.
3. Reconcile prose with the exact table row, column, version, and party count.
4. Check every caption and legend against all panels and configurations.
5. Confirm that measured, estimated, inherited, and projected results are visibly distinct.
6. Check that security labels follow any diagnostic or idealized configuration everywhere it appears.
7. Ensure exclusions and failures remain visible in the main result surface.
8. Verify code revision, commands, parameter files, raw results, and artifact links when available.
9. Confirm that every claimed hardware instruction, accelerator, backend, and build feature exists on the stated architecture and was enabled in the measured binary.
10. Remove unsupported claims that an implementation is secure, optimal, practical, or end-to-end.

When a check exposes missing evidence, correct or qualify the text within the authorized scope and identify the smallest useful follow-up. A writing review does not by itself authorize implementing missing checks, changing parameters, or launching new experiments.

Published tables and prose can disagree. Treat arithmetic, headers, captions, and formulas as claims to verify, not as automatically consistent evidence.
