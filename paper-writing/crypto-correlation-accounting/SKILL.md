---
name: crypto-correlation-accounting
description: Define and compare cryptographic correlation counts, PCG expansion ratios, and throughput units by algebraic relation, domain, grouping, and denominator. Use when lanes, entries, blocks, calls, or correlation rates are ambiguous; not for protocol implementation or benchmark execution alone.
---

# Cryptographic Correlation Accounting

Give each counted output an algebraic meaning before comparing counts or rates. The word “correlation” does not make different interfaces interchangeable. Theoretical counts and expansion factors need definitions and formulas, not benchmark runs.

## Normalize the unit

- Specify the relation, domain/field, party holdings, dimensions, randomness, and shared keys or multipliers. Count one reconstructed relation once unless the metric explicitly counts shares or stored elements.
- Preserve the hierarchy from scalar entries through coordinates, vectors, blocks, batches, provider calls, and protocol executions. State coupling and requested versus padded outputs; scalar relations sharing a key need not be independent instances. An encoder's internal block is not automatically the primitive's block width.
- For expansion ratios, name numerator, denominator, party aggregation, and exclusions. Keep logical output-share bits, private key bits, public parameters, setup traffic, and serialized storage distinct.
- For throughput, state the exact rate equation, field/bit width, timed phase, concurrency, and aggregation rule. A maximum of separately measured party times is a model, not measured concurrent wall time. Zero-interaction expansion does not remove setup cost.
- Preserve evidence status: reported or derived, measured or modeled, original or inherited. Scalarization alone does not justify protocol throughput; check consumption shape, coupling, scaling, overlap, and excluded work. Use “speedup” only for a comparable workload.

Read [relation and rate method](references/relation-and-rate-method.md) for grouped outputs, cross-construction comparisons, or rate conversions. It contains optional worksheets and equations; use only the fields the question needs.

Return the defining relation, reversible conversion, assumptions, and evidence status, adding timed operations when rates are involved. Prefer an explicit unit such as field-specific scalar VOLE entries/s to bare correlations/s. Counting does not establish security or choose parameters. Change code or tables only within the requested scope; optional literature, benchmarking, or writing skills do not block this self-contained calculation.
