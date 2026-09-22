# Relation and rate method

## 1. Relation sheet

Complete one sheet per primitive or benchmark row:

| Field | Record |
| --- | --- |
| Name and variant | Source-defined primitive and version |
| Algebraic relation | Equation for one scalar output unit |
| Domain | Base/extension field, ring, bit width, encoding |
| Party holdings | Every input, key, mask, and output share |
| Shared structure | Global delta/key, shared multiplier, reused vector, coupling |
| Dimensions | Coordinates, vector lengths, block widths, edge set, padding |
| Invocation shape | Calls, batches, multiplicity, requested versus generated outputs |
| Consumption | Downstream functionality, protocol step, or workload served by the outputs |
| Validity state | Candidate, checked, authenticated, usable for which consumer/key/epoch, or consumed |
| Setup | Seed establishment, trusted/ideal resources, programmability, reuse |
| Timed work | Exact included expansion/programming/audit/consumption phases |
| Evidence | Author-measured, inherited/cited measurement, source-reported analytical, local measurement, rerun, derived, estimated, projected, N/R |
| Security | Computational/statistical parameters, actual sampler/ensemble, and unproved/diagnostic status |

Use the source's notation first, then introduce a normalized symbol only if it makes the conversion reversible. For a narrow explanation, retain only the implicated rows; the full worksheet is for multi-construction or publication-facing comparisons.

Canonical scalar relations include the following, subject to the source's party/role convention:

- VOLE: `v = b + a Delta` over the stated field;
- subfield/sVOLE: the designated coordinate input (for example, `a`) lies in a stated subfield, often one bit, while the key, masks, and tags lie in the specified larger field;
- block variants: a coordinate contains several scalar relations coupled by a shared multiplier or key;
- programmable OLE: additive output shares reconstruct selected coordinatewise products of programmed vectors.

These are normalization aids, not universal interfaces. Reproduce the source's exact syntax, dimensions, and party holdings before using them.

## 2. Count hierarchy

For a block relation with `L` coordinates and width `B`, a scalarized count may be `L B`, but report both levels. If widths vary by call,

```text
scalar outputs = sum_j L_j B_j
coordinates    = sum_j L_j
average width  = scalar outputs / coordinates
```

For a programmable product graph with edge set `Q` and per-edge vector length `n_q`,

```text
scalar products = sum_(q in Q) n_q.
```

Do not replace this by `n |Q|` when edge lengths differ. A complete graph position, one edge vector, and one scalar product are three different units.

Distinguish one ideal invocation from its concrete provider calls. Co-batching several short vectors may preserve the desired distribution or may alter coupling, padding, and startup cost; do not assume equivalence solely from equal scalar counts. Count extra authentication, input, or output coordinates from the live consuming interface rather than a mnemonic such as one triple per gate.

For a protocol consuming several primitive families, keep a vector of counts `(c_1,...,c_k)` until a concrete cost model is fixed. Adding unlike counts produces no meaningful “total correlations.”

### From raw generation to usable inventory

Use this ledger when comparing a generator with a consumer. Define the counted relation and grouping first; these are overlapping stages, not quantities to add:

| Count | Meaning to fix |
| --- | --- |
| Raw | All generated units, including padding or test material if generated in the same unit |
| Candidate | Units eligible for the intended validation or conversion after initial filtering |
| Checked | Retained outputs after the specified completed checks; identify the acceptance and authentication guarantees |
| Usable | Units admitted to the specified consumer interface, including required checks, key/epoch, grouping, and timing |
| Discarded | Units permanently unavailable, with padding, failed checks, and destructive test/sacrifice use separated |
| Consumed | Units irreversibly spent by the downstream workload; keep validation consumption separate |

State whether counters are cumulative or current inventory. Some interfaces require no checks or authentication, while others release a whole batch only after one check; do not invent independent per-entry acceptance. A tag being present is different from the required verification having completed. Record the authentication key context, sharing, pending checks, and permitted reuse.

