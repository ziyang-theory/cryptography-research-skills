# ZK optimizations

Use this reference for relation compilation, witness generation, proving, verification or distributed proving. Fix the proof interface, setup, assumptions and deployment before choosing a backend or acceleration technique.

## Preserve the relation while reducing its cost

Separate witness generation from the constraints checked by the proof system. Optimize repeated decompositions/range checks, non-native arithmetic, memory arguments and duplicated work only when the resulting constraints still enforce the intended relation for every allowed adversarial witness. An invariant of the honest witness generator is not enough to remove a constraint. Track public-input encoding and the mapping between old/new witness representations, including whether every intended valid statement remains provable.

Use a backend-aware cost model: rows/constraints, polynomial degree, domain padding, witness columns, lookups and table representation, commitments and memory. Custom gates or lookups may reduce rows while adding degree, table, commitment or consistency costs. Distinguish a structured conceptual table from one that must be materialized. Validate representative gadgets, malformed witness assignments and relevant range/encoding cases; passing honest proofs alone does not establish relation equivalence.

For hash choices, distinguish hashing inside the proved computation from transcript or commitment hashing used by the proof system. A circuit-friendly primitive can be a useful design choice, but an application that specifies a particular hash cannot silently substitute another. Retain the primitive's parameters, encoding/domain separation, assumptions and application compatibility. Follow [security preservation](security-preservation.md) for construction changes.

## Accelerate the actual prover pipeline

Profile witness/constraint preparation, proving stages, public-parameter loading, memory and transfers separately. Do not assume every prover is dominated by multiscalar multiplication (MSM) and polynomial transforms; sumcheck, hashing or other backend operations may dominate.

For the measured kernels, candidates include balanced MSM buckets, window tuning, contiguous layouts, parallel reductions, reusable public bases/transform constants and bounded CPU/device overlap. Window sizes, recomputation and precomputation trade work against memory. Include transfers, synchronization and scratch/buffer lifetimes when assessing integration. Public-data caching does not permit witness-dependent buffers or stale contents to cross request ownership. Zero knowledge against the verifier does not establish resistance to observable secret-dependent branches, bucket accesses or prover timing.

## Distinguish distributed-prover objectives

State whether workers may see witnesses, deviate or collude, and what a coordinator sees. Scaling computation/memory, protecting a shared witness, identifying faulty workers and guaranteeing completion are separate objectives. Partitioning work across servers does not itself provide privacy or malicious security. Identify the actual sharing/packing, threshold, preprocessing, worker checks, abort and recovery contract before using a distributed backend.

Partitioning and hierarchical aggregation can shift the bottleneck to redistribution, transfers or the coordinator. Compare completion time with total work and memory across workers; reducing time by buying more machines need not reduce aggregate cost. Treat virtual parties simulated inside an MPC-in-the-head prover separately from actual distributed workers. Changing an interactive/private-verifier proof into a public non-interactive application requires a matching construction, not an execution flag.

## Select the verifier or application objective

Distinguish the interfaces and their costs:

| Mechanism | Intended effect and qualification |
| --- | --- |
| Batch verification | Share verification work across proofs; original proof objects generally remain |
| Proof aggregation | Produce a proof about a collection; account for aggregation work and required public inputs/data |
| Recursion | Prove a verifier's computation inside another proof; include verifier-circuit and outer-proof costs |
| Folding | Combine relation instances; establish what final proof, compression and zero-knowledge steps the application still needs |

For a proof service, include queueing, witness preparation, proving, transfers and integration at the requested scope. For blockchain use, include final proof size, verifier work and required public-data publication alongside off-chain work. A smaller final proof does not establish less total work, data availability, timely inclusion, consensus liveness or recovery from unavailable workers. Those claims need their own mechanisms and evidence.
