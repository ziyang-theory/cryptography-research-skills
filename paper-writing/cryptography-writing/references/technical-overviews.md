# Writing a cryptographic technical overview

Use this guide for a technical overview, an overview of techniques, an approach section, or an explanatory proof outline. Such a unit may be inside the introduction or later in the paper. For a local edit, preserve its organization and make only the requested repair. The source examples concern MPC and related primitives; transfer their explanatory choices to other areas when the contribution has the same shape.

## Purpose and preparation

Give the reader enough understanding to explain the central mechanism, why its ingredients are needed, and what remains to be established in the formal treatment. The introduction's result statement supplies the destination; the overview explains how the construction or argument reaches it. Avoid repeating the contribution list or paraphrasing every protocol step at equal depth.

Recover the actual construction, claim, and available supporting lemmas before drafting. Identify the point the reader is most likely to find difficult: a missing interface, an apparent attack, an incompatible pair of requirements, a cost bottleneck, or a distributional argument. Choose the main explanatory thread around that difficulty. Treat user-supplied facts as supplied facts; use existing section/lemma anchors where available. Do not invent a failed baseline, an attack, a toy construction, or a missing proof step to make the story flow.

Assume the intended reader knows the field's standard background. Explain an unfamiliar primitive from its relevant inputs, outputs, and guarantee before asking it to carry the argument. Introduce notation when it becomes useful and reuse it in the formal section. A short dependency sketch can help the author plan the explanation; it need not appear in the paper.

## Choose the explanation order

A useful progression is **target → obstacle → observation → mechanism → remaining obligation**, but the material determines the order. The source corpus supports several alternatives:

| Shape of contribution | Explanatory choice | Examples |
| --- | --- | --- |
| One algebraic idea | Work through the smallest meaningful case; expose the identity or invariant; combine the cases and account for the cost. | P17 |
| Compiler or layered construction | Give the target resource, explain the intermediate interfaces, and show why each conversion is needed. Choose top-down or bottom-up order to reduce forward references. | P10, P16, N01, N03 |
| Family of constructions | State one common method; instantiate a representative case; explain only the changed requirement or mechanism for each further case. | P28 |
| Difficult security argument | Begin with a clearly labeled easier setting or hypothetical tool; show what it explains and why the actual assumption requires more work. | P38 |
| Several interacting obstacles | Track the unresolved issues, explain which step discharges each, and revisit the remaining ones. | N02 |
| New model or lower-bound argument | Expose the concrete behavior the definition must capture or the separating experiment; explain the key logical implication and its scope. | P20, P45 |

These are options, not required headings or a fixed number of paragraphs. A direct explanation is often better when no failed approach is documented. A baseline overview can establish needed background, but mark it as prior work and transition explicitly to what the new construction changes. A long paper can pair a short global map with local overviews of difficult components; avoid repeatedly restarting the whole story (P29, P48).

## Make the mechanism visible

**Use a minimal case with a purpose.** A gate, two parties, one correlation, a tree, or an idealized primitive can isolate the idea. State what was simplified before using it: adversarial behavior, number of parties, function class, exact arithmetic, setup, or a stronger hypothetical assumption. Explain the step that restores the actual setting, or say where it is handled. Do not silently promote semi-honest intuition to malicious security or a toy case to the general theorem. The simpler construction need not be a usable special case; if it is only an expository device, label it accordingly.

**Explain the new object's interface.** Say who holds which values, what is public or hidden, which party computes or learns an output, and what the new operation preserves. In a reduction or compiler, identify the consumed resource and the produced guarantee. Explain why the consumer needs that property; the primitive's name alone rarely supplies this connection. Retain state and lifetime when they affect the argument, especially for preprocessing and NISC reuse.

**Let equations do explanatory work.** Include an identity, invariant, or short calculation when it reveals the mechanism more clearly than prose. Explain the operands' roles and what the relation enables. Distinguish an algebraic correctness identity from a privacy or simulation claim. Define the view and the relevant correlation when arguing that a mask hides information; a marginally uniform value need not remain hidden given everything else revealed. A displayed equation is useful when it supports the next inference, not just because the formal construction contains it.

