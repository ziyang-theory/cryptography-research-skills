# Optimization strategy and execution

Use this reference when selecting or implementing optimizations. Techniques are candidates conditioned on the workload, not a mandatory sequence or a ranking of libraries.

## Choose the objective and locate the cost

Resolve whether the request targets single-request latency, sustained throughput, total work, transmitted bytes, peak memory, or a deployment limit. Retain the functionality, security parameters and guarantees as constraints. Identify coordinates that may worsen: a faster batch can consume more memory and increase queueing delay; less communication can require more local expansion.

Use available profiles and phase/message traces to separate computation, serialization, transfers, waiting and allocation. Distinguish an observed bottleneck from a hypothesis needing measurement. Trace causal dependencies: placing two dependent operations into the same send buffer cannot eliminate their dependency. Local operation counts, total bytes and round counts each explain only part of a distributed execution.

Propose the smallest change that addresses the evidence within the requested scope. Broader circuit, primitive or protocol changes can be useful candidates, but require their own semantic obligations from [security preservation](security-preservation.md). Do not present an unmeasured candidate as an established improvement or run a large experiment merely to follow this reference.

## Match execution techniques to the bottleneck

| Bottleneck | Candidate mechanism | Counter-cost or condition to inspect |
| --- | --- | --- |
| Many small exchanges | Batch independent operations from the same causal layer; coalesce messages | Buffering and queueing; transport packing alone does not reduce logical rounds |
| Idle stages or transfer stalls | Overlap independent setup, evaluation, serialization or transfers | Synchronization, intermediate observations, capacity and cancellation |
| Repeated primitive calls or runtime overhead | Batch primitive evaluations, vectorize or use a supported hardware path | Tails, alignment, dispatch, worker overhead and actual input preconditions |
| Large intermediates or allocation pressure | Stream in a public dependency order, reuse dead buffers, recompute selected intermediates | Extra work, liveness/fan-out, secret ownership and peak overlapping allocations |
| Serialization or copying | Contiguous binary batches, compact encodings and fewer intermediate copies | Complete transport bytes and parsing cost; preserve validation and framing |
| Repeated setup or device loading | Cache reusable public tables/bases, pool buffers, keep suitable data resident | Configuration identity, memory pressure, request isolation and permitted reuse |

Generic compression need not shrink pseudorandom payloads. Check actual framing and representation overhead before assuming the cryptographic payload is compressible. Removing a canonicality, range, group or framing check needs a documented invariant covering the relevant adversarial inputs; an honest producer's behavior alone is insufficient.

## Bound concurrency and distinguish lifetimes

Use bounded queues and backpressure when overlapping producers and consumers. Track ownership through completion, failure, cancellation and retry, including in-flight work. A faster producer can otherwise turn a downstream bottleneck into memory exhaustion. Scheduling changes must preserve commitment/challenge dependencies and withholding of outputs or externally visible actions until required checks complete. An asynchronous runtime does not by itself implement security in an asynchronous-network model.

Distinguish reusable setup/public material, consumable correlations and temporary buffers. Cache only what the construction permits, indexed by the relevant parameter or setup identity. Restarting or retrying must not reassign already used one-time material to a different logical operation. Reusing a memory address, a circuit description and a cryptographic mask are different actions; buffer pooling does not authorize correlation or garbled-label reuse. Apply [state and validation](state-and-validation.md) to the affected lifecycle.

Name the parallelism layer: CPU instructions, compiler/runtime vectors, local worker tasks, independent sessions, accelerators or distributed parties. Cryptographic packing is a separate construction choice. Profile scheduling, copying and synchronization overhead before inferring an application gain from a faster kernel.

## Follow the relevant construction

- Read [MPC optimizations](mpc-optimizations.md) for circuits, representations, arithmetic domains, garbling, correlations and oblivious access.
- Read [ZK optimizations](zk-optimizations.md) for relations, witness pipelines, proof kernels, distributed proving and verifier/aggregation costs.

Record the selected mechanism, the replaced cost and added work, preserved or changed contract, focused validation, and measured or still-hypothetical effect. Match the validation and performance evidence to the request; a local kernel result need not claim a complete application speedup.