Algebraic relation satisfaction alone does not establish compatibility. Point to the generator guarantee and the consumer's required joint distribution, adversarial interface, and release time. Key coupling, auxiliary generator state, or a static-versus-adaptive corruption mismatch can prevent substitution even when every equation holds. Accounting should expose an unresolved compatibility premise rather than certify it. Count further authentication, conversion, checking, and coordination resources needed to reach the claimed usable state.

**Hypothetical inventory example, not a security construction or measurement.** Count one triple as one shared relation `c = ab` over a fixed field, together with the consumer's authentication data; do not count its elements or parties' shares as separate triples. Suppose a pipeline generates 1,024 raw triple units, removes 64 padding units, and spends 192 of the 960 candidates as destructive test material. Assume a separate argument establishes consumer compatibility, and its checks admit the remaining 768 authenticated triples: 512 under key context `K` and 256 under `K'`. A workload needs blocks of 128 triples under `K`. It can use four blocks, not six; the `K'` inventory cannot simply be merged into a `K` call. After consuming three blocks:

```text
raw = 1,024; candidates = 960; checked = 768
usable produced for this workload = 512; consumed = 384
discarded = 64 + 192 = 256
remaining inventory = 128 under K + 256 under K' = 384
raw = discarded + consumed + remaining inventory = 1,024
```

The `K'` items are retained inventory, not discarded failures. If the complete preparation of this batch takes a hypothetical two seconds, raw throughput is 512 units/s and usable preparation throughput for the `K` workload is 256 triples/s. This is not an online consumption rate. The time must include the expansion, filtering, authentication, checks, and coordination used to produce those usable outputs; report setup inclusion and amortization explicitly. Crediting the `K'` inventory to a second workload changes the denominator and requires stating that workload.

## 3. Expansion ratios

State the ratio explicitly, for example `logical output-share bits / private seed-key bits`, and say whether both roles are summed or one role is reported. Public matrices/seeds, authentication keys, serialized metadata, and setup communication may be different objects with different inclusion rules. A compressed seed length is not the total cost of establishing it.

Count fixed schedule entries and padded or zero-payload slots when they are part of the represented keys; do not omit them merely because their algebraic contribution vanishes. Use the implementation's actual representation for storage claims and the defined representation for logical-bit claims.

## 4. Throughput definitions

For a run producing `N` accepted units under a declared pair-time rule `T_run`,

```text
R_run = N / T_run.
```

Record whether party expansions run separately, concurrently on one shared host, or on separate hosts, and whether worker limits apply per party or in total. State whether `T_run` is measured pair wall, `max(T_0,T_1)` from concurrent party timers, a maximum of separately measured local timers, or summed CPU work. Aggregate raw per-run rates or counts/times according to the experiment design; do not reconstruct a run rate from unrelated medians. `median(N/T_j)`, `mean(N/T_j)`, and `sum_j N_j / sum_j T_j` answer potentially different questions; retain the declared rule and raw observations.

Conversions are identities only when the grouping is fixed. For constant width `B`, scalar rate divided by `B` gives coordinate rate. It does not establish that an independent `B=1` invocation has that performance.

For a modeled protocol consuming `c_i` units from component `i` at compatible rate `R_i`, a sequential no-overlap estimate may use

```text
T_hat = sum_i c_i / R_i,
R_hat = workload_units / T_hat.
```

Label this modeled. Change the formula when calls overlap, have setup amortization, depend on batch shape, or use incompatible security configurations. Propagate uncertainty from the raw component measurements rather than quoting a false exact rate.

## 5. Comparison gate

Before dividing two rates, align or visibly qualify:

- relation/interface and party holdings;
- field/ring and element width;
- block/vector/call shape and padding;
- security calibration, actual sampling ensemble, setup trust, and permitted reuse;
- timed phases, workers, concurrency, and denominator;
- evidence class and artifact fidelity.

If these do not align, report both decomposed rates without an overall speedup. A quotient of unlike scalar counters is at most a descriptive rate ratio. Reserve “speedup” for a common downstream workload or consumption interface with aligned boundaries. Explain which mechanism—packing, width, encoder, call shape, omitted setup, or hardware—could account for the difference, and mark it as interpretation unless directly measured.
