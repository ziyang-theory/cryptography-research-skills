---
name: crypto-benchmarking
description: Design, run, or audit cryptographic experiments and evidence-to-table calculations with explicit timing, communication, memory, and statistical accounting. Use for measurements and their interpretation, not protocol implementation or evaluation prose alone.
---

# Cryptography Benchmarking

Define the measured object, included operations, units, and evidence source before running or comparing experiments. Resolve the actual protocol variant, workload, setup and hardware from the project.

## Workflow

1. Fix the measurement contract: construction/configuration, workload, prepared state, timer events, concurrency, cost aggregation, repetitions and statistic. Distinguish measured facts from unknown configuration details.
2. Collect or inspect the evidence needed for the request. Preserve raw observations, failures and source/build identity; derive summaries separately. A smoke request needs bounded functional coverage, while a performance claim needs repetitions and uncertainty appropriate to that claim.
3. Establish correctness coverage for the selected configuration. When executing checks, confirm the intended tests and executable ran; for reanalysis, report the retained validation evidence and gaps. Keep protocol-required checks inside measured execution; an external diagnostic audit is a different operation.
4. Compute each execution's metric before aggregating repetitions. Reconcile formulas, units and table values, then report what the evidence supports.

Keep continuous elapsed time, party-local time, CPU work and sums of separately timed intervals distinct. Label each value as measured, rerun, inherited, derived, estimated, extrapolated or unavailable. A provider-rate calculation is an estimate, not a measured pipeline.

Functional validation, protocol correspondence, empirical performance and cryptographic security are separate conclusions. Preserve differences between the implemented sampler/configuration and the theorem's distribution; matching parameter widths does not establish matched security. Reanalysis need not trigger an expensive rerun or manuscript edits.

## Review, correct, and recheck

Before delivery, review the measurement contract, raw evidence, calculations, and resulting claims. For a substantial experiment or reanalysis, use a separate reviewer when available; supply the original request, configuration, observations, formulas, and results. A delegated reviewer returns findings without starting another review chain. For a small calculation or unavailable delegation, perform a focused self-review without claiming independence.

Adjudicate concrete discrepancies, preserve raw records, correct derived results, and recompute affected summaries and comparisons. Collect additional measurements only to address a concrete defect or evidence gap, within the authorized experiment scope. Preserve prior observations and record why additional measurements were needed. Use one review-and-revision pass by default; repeat for an unresolved discrepancy or new evidence. No correction is a valid finding. Finish with supported results and any missing evidence or failed checks; do not rerun until a preferred performance result appears.

## References by task

- [Experiments and timing](references/experiments-and-timing.md): collecting measurements, comparing optimizations, repetition and resource accounting.
- [Optimization experiments](references/optimization-experiments.md): causal attribution, services, accelerators and distributed scaling.
- [Costs and interfaces](references/costs-and-interfaces.md): communication, rounds, workload alignment and correlation-supply estimates.
- [Evidence and tables](references/evidence-and-tables.md): reanalysis, provenance and manuscript-value reconciliation.

Load the applicable reference sections. For a calculation, return the formula, units, assumptions and result. For an experiment or project-data review, also report configuration/provenance, commands and evidence locations, correctness coverage, statistics and material limitations as relevant.
