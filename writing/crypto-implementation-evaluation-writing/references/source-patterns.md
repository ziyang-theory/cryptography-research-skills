# Evaluation patterns from eight cryptography papers

> **Source status:** These are retained earlier reading notes, not findings independently reverified in the 2026-09-14 skill update. Keep this collection separate from the supplied 30-paper corpus. Check the exact primary version before reusing locators, numerical claims, or reported defects; see [evidence sources](evidence-sources.md).

These notes distinguish the evidence modes represented by the source set. Page references are PDF pages; ASHIV20's printed proceedings pages are 1592-1603. Recheck the exact paper version before reusing numbers.

## Evidence modes in the sample

| Paper | Useful locations | Evaluation mode and lesson |
| --- | --- | --- |
| WRK17 | Section 7 pp.12-18; Tables 4-10; Figure 3 | Full empirical protocol evaluation. States implementation components, security parameters, CPU-instruction optimizations, thread placement, circuits, LAN/WAN environments, and phase-separated times. It reruns a baseline, excludes base OTs consistently, reports larger workloads and scaling, and defines directional communication. Modernize it by adding commit/toolchain, warmups, dispersion, and raw-data provenance. |
| KRRW18 | Section 6 pp.20-22; Tables 2-3 | Concrete analytical evaluation without a new implementation. Own communication values are formula-derived; computation uses hash-evaluation counts and reported component timings. Useful model only if every claim is labeled calculated or inferred. |
| DPSZ12 | Appendix D pp.40-45 | Security-driven parameter derivation followed by narrow SHE microbenchmarks. Gives hardware and both total and amortized per-field-element timings, then discusses uncertainty in mapping the lattice hardness parameter to bit security. These are core-operation measurements, not end-to-end MPC timings. |
| ASHIV20 | Section 7, PDF pp.10-12; Figure 8, PDF p.13 | Full C++ implementation narrative covering primitives, hardware, security parameters, workload design, offline/online and sender/receiver costs, communication, time, and peak memory. It exposes OOM limits and non-optimized code. It also uses an explicitly insecure reduced-round AES diagnostic and unimplemented memory/reuse projections, which must remain visually distinct from secure measurements. |
| BCGI18 | Section 5 pp.18-25; Tables 1-4 | Parameter optimization, operation-based runtime estimates from literature throughput, one actual conservative component benchmark, and derived setup projections. It clearly says the complete runtime estimates are not from an implementation and identifies ignored cache effects. Useful model for an honest estimate section, not an end-to-end benchmark section. |
| HKNOS25 | Section 7 pp.22-23; Appendix H pp.47-49 | Formula-derived concrete communication comparison only. No code, runtime, or experimental environment. Call it concrete cost analysis, not implementation or performance benchmarking. |
| LXYY25 | Tables 2-3 p.6; Section 9.3 p.59 | Implementation based on a baseline codebase, same-machine rerun, same parameters, CPU/RAM, and code link. It explicitly gives formulas that extrapolate a measured small run and estimated seed communication to `10^9` triples. The displayed large-workload results are therefore mixed measured/derived evidence. |
| MMST25 | Section 5 pp.21-26; Tables 1-2 p.25 | Strong section decomposition: implementation/optimizations, parameters, analytical cost, then performance. Names libraries, two AWS machines, LAN, resources assumed pre-sampled, phase-specific metrics, asymmetric seed sizes, operation counts, measured runtimes, starred estimates, and OOM cells. Missing revision, compiler, network details, repetitions, and dispersion remain useful reminders. |

## Strong combined architecture

The sample supports this adaptable sequence:

1. **Implementation scope:** exact variant, artifact, primitives, and unimplemented alternatives.
2. **Optimizations:** changes that affect messages, operations, memory, or parallelism.
3. **Security and parameters:** estimator/proof basis and any uncertainty.
4. **Analytical cost:** formulas and operation counts used to predict trends.
5. **Experimental setup:** machines, software, network, concurrency, workloads, and trial procedure.
6. **Results:** phase-separated time, communication, memory, failures, and scaling.
7. **Comparison:** same-machine rerun where feasible, otherwise visibly inherited or modeled values.
8. **Limitations and reproducibility:** exclusions, ideal resources, OOM/timeouts, projections, commands, and raw evidence.

This is not a mandatory heading list. Collapse sections when the evidence is small; retain the distinctions.

## Useful presentation patterns

- WRK17 defines phases before showing results and carries the same boundaries through all tables.
- ASHIV20 reports both crossover points and regimes where its computation is worse.
- BCGI18 pairs an optimistic operation-rate estimate with a slower measured proxy as a conservative check.
- LXYY25 distinguishes a published baseline value from a local rerun on the same machine.
- MMST25 marks estimated cells with `*` and OOM with an em dash in the main table rather than silently dropping them.
- DPSZ12 places parameter derivation next to the microbenchmark so the security/performance dependency remains visible.

## Source-derived validation warnings

- WRK17's reviewed PDF has stale/conflicting abstract and body AES totals. Reconcile the final manuscript globally after updating results.
- ASHIV20 Figure 8's overall caption does not accurately describe all five panels. Check every panel title, legend, security status, and prose reference against the caption.
- BCGI18 labels near-local-minimum parameter search results as optimal in a caption and contains an apparent arithmetic mismatch in a derived setup total. Calibrate optimization language and machine-check calculations.
- HKNOS25 has table-header/prose-ratio inconsistencies even though its comparison is analytical. Formula-derived tables require the same QA as measurements.
- LXYY25 and MMST25 show why output-count normalization matters: large headline workloads may be extrapolated, while only smaller instances were run.

## Common missing fields in the sample

No single source consistently reports all of: commit, dependency revisions, compiler and flags, OS, thread policy, warmups, independent repetitions, aggregation statistic, dispersion, raw results, LAN latency/bandwidth, and failure thresholds. A new section should add the fields that materially affect reproducibility and the claim.

## What the sample does not justify

Do not infer that every cryptography paper needs an end-to-end implementation. Analytical cost analysis and component microbenchmarks are legitimate when labeled precisely. The required invariant is correspondence between the claim and evidence class.