**Give each component a reason.** Connect its input/output guarantee to the next step. Explain which consistency condition, adversarial action, or cost it addresses. When components share state or consistency checks, explain their interaction; do not assert a modular composition that the actual argument does not provide (P14). When a step deliberately permits leakage, abort, or another relaxation that a later transformation removes, retain both the intermediate guarantee and the repair. A brief list of pending obstacles can make a long construction legible; every listed obstacle should eventually be resolved or explicitly deferred.

**Use diagrams when they reduce ambiguity.** A component graph, role/message diagram, or small worked example can clarify ownership, dependencies, and parallelism. Label whether an arrow means a construction reduction, a runtime message, or an exposition dependency. These need not coincide. Do not make a teaching order look like the actual execution order, or turn parallel operations into additional rounds. Cite a figure from the prose and explain the important relationship it shows.

**Explain the source of the improvement.** Tie a cost reduction to the expensive operation removed, shared, batched, or moved to another phase. For round savings, explain when a value must be fixed, known, or revealed, and which dependencies permit parallelism (P39). Give the unit and dominant parameter; identify the compensating cost or regime when material. A compact calculation can explain the scaling without reproducing an evaluation section. Preserve the distinction between analytical estimates and measured performance, and between a component's efficiency and the cost of generating its ideal inputs.

## Security intuition and the handoff to formal arguments

Use correctness intuition to explain why honest computation produces the intended relation. Use security intuition to identify the adversarial freedom, what prevents it from helping, and the invariant or assumption supporting that explanation. When a simulation view is informative, describe what must be extracted, simulated, or kept consistent and why the available interface permits it. If only one corruption case or a simplified execution is discussed, label that scope.

An explanatory proof outline need not contain the full simulator and every hybrid. The skill's simulation-first preference applies to full proofs and authorized proof reorganizations; it does not require an overview to become a full proof. If actual hybrids are given, retain their endpoints and the reasons for the selected transitions. Do not replace the governing definition with an intuitive claim that the adversary learns nothing. Native algebraic, game-based, combinatorial, or lower-bound explanations should follow their own argument.

Finish each major explanatory thread by connecting it to the actual construction or formal statement. Point to the lemma, theorem, section, or full version that supplies the deferred argument, using only anchors that exist. Make the central reason understandable before this handoff; calling it a standard argument or deferring every difficult point leaves no useful overview. For an author-authorized draft with missing details, preserve an explicit gap or outline rather than inventing the argument. A requested proof completion or validation requires substantive proof work; use `crypto-proof-auditor` when available, and do not substitute exposition for the missing derivation.

## Revision check

When space is split between a main text and appendices, give each location a purpose: the overview explains the idea, the main construction section exposes the interface and supported guarantee needed by later sections, and the appendix provides the detailed algorithms and proofs. Retain essential definitions, conditions, and a consuming section's needed interface in the main text. Use specific stable references for deferred details; moving material should not strengthen the main-text theorem or leave the appendix without its notation. Apply this redistribution only within an authorized reorganization.

Read the overview beside the formal construction and result. Can a reader identify the new idea, each essential ingredient's role, the simplifications, and where the remaining obligations are handled? Check that ownership, interfaces, variants, setup, reuse, and costs agree across the two accounts. Ensure that a failed approach is supported and that every temporary assumption is either discharged or retained in the final scope.

Keep the explanation focused: omit routine mechanics that do not illuminate the idea; retain details whose omission would make the mechanism misleading. Preserve the author's terminology and local-edit boundaries. There is no required overview length, failed-approach narrative, diagram, toy example, or heading scheme.

Read [technical-overview-evidence.md](technical-overview-evidence.md) when selecting source examples or checking provenance. Use the existing security, secure-computation, and construction/cost references for exact terminology. This guide supports exposition; the source study is not a proof audit or evidence that a writing pattern causes citation impact.
