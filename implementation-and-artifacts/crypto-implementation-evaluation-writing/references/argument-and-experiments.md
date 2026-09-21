# Building the empirical argument

Use this reference when organizing a substantial section, planning evidence for a claim, or reviewing baseline fairness and interpretation. It proposes decision criteria, not authorization to execute experiments. For metric definitions and evidence labels, use [evaluation-method.md](evaluation-method.md).

## Connect claims to observations

Connect each important claim to an observation and a useful controlled comparison. Identify plausible confounds and what would require narrowing the claim.

| Proposed claim | Informative evidence | Interpretation to avoid |
| --- | --- | --- |
| Lower communication improves runtime | Bytes and latency under controlled network settings, with computation profiled | Fewer bytes imply faster execution in every regime |
| A particular optimization causes a gain | Same-codebase ablation holding other changes fixed | Attributing a combined compiler/library/protocol change to one mechanism |
| Scaling with party count | Party sweep with workload, threshold, topology, and CPU/thread allocation documented | Attributing a new remote region or extra cores solely to party count |
| Setup amortizes well | First-call and batch-size costs, including fresh work and unused outputs | Reusing consumable preprocessing or calling batch-average time request latency |
| A compiler selects well | Predicted versus measured costs, selection overhead, and actual executions | Treating an unvalidated cost model as measured performance |
| A complete application is useful at a stated scale | Whole-task cost, machine budget, and correctness/quality at that scale | Promoting an iteration, subset, reduced-precision task, or projection to the full job |

Choose the smallest informative set of experiments. A relevant startup regime, unfavorable network regime, or observed memory limit can delimit a claim. Do not require every paper to run every sweep, and do not describe an unexplored regime as either an established success or an established limit.

## Compare like with like

Compare under the contract recorded in [evaluation method](evaluation-method.md). Comparisons across different guarantees can be useful when stratified clearly; they do not establish a win under identical guarantees.

Prefer matched reruns when available and authorized. Record baseline revision, patches, dependencies, tuning range/objective, and effort. When isolating protocol novelty, consider a baseline that receives applicable engineering improvements too. Otherwise disclose the combined effect instead of assigning the entire gain to the new construction.

Separate two comparison questions:

- **Protocol on a common workload:** Hold the circuit or arithmetic computation and other relevant conditions fixed to compare protocol implementations.
- **Whole system on the same application:** Allow each compiler/framework to optimize the application while preserving semantics and quality. This measures the integrated system and does not isolate the cryptographic protocol.

CPU-frequency rescaling is a model, not proof of hardware equivalence. Preserve source conditions for quoted and estimated baselines.

## Explain mechanisms with evidence

Connect an optimization to the operation it changes and then to the affected metric. A controlled ablation can isolate its effect; a profile can identify a dominant component but may leave competing explanations. Use “is consistent with” for a supported but non-isolated mechanism and “we hypothesize” for an untested explanation; name the missing test when material.

Vary axes implicated by the claim while controlling other factors: workload size/depth, representation, field, batch, parties/threshold or network. Disclose deployment changes that confound these axes.

A model such as local computation plus transfer time plus sequential latency assumes a particular schedule and bottleneck. Overlap, pipelines, and heterogeneous links can invalidate simple addition. Validate predictions against observed executions where possible, report prediction error, and keep subsequent predictions labeled as estimates. If validation is absent, state that limitation.

For services, pair throughput with request completion including queueing/batch-fill delay, arrival/concurrency regime and backlog behavior. A preloaded batch does not demonstrate sustained service. For accelerators, include preparation and transfers when claiming a pipeline gain.

For distributed scaling, distinguish fixed total workload with more resources from workload growth with more resources. Explain coordinator work and imbalance when they limit completion, and pair elapsed-time claims with the aggregate resource budget. More capacity, lower elapsed time and lower total work are distinct conclusions.

## Adapt the section to the contribution

- **Protocol or primitive:** Establish implemented scope and security parameters, present the central measured or analytical result, then use phases, ablations, scaling, and tradeoffs to explain it. Integration is needed for an application-performance claim; a precisely scoped primitive result can stand on its own.
- **Proof system:** Align the relation and representation, security/soundness target, setup and oracle assumptions, and public-input/witness sizes. Separate key generation, witness generation, proving, verification, proof size, and key/CRS storage. Microbenchmarks of FFT, MSM, hashing, or field arithmetic support kernel claims; they do not alone measure a prover. Distinguish a single proof, many independent proofs, aggregation, and recursive composition.
- **Framework or compiler:** State supported programs, representations, backends, and security settings. Separate compilation, optimization/search, setup, and secure execution. Validate the cost model when it supports selection claims. Structural proxies (gate count, depth, cycles) and runtime answer different questions. Development-time anecdotes do not establish a productivity study.
- **Application:** State task, trust/leakage, data/model versions, precision, and correctness or quality target. Distinguish inference, an iteration, convergence, and a complete job. For numerical work, compare behavior with an appropriate plaintext reference. For PSI, include set-size asymmetry, item width, and relevant distributions. Changing precision, model, or quality target is a tradeoff to report separately from a protocol speedup.
- **Concrete estimate:** Separate measured kernels, exact operation counts, modeling assumptions, and unimplemented construction/application costs. Do not force an empirical narrative onto an analytical result.

These are ordering options. Keep the main result and its material qualifications in the main text; detailed configuration matrices and commands may go in an appendix or artifact.

## Source examples

For optional examples, use the [source routes](evidence-sources.md): P15 for protocol versus engineering improvements; P10/P23 for phases and granularity; P02/P27 for heterogeneous configurations; P19/P25 for compilers; P03/P13/P21 for application quality and cost; P26/P24 for modeled costs. These are pointers into supplied notes, not fresh primary-source verification or mandatory citations in the user's paper.
