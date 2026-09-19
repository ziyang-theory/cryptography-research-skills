---
name: crypto-correlation-accounting
description: Define, normalize, and compare OT/OLE/VOLE, authenticated-correlation, triple, and PCG output counts or throughputs by algebraic relation, field, grouping, setup requirements and costs, denominator, and evidence provenance. Use when “correlation,” lane, entry, product, vector, block, call, or rate units are ambiguous; not for implementing a PCG, running a benchmark alone, or drafting comparison prose by itself.
---

# Cryptographic Correlation Accounting

Do not compare rates until each output unit has an algebraic meaning and a complete denominator. A shared word such as “correlation” does not make two primitive interfaces or grouped outputs interchangeable.

For theoretical relations, resource counts, or logical expansion factors, work from the definitions and formulas; no implementation or measurements are required. Apply the throughput guidance only when a rate is requested or used. Optional companion skills do not block this workflow when absent.

## Authorization and routing

An explanation, normalization, source audit, or fit calculation is read-only. Change benchmark code, profiles, or manuscript tables only within the user's authorized scope.

- Read [references/relation-and-rate-method.md](references/relation-and-rate-method.md) whenever two constructions, grouped outputs, or throughput conversions are involved.
- When available, use `crypto-literature-evidence` to establish paper-exact relations, variants, call counts, and whether a value is reported or derived. Otherwise inspect the primary source directly.
- Keep implementation, parameter selection, and security auditing separate from count normalization; use a relevant dedicated skill when available and the requested task needs it.
- Use `crypto-benchmarking` when available and measurement design or execution is requested. Use `crypto-prior-work-comparison` when available for comparison prose after the relation and count definitions are stable.

## Core invariants

- Write the defining relation, domain/field, party holdings, randomness, dimensions, and shared/global keys before assigning a count.
- Count one reconstructed algebraic relation once, not once per party share, unless the requested metric explicitly counts shares or stored elements.
- Keep count levels separate: scalar lane/entry/product, coordinate, vector, block, batch, ideal-functionality call, PCG seed pair, and protocol execution.
- State field or bit width next to every scalar rate. Equal scalar counts over different domains do not imply equal bytes, computation, security, or usefulness.
- Distinguish a protocol's block width from an encoder's internal block, stripe, chunk, or packing parameter.
- A block with a shared multiplier/key contains multiple scalar relations but not necessarily independent primitive instances. State the coupling.
- Distinguish private PCG-key bits, public parameters, setup traffic, serialized bytes, and logical output-share bits when reporting expansion ratios. Name the numerator, denominator, party aggregation, and excluded material.
- Count requested and padded outputs separately. Preserve per-call vector lengths and multiplicities instead of flattening them without a reversible formula.
- Name the timed phase and included operations: setup/seed generation, local expansion, programming, audit/validation, consumption, or end to end. Zero-interaction expansion is not zero-cost setup.
- Define pair time and concurrency. `max(T_0,T_1)` from separately timed parties is a model, not a measured concurrent wall time.
- Label every rate author-measured, inherited/cited measurement, source-reported analytical, locally measured, independently rerun, derived, estimated/extrapolated, projected, or unavailable. Never say a paper “reports” a quotient you derived.
- Do not infer whole-instance or protocol throughput by dividing a scalar rate unless independence, linear scaling, call shape, overlap, and excluded work are justified.

## Expected result

Return the relevant relation sheet, reversible count hierarchy, evidence status, and setup/security qualifications. When the task concerns throughput, also give the exact rate equation and timed operations before any normalized rate comparison. A compact sheet is sufficient for a simple explanatory question. Distinguish a descriptive ratio of unlike counters from a speedup for a common downstream workload. Prefer explicit units such as `F_(2^40) scalar block-VOLE entries/s`, `F_(2^128) scalar programmable-OLE products/s`, or `complete product-graph vector positions/s` over bare `correlations/s`.
