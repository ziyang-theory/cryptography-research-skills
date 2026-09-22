# Costs, workloads and interfaces

## Communication and rounds

Specify logical protocol bits, serialized/framed bytes, or transport bytes. For point-to-point transmitted traffic, sum sends over all included channels and directions; do not add their matching receives again. Broadcast may count once as a logical message or once per recipient on the wire; state the convention. Separate setup key delivery, auxiliary checks and control traffic according to the chosen metric.

Derive finite-instance totals from message inventories before normalizing per gate, constraint, proof or party. Include input/output terms, authentication/check messages, padding, fixed costs, compiler duplication and batching. An asymptotic leading coefficient is not a complete finite-instance count. Challenge vectors, sent PRG seeds and transcript-derived challenges define different transcripts; retain separate variant identities and proof qualifications.

Count causal message layers under the stated convention. Draw the dependency order when exact rounds are contested; local phases, send calls and worker threads are not rounds. Interactive conversion may already be incorporated into later messages; check the schedule before adding or removing a round. Local expansion after setup does not make setup noninteractive or free.

## Workload identity

Use the same computation and interface where possible. For Boolean circuits, verify content hash against the intended fixture, gate types/counts, constants, bit order, input ownership and output semantics, with a known-answer test. Equal nonlinear-gate counts alone do not establish equivalent runtime workloads.

For arithmetic/ZK workloads, compare the relation, arithmetization, field, public inputs, witness preparation, constraints/rows/domain, padding, lookup/custom-gate choices, batch size and output guarantee when relevant. Do not rank different workloads or soundness settings by a single unlabeled time. Distinguish native, recursive, aggregated and batch-verification configurations where they differ.

## Correlation and provider estimates

Define the algebraic output and who holds each component before converting counts. Scalar OLE, VOLE vectors, authenticated products, triples, and programmed/shared-input correlations need not be interchangeable. Matching output counts or field widths does not establish the required interface, setup distribution, or programming ability.

For an estimate using required units n_j and provider rates r_j, `sum_j n_j/r_j` assumes additive supply costs under the stated reuse and scheduling model. If stages overlap or providers share work, this is not a measured pipeline time. Multiplying a published scalar rate into a vector/block/programmed resource requires a justified conversion and its costs. A paper's distributed setup capability does not establish whether setup was included in the published timer.

Keep generated, usable, consumed, discarded and padded counts separate. Account for finite-batch waste and one-time/reusable setup. Do not treat repeated public or deterministic seeds as fresh independent secret correlations. A provider benchmark, a supply estimate and a full protocol run remain three distinct pieces of evidence.
