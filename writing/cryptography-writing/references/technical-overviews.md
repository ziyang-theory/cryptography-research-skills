# Technical overviews

Use for an overview of techniques, an approach section, or an explanatory proof outline, wherever it appears in the paper. Preserve structure during local edits. The optional examples concern MPC and related primitives; adapt them by contribution shape.

## Choose the explanation's purpose

Recover the actual construction, claim, and supporting lemmas. Find the hardest connection for the reader: a missing interface, apparent attack, incompatible requirements, cost bottleneck, or distributional argument. Explain how the mechanism resolves it. An overview should do more than repeat results or summarize every protocol step equally.

Assume standard field knowledge, but introduce an unfamiliar primitive through its relevant inputs, outputs, and guarantee. Reuse the formal section's notation. Do not invent a failed baseline, toy construction, or missing proof step for narrative convenience.

A useful progression is **target → obstacle → observation → mechanism → remaining obligation**, with alternatives:

| Contribution | Explanatory choice | Examples |
| --- | --- | --- |
| Algebraic idea | Smallest meaningful case, identity/invariant, combination and cost | P17 |
| Layered construction | Intermediate interfaces in the order reducing forward references | P10, P16, N01, N03 |
| Family of constructions | One common method, representative case, changed requirements | P28 |
| Difficult security argument | Labeled simpler setting/hypothetical tool, then actual proof obstacle | P38 |
| Interacting obstacles | Track which step resolves each remaining issue | N02 |
| New model or lower bound | Behavior/separating experiment and key logical implication | P20, P45 |
| Component used in another role | New exposure and the original guarantee protecting it | M01 |
| Useful algebraic representation | Preserved equations and enabled operation before proof machinery | M02 |
| Conflicting requirements | Candidate repairs and the constraint each misses | M03 |
| Proof-only modes | Changed semantics and why the reduction cannot test its own challenge | M04 |
| Approximation or rounding | Actual error term and needed bound/margin/rejection | M05 |
| Quantitative security | Expensive reduction term and whether proof or construction changes | M06 |
| Definition for a consumer | Failed inference and the quantified interface that repairs it | M07 |
| Maintained representation | One component's output has exactly the form the next consumes | M08 |
| Round overlap | Identify which messages can be formed before the other task finishes | P12, P39 |

These are options, not a template. Use a direct explanation when no failed approach is documented. A long paper may combine a global map with local component overviews (P29, P48). Mark a prior-protocol explanation as background before explaining the new contribution.

The [supplemental cases](technical-overview-evidence.md#supplemental-mechanism-cases) concern mechanisms, not discovery history or individual coauthor credit. Keep mathematical dependency, explanation order, real execution, and hybrid order distinct. A proof-only mode need not be available to protocol participants.

## Make the mechanism visible

**Use a small case for a reason.** A gate, two parties, tree, correlation, or idealized primitive may isolate the invariant. State what was simplified—adversary, function class, arithmetic, setup, or hypothetical assumption—and how the formal treatment restores the actual setting. A teaching construction need not be a usable special case; label it when it is only an expository device. Do not promote passive intuition to malicious security.

Specify the toy functionality's output recipients and any intermediate values it intentionally reveals. Do not describe that functionality as revealing only the final answer. If these values reveal more than the target permits, identify the changed privacy obligation and explain which dependency the toy still preserves; this is a relaxation, not merely a smaller instance.

**Expose interfaces.** State who holds what, what is public or hidden, who computes/learns an output, and what the operation preserves. Explain why the next component needs its guarantee. Retain state and lifetime where preprocessing or reuse affects that reasoning.

For a repeated gate or stage, state the representation invariant once, then show how a representative step preserves it and how input encoding and output recovery connect it to the intended computation (M08). Separate preservation of the algebraic representation from preservation of the adversary's joint-view distribution. This can replace a long list of similar gate procedures.

**Let equations explain.** An identity or short calculation should reveal the invariant or enabled operation. Distinguish algebraic correctness from security. A mask's uniform marginal need not hide its secret given the joint view; show the relevant correlations. A formula copied from the construction without explaining its next implication adds little.

**Give each component a purpose.** Name the consistency condition, adversarial freedom, or expensive operation it addresses. Shared state and checks can obstruct a fully modular account (P14). If an intermediate step permits leakage or abort later repaired, preserve both guarantees and the repair. Resolve or explicitly defer each introduced obstacle.

**Show dependencies accurately.** A figure can explain ownership, interfaces, or parallelism. Label whether arrows mean runtime messages, construction reductions, or exposition dependencies; these differ. Cite and explain the figure in the prose. Teaching order must not create fictitious protocol rounds.

**Explain the saving.** Identify the operation removed, shared, batched, or shifted, with its dominant parameter and compensating cost. For round savings, track when values are fixed, known, and revealed (P12, P39). If overlap is the key step, show which input to each concurrent operation is already available; an unfinished evaluation key may or may not block input encryption. Distinguish analytical estimates from measured performance, and component costs from generating their ideal inputs. Use [construction and cost accounting](constructions-and-costs.md) when phase totals or round conventions need clarification.

## Security intuition and formal handoff

Correctness intuition explains honest outputs. Security intuition identifies adversarial choices, why they do not help, and the invariant or assumption supporting that claim. If simulation clarifies the mechanism, explain what must be extracted or kept consistent and why the interface permits it. Label any single-corruption or simplified case.

An overview need not contain the full simulator and every hybrid. If it includes selected transitions, retain their endpoints and justification without claiming to prove omitted steps. Follow the native argument for algebraic, game-based, combinatorial, or lower-bound results; an intuitive assertion that the adversary learns nothing is not a replacement definition.

Connect each major thread to an existing construction, lemma, theorem, or section supplying the deferred details. Make the reason understandable before that handoff. For an authorized draft with missing reasoning, leave the gap visible. A requested proof completion or validity audit requires substantive proof work, not a smoother overview.

For authorized redistribution between main text and appendix, keep essential interfaces and conditions available to their consumers. The overview explains ideas; formal construction exposes the needed guarantee; detailed algorithms/proofs can follow in appendices with valid notation and stable references. Moving a proof cannot strengthen its theorem.

## Revision check

Read the overview beside the formal construction: are the idea, component roles, simplifications, and deferred obligations identifiable? Check ownership, variants, setup, reuse, and costs across both accounts. Discharge temporary assumptions or retain them in the final scope. Omit routine mechanics that do not illuminate the idea while keeping details needed to avoid a misleading explanation.

There is no required length, failed-approach narrative, toy example, diagram, or heading scheme. [Source evidence](technical-overview-evidence.md) supplies optional examples and provenance; it is not a proof audit or evidence of citation impact.
