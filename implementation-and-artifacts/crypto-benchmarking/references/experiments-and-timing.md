# Experiments and timing

## Measurement contract

Record the exact construction/variant, source revision and dirty diff or content identity, dependency/toolchain/build settings, actual executable identity, workload identity, parameters, topology, and timer start/stop events. Retain only applicable fields; do not invent missing provenance.

For MPC, identify parties, corruption model, circuit/inputs/output recipient, and the supplied correlations. For a proof system, identify the relation or circuit, field, constraint/domain sizes, public-input/witness sizes, setup/SRS model, proof variant, and prover/verifier configuration. A witness-generation benchmark, proving benchmark, verification benchmark, and batch-verification benchmark answer different questions.

State whether loading, compilation, witness generation, generic or circuit-specific preprocessing, allocation, validation, serialization, network exchange, output release, erasure and deallocation lie inside the timer. Keep nested timers and disjoint components identifiable. If phases change during optimization, compare an unchanged encompassing interval.

## Concurrency and aggregation

Prefer direct elapsed measurement of the intended event sequence. If only component observations exist, define the justified aggregate per repetition before summarizing repetitions. `median(a_i+b_i)` need not equal `median(a_i)+median(b_i)`.

For two party paths, `max(T_A,T_B)` is a party-local cost statistic; it equals a completion-time estimate only under a matching start, scheduling, synchronization, and measurement contract. `max(A_1,B_1)+max(A_2,B_2)` assumes phase barriers that must actually exist. Separately timed expansion plus execution is an additive diagnostic, not a continuous end-to-end wall measurement.

For N jobs, elapsed batch time divided by N is amortized time per job, not the latency of a single job. Summing concurrent call durations measures accumulated call time and contention, not the batch makespan. Distinguish independent-job parallelism, per-party workers, nested kernel pools, test-runner concurrency, and party overlap.

Record detected/process-visible CPUs, requested/configured workers, and observed effective workers when measurable. Label unobserved effective counts unavailable; a configured cap is not evidence that every worker was active. A hardware-derived default is not a measured optimum. Check quotas/affinity and memory limits rather than only host totals. Overlapping party workspaces add to the peak; a workspace budget need not cap total resident memory.

## Repetitions and comparisons

Build before measurement. Choose repetitions/warmups and a statistic appropriate to the task and expected variability; do not carry a fixed count from an earlier project. Retain run order and all observations, including failures and justified exclusions.

For optimization claims, pair or interleave alternatives where feasible and account for thermal/frequency/cache drift and competing load. Rotate multi-configuration order when order effects matter. The median paired ratio and the ratio of separate medians are different estimators; state which is used, with uncertainty when a speedup claim depends on it. Do not call a noisy difference an established improvement.

Fresh-process repetitions repeat process-local initialization. Discarding warmup processes does not warm later new processes; repeated execution in one process is a different experiment. Reusing buffers, keys, SRS data, compiled circuits, or worker pools requires both a matching harness and a permitted reuse model.

Check correctness outside the performance interval when that matches the contract, retaining the result and its scope. Keep checks required by the actual protocol inside the measured execution. A trusted full-output audit may be useful for testing but must not supply information unavailable to the real parties.

## Resource and portability reporting

Separate analytical allocation sizes, allocator-observed memory, and measured peak RSS, with decimal/binary units. Failed OS instrumentation produces unavailable data, not a measured bound. Assess architecture instructions, dependency versions and memory feasibility before attempting a large rerun. Smaller parameters or a software fallback can validate portability without reproducing published throughput or security settings.
