---
name: crypto-implementation-evaluation-writing
description: Draft, revise, or review cryptography implementation and evaluation sections from code and experimental evidence. Use for supported performance claims, fair comparisons, and identifying missing evidence; not benchmark execution or raw analysis alone.
---

# Crypto Implementation Evaluation Writing

Make clear what was implemented, measured and inferred, and which conclusions the evidence supports. Build the section around its empirical argument rather than a mandatory sequence of headings.

## Workflow

1. Identify the evaluated construction/configuration and the evidence for each result. Fix workload, guarantees, included phases, prepared state/reuse, metric, aggregation and provenance. A compact working table is enough when useful; a local edit need not create planning documents.
2. Describe implementation scope and material deviations so readers know which algorithm produced the data. Distinguish original artifacts, reproductions, ports and transformed variants. Keep the implemented sampler and concrete parameter support separate from the formal theorem.
3. Present results before interpretation. Align comparisons on functionality, guarantees, workload, costs and resource budgets; expose uncontrolled differences. Separate protocol comparisons on a common workload from whole-system comparisons on an application.
4. Connect observations to a supported explanation and qualified conclusion. Profiles can support an explanation; uncontrolled correlation does not isolate causality. Label untested explanations and proposed optimizations accordingly.
5. Recompute arithmetic and reconcile prose, tables, captions and legends. Keep exclusions, failures and evidence classes discoverable beside affected results.

A component benchmark, ideal-resource fixture or modeled cost is valid evidence for its stated scope, but is not an end-to-end measurement. Builds, tests and smoke runs establish only their tested coverage. Preserve unknowns instead of filling them by unstated extrapolation.

## References by task

- [Evaluation method](references/evaluation-method.md): result records, measurement semantics, evidence labels and final checks; read the relevant sections when these are uncertain.
- [Argument and experiments](references/argument-and-experiments.md): substantial sections, comparison design and evidence gaps.
- [Setup, phases and amortization](references/setup-phases-and-amortization.md): role topology, correlation consumption, proof-system setup and reuse.
- [Evidence sources](references/evidence-sources.md): optional historical examples and their provenance; select entries rather than loading the corpus.

Match the deliverable: findings for a review, a scoped edit for revision, or a supported section for drafting. Preserve existing notation, wrapping and unrelated prose. Missing evidence calls for a narrower claim or a specific follow-up; run experiments or change code only when the user's task authorizes that work.
