# Source patterns from eight cryptography papers

These retained reading notes summarize writing patterns, not authoritative current rankings or newly verified paper claims. They are optional examples; using the method requires neither these papers nor local copies of them. Page references are PDF pages; they also match printed pages except ASHIV20, whose printed proceedings pages are 1592-1603. Recheck the exact paper version before reusing a number or attribution.

## Paper-by-paper patterns

| Paper | Useful locations | Comparison pattern |
| --- | --- | --- |
| WRK17, *Authenticated Garbling and Efficient Maliciously Secure Two-Party Computation* | abstract p.1; Tables 1-2 pp.2-3; Section 1.1 pp.3-4; Section 7 pp.12-18 | Builds a taxonomy of protocol families, defines function-independent, function-dependent, and online phases, and separates asymptotic from measured comparisons. Reruns one baseline on the same hardware, inherits another under matching hardware, labels a back-of-the-envelope comparison for an unimplemented protocol, and declines an end-to-end ranking when preprocessing is unreported. It explains ratios through garbled-circuit count, per-gate work, and round depth. |
| KRRW18, *Optimizing Authenticated Garbling for Faster Secure Two-Party Computation* | Table 1 pp.2-3; Section 6 pp.20-22 | Presents two variants optimized for different phases. Separates maximum one-way from summed two-way communication and single from 1024-execution amortization. New costs are calculated rather than measured; computation is compared by aligned hash-evaluation counts. It preserves a tradeoff where slightly smaller prior totals lack function-independent preprocessing. |
| DPSZ12, *Multiparty Computation from Somewhat Homomorphic Encryption* | Section 1.1 pp.2-4; Appendix D pp.40-45 | Compares asymptotic online work and preprocessing operations while stating field and security regimes. Calls one FHE-based alternative theoretically incomparable, then names the practical tradeoff. Concurrent work is organized by objective and computation domain rather than chronology alone. Appendix D treats hardness-estimation uncertainty explicitly. |
| ASHIV20, *Is the Classical GMW Paradigm Practical?* | Section 1.1, PDF pp.3-4; Section 7.1, PDF pp.10-12 | Groups prior work by technique and first compares qualitative properties: interaction, offline participation, reuse, selective failure, and random-oracle/Fiat-Shamir scope. Quantitative discussion returns to the same axes and reports crossover points, including regimes where the implementation is slower. |
| BCGI18, *Compressing Vector OLE* | Sections 1.1-1.3 pp.2-5; Section 5 pp.18-25; NIZK comparison p.34 | Compares rate, local preprocessing, malicious-security amortization, setup strength, and interface rather than only running time. Compares its own primal/dual variants as a seed-size versus computation tradeoff. Leads the NIZK comparison with what the construction does not achieve before stating its repeated-proof advantage. |
| HKNOS25, *Multiparty Garbling from OT with Linear Scaling and RAM Support* | Table 1 p.2; Section 7 pp.22-23; Appendix H pp.47-49 | Uses a feature/asymptotic landscape table, then a concrete formula-derived table for a fixed AES circuit across party counts. Discloses different corruption thresholds and broadcast assumptions. The prose is organized by total communication, garbled-circuit size, and break-even regimes. There is no implementation benchmark. |
| LXYY25, *Efficient Pseudorandom Correlation Generators for Any Finite Field* | Tables 1-3 pp.5-6; Section 9.3 p.59 | Normalizes PCGs by field, communication, computation, programmability, and assumption. Concrete tables distinguish a prior reported value from a same-machine rerun and define point-to-point, broadcast, per-party, and localhost metrics. Headline large-workload values are extrapolated from smaller measurements under displayed formulas. |
| MMST25, *Pseudorandom Correlation Generators for Multiparty Beaver Triples over F2* | Section 1.1 pp.3-5; Section 5.4 pp.24-26 | Separates comparisons with a direct baseline and concurrent work. Decomposes the latter into assumptions, seed generation, seed size/rate, and expansion time, explicitly conceding where the concurrent construction is faster. States when comparison is incomplete because a phase was not implemented. |

## Reusable structures

### Landscape then close comparison

Use a compact feature/asymptotic table to define the design space, then a separate concrete table for aligned configurations. WRK17, HKNOS25, and LXYY25 illustrate this two-layer structure.

### Split winners

Name the winner per axis and regime. KRRW18 and MMST25 are useful models: they claim improvements while retaining the prior work's advantage or missing capability in the same discussion.

### Crossover analysis

Report where a scaling advantage becomes concrete rather than showing only a favorable endpoint. ASHIV20 and HKNOS25 organize result prose around such ranges.

### Honest non-comparison

If a baseline omits a phase or lacks an implementation, give an analytical count or bound with assumptions, or state that an end-to-end comparison is unavailable. WRK17, KRRW18, BCGI18, and MMST25 use variants of this pattern.

## Source-derived consistency warnings

These examples motivate verification; they are not templates to imitate.

- WRK17's abstract AES totals differ from Tables 1/6 and Section 1.1 in the reviewed PDF. Always reconcile abstract, body, and final table values.
- HKNOS25 Table 2's two rightmost garbled-circuit headers appear swapped: the prose ratios and Appendix H formula identify the displayed `200` value as the authors' construction, not the labeled GLM column. A total-cost ratio sentence labeled `n=512` instead matches the `n=1024` row. Check headers, ratios, row labels, and formulas together.
- BCGI18 contains at least one derived-total arithmetic mismatch in its setup estimate. Machine-check every displayed derivation.
- A table that mixes broadcast and point-to-point channels, honest- and dishonest-majority thresholds, or MB and MiB can still be useful, but only with adjacent qualifications and no unscoped winner claim.

## What the sample does not justify

The papers are exemplars, not a statistical survey of all cryptography writing. Do not universalize their section order, baseline set, or preferred metrics. Reuse the decision principles: align the claim, expose provenance, preserve tradeoffs, and verify internal consistency.
