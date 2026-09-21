# Optimization experiments

Use the relevant sections when designing or interpreting an optimization experiment. Apply the measurement and security-contract rules in [experiments and timing](experiments-and-timing.md); do not require every diagnostic or sweep for a bounded request.

## Locate the limiting work or dependency

Use profiles of the actual workload and backend when selecting a kernel to optimize; collect a scoped diagnostic if the claimed bottleneck lacks evidence and execution is authorized. Distinguish arithmetic, serialization/copying, memory traffic, transfers, synchronization and queueing. A prover need not be dominated by MSM or transforms; witness generation, hashing, sumcheck or relation encoding can dominate instead.

Trace causal dependencies and overlap. The component with the most accumulated work need not limit completion time; a serial dependency or saturated pipeline stage can dominate. Packing messages does not remove a dependency between operations. Treat additive compute/bandwidth/latency models as hypotheses about a schedule, then compare their predictions with executions. State which objective matters: request latency, sustained throughput, total work, bytes or peak memory.

## Attribute the improvement

State what expensive operation the change removes and what replaces it. Use a controlled component comparison to test that mechanism, and measure the encompassing pipeline when claiming application improvement. A faster kernel may expose another bottleneck or add conversion, transfer or synchronization costs.

Use selective ablations when multiple changes could explain a gain. Hold workload, security contract and resource budgets fixed where possible; disclose confounds and test interactions when the combined change is central to the claim. Choose batch, network or memory regimes that distinguish plausible explanations, rather than requiring an exhaustive sweep. A profile localizes work; it does not alone establish the causal benefit of a proposed optimization.

## Batches and services

For a service claim, record arrival workload, admission/concurrency limits, batch formation and queue policy. Measure request completion from arrival, including queueing and batch-fill delay, alongside completed useful outputs per unit time. Report a latency distribution when supported by enough requests; separate timeouts and rejected requests from successes.

Distinguish a finite preloaded batch from sustained service. Growing backlog can conceal overload during a short throughput run. Identify startup, pipeline fill/drain, reusable prepared state and recurring preprocessing or refill costs. A batching gain can trade lower per-output work for longer waiting time and greater memory use.

## Accelerators and distributed execution

For CPU/GPU comparisons, include or separately expose host preparation, public-parameter loading, representation conversion, host-device transfers, device work and result return. Synchronize at the declared completion event: asynchronous launch duration is not completed device execution. Account for host and device peak memory and the prepared state behind resident-data measurements.

For distributed scaling, distinguish fixed total workload with more resources from workload growth with more resources. Report coordinator/client work, partitioning, communication, final collection and load imbalance where they affect completion. Compare observed wall time with aggregate resource consumption under explicit units and a comparable baseline budget. Greater capacity or lower latency need not reduce total work; multiplying a single-worker rate by worker count is a model, not an observed cluster run.

Label hardware synthesis and simulation separately from device measurements. Retain the modeled target, frequency, memory and transfer assumptions; simulated cycles or synthesized area do not establish measured silicon throughput or power.

## Proof and application boundaries

When comparing proof-generation or aggregation strategies, track witness preparation, proving, aggregation/final compression, verifier work and required public data separately. Identify the accepted output: original proofs, an aggregate, an accumulated relation instance or a final proof. Smaller proof bytes or verification cost can require more production work and need not reduce public-input, publication or data-availability costs. Evaluate the costs implicated by the application claim without attributing unrelated service guarantees to the proof.
