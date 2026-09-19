---
name: crypto-implementation-evaluation-writing
description: Draft, revise, or review implementation and performance-evaluation sections for MPC, zero-knowledge, and other cryptography papers. Use when turning artifact or benchmark evidence into manuscript prose, checking comparison fairness and supported claims, or identifying experiments needed for an evaluation claim. Do not use for benchmark execution, protocol implementation, raw data analysis alone, or proof-validity auditing.
---

# Crypto Implementation Evaluation Writing

Write an evaluation that makes clear what was implemented, what was measured, what was inferred, and what remains outside the evidence.

Organize substantial sections around the empirical argument: contribution claim, question, controlled comparison, observation, supported explanation, and qualified conclusion. Adapt this structure to protocol, primitive, compiler, application, or concrete-cost work; it is not a mandatory sequence of headings or a requirement for an end-to-end implementation.

## Authorization and supported claims

- Treat review or suggested wording as read-only unless edits are explicitly requested.
- A writing or evaluation review request does not by itself authorize benchmark runs, implementation changes, parameter changes, or publication. When evidence is missing, narrow the wording and identify the specific missing measurement or check; carry out further work when the user's task authorizes it.
- An executable artifact implements a protocol path; benchmark success does not establish the paper's security theorem or a concrete instantiation theorem.
- State the implemented security mechanisms and omissions separately from the theorem's guarantees. Keep ideal setup, omitted checks, and diagnostic configurations visible wherever they qualify a result. A seeded, conditioned, certified, or reused sampler need not instantiate the theorem's ensemble; parameter width and passing tests do not establish concrete security.
- Identify local reproductions, ports, and transformed variants separately from author-maintained implementations. A project-selected default is a configuration choice, not an endorsement or a transferred security proof.
- Do not call a component benchmark, ideal-resource fixture, analytical operation count, or projected optimization an end-to-end implementation.
- Preserve unknowns and failed configurations. Do not fill missing results by unstated extrapolation.

## Before drafting

Freeze the evaluation contract:

- implemented construction, variant, revision, and deviations from the specification;
- security parameters, concrete primitive choices, assumptions, and any insecure diagnostic configuration;
- parties, workload, circuit/relation/field, batch or amortization denominator;
- functionality, input/output ownership, setup/trust, leakage or output-delivery differences relevant to comparisons, and numerical correctness or approximation target;
- setup, preprocessing, expansion, online, and cleanup phases; for proof systems, distinguish relation compilation, witness generation, proving, and verification when relevant;
- initial prepared state, dependencies on inputs/function/participants, and which state is reusable or consumed;
- hardware, software, network, concurrency, memory, and trial methodology;
- metric definition and aggregation;
- provenance of every reported value.

Use the available evidence without inventing missing facts. For a full section, a compact working table can hold results, phase definitions, and claim-to-evidence mappings; do not require separate planning documents for every edit. If evidence is incomplete, draft the narrowest supported section and identify the gaps that materially affect the claim.

## Working method

Read [references/evaluation-method.md](references/evaluation-method.md) in full for a new or substantially revised implementation/evaluation section or table, or whenever included operations, provenance, or accounting are uncertain. For a narrow local sentence edit whose evidence contract is already fixed, use only the invariants in this entrypoint; load the full method if the edit exposes an uncertainty that requires it.

1. Record results and the questions they answer before writing. Label each value as measured, baseline rerun, inherited, derived, estimated, extrapolated, or projected, down to the cell when a row mixes evidence classes.
2. Describe implementation scope and optimizations before performance so readers know which algorithm generated the data.
3. State security configuration and implementation deviations separately from performance choices.
4. Define environment, workloads, repetitions, timed operations, communication accounting, failure handling, and exclusions.
5. Present primary results before interpretation. Separate phases and evidence classes in tables or figures.
6. Align baselines on functionality, guarantees, included costs, and computation budgets. Distinguish protocol comparisons on a common workload from whole-system comparisons and identify uncontrolled differences.
7. Explain trends through evidence, then discuss observed bottlenecks, crossovers, and limitations. A profile may support an explanation; an uncontrolled correlation does not isolate a cause. Label untested explanations as hypotheses.
8. Recompute table arithmetic and reconcile prose, captions, legends, headers, and formulas.

Load further references only when they help the request:

- [Argument and experiment design](references/argument-and-experiments.md): organizing a substantial section, planning evidence, assessing baselines, or adapting to compiler/application work.
- [Setup, phases, and amortization](references/setup-phases-and-amortization.md): role topology, correlations, PCGs, proof-system setup, reuse, expansion, and phase-specific claims. Follow the target construction's interface.
- [Evidence sources and reading routes](references/evidence-sources.md): selecting paper examples, interpreting the supplied 30-paper corpus and selection audit, or reconciling it with the earlier eight-paper notes. Read selected entries instead of loading the whole corpus by default.

## Required distinctions

Keep these separate whenever relevant:

- protocol specification, implementation, and concrete instantiation;
- secure configuration and insecure diagnostic proxy;
- setup/seed generation, circuit-independent preprocessing, circuit-dependent preprocessing, local expansion, input processing, online evaluation, and total;
- wall-clock time, CPU time, per-party time, critical-path time, throughput, and latency;
- payload bytes and transport bytes; one-way maximum, per-party, aggregate, point-to-point, and broadcast;
- single execution, parallel batch, sequential amortization, and reusable preprocessing;
- input independence, permitted reuse, fresh consumable correlations, and unused batch outputs;
- measured end-to-end result, measured component, analytical count, inherited number, estimate, extrapolation, and projection;
- average, median, percentile, range, standard deviation, and confidence interval;
- excluded cost, unavailable cost, and zero cost.

## Output standard

The section should be reproducible in proportion to the claim and honest about its evidence class. A reader should be able to identify the exact artifact and configuration, determine what each metric includes, and distinguish measurements, calculations, and interpretations. Keep material qualifications in the main text and discoverable from the affected table or figure.

A build, known-answer test, portability check, or small smoke run supports only its tested functionality and configuration. Report planned, completed, failed, and unrun experiments accurately; do not promote smoke-run rates to publication evidence. When execution is authorized, `crypto-benchmarking` is an optional companion. Without it, use the local [evaluation method](references/evaluation-method.md) to fix the configuration, start/stop events, workload, repetitions and aggregation before collecting and retaining raw evidence.

Match the requested deliverable: a local edit receives a local edit; a review receives findings; a full draft may include useful tables/captions and a short prioritized list of evidence gaps; an experiment plan proposes the smallest informative set of measurements. Preserve manuscript terminology, notation, wrapping, and unrelated prose when revising existing text.
