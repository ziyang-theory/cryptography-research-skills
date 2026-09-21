---
name: crypto-benchmarking
description: Design, run, or audit reproducible cryptographic experiments and their timing, communication, memory, and statistical accounting. Use for MPC, zero-knowledge, and correlation-generation benchmarks or evidence-to-table calculations; not for protocol implementation or evaluation prose alone.
---

# Cryptography Benchmarking

Define what the experiment measures before running it. Resolve the actual protocol variant, implementation, workload, setup model, and available hardware from the current project; do not import another project's defaults or security claims.

## Select the work

- For collecting measurements or evaluating an optimization, read [experiments and timing](references/experiments-and-timing.md).
- For bottleneck diagnosis, optimization attribution, batched services, accelerators or distributed scaling, also read [optimization experiments](references/optimization-experiments.md).
- For communication, rounds, workload alignment, or correlation-supply estimates, read [costs and interfaces](references/costs-and-interfaces.md).
- For deriving a table from existing evidence or reconciling paper values, read [evidence and tables](references/evidence-and-tables.md). Source-only arithmetic does not require an expensive rerun.

Load only the references implicated by the request. Optional companions are `crypto-correlation-accounting` for ambiguous output units, `crypto-protocol-implementation` for requested implementation repairs, and `crypto-implementation-evaluation-writing` for authorized evaluation prose. Without them, define the algebraic relation, holdings, dimensions and reversible count conversion using [costs and interfaces](references/costs-and-interfaces.md); map any repair to the governing specification and focused correctness checks; and write only claims supported by the recorded configuration, phases and evidence status.

## Essential distinctions

- Separate correctness validation, empirical performance, correspondence to a protocol, and cryptographic security. Key width, a successful audit equation, and a timing result do not calibrate concrete security.
- State what is supplied and what is timed: trusted or distributed setup, preprocessing, expansion, conversion, proving/evaluation, verification, transport, and cleanup as applicable. A function name such as `online` does not define its dependencies.
- Keep continuous elapsed time, party-local time, CPU work, and sums of separately timed intervals distinct. Do not infer a distributed makespan from unrelated local timers.
- Preserve each value's origin: measured here, rerun, reported by a source, analytically derived, estimated, extrapolated, or unavailable. A formula using a cited rate remains a derived estimate.
- Keep the experimental sampler/configuration distinct from the theorem's distribution. State comparable widths or parameters without asserting matched security unless that assertion is supported.
- Preserve raw observations and failures in a fresh result directory. Check the actual selected tests and executable; zero selected tests is not successful validation.

Return the metric and units, configuration/provenance, commands, correctness status, repetitions/statistic, evidence location, and material limitations. A bounded smoke run is sufficient for a smoke request; report its coverage without implying repeated performance evidence.
