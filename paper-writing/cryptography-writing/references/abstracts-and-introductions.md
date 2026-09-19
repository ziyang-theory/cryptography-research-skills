# Writing cryptography abstracts and introductions

Use this guide for new writing, an authorized structural rewrite, or a review of organization. For a local edit, retain the manuscript's structure and apply only the relevant repair. The source corpus concerns secure computation; transfer its rhetorical decisions to other areas only when the contribution has the same shape.

## Start from the contribution

Before choosing an opening, recover a compact claim sheet from the manuscript: the task, closest relevant baseline, precise unresolved obstacle, main result, reason the new approach works, and material qualifications. Attach existing theorem/definition/table locators where available; identify supplied facts as such. Mark missing evidence instead of completing the story with an invented result. This is drafting scaffolding, not a form to paste into the paper.

Choose the organizing contribution: a new feasibility result, a better cost under a fixed model, a new model or abstraction, a compiler with several applications, or a specialized application protocol. A paper can combine these; give it one central thread and subordinate the other results to that thread. An implementation is a separate evidence class from a theorem or analytical estimate.

## The abstract: a compact account of the result

A useful default is **task or bottleneck → result with decisive conditions → new idea → consequence or tradeoff**. Change the order when the result itself supplies the best orientation. The corpus contains result-first, question-first, and application-first abstracts; it does not justify one universal template or sentence count.

Select an opening that gets to this paper's problem:

| Contribution | Productive opening and progression | Examples in the evidence companion |
| --- | --- | --- |
| Efficiency | Identify the costly component or incompatible previous improvements; state the new bound against that baseline; explain the enabling idea and relevant tradeoff. | P04, P17, P44 |
| Protocol with several phases | Name the task and adversary; separate the online result from preprocessing assumptions and costs. | P01, P19 |
| Framework or compiler | State the missing conjunction of properties or the transformation interface; give the mechanism once; attach distinct conditions to its consequences. | P05, P10, P23 |
| New model | Identify the mismatch in existing models; define the proposed guarantee informally; separate motivation from what is formally guaranteed. | P35 |
| Application | Give the concrete joint computation and privacy requirement; explain the inadequacy of the generic solution; state the specialization and result. | P02, P03, P06 |
| Feasibility or minimal interaction | State the exact question and resource model; give the achieved construction and its scope or remaining restriction. | N01–N03 |

State the principal contribution explicitly with an accurate verb: construct, prove, characterize, define, implement, or measure. Explain what changes relative to the previous situation. Avoid making the reader infer the result from a list of techniques or applications.

Place the conditions that determine the headline's meaning next to it: for example, malicious versus semi-honest security, honest versus dishonest majority, an OT hybrid, a setup assumption, security with abort, or a restricted function class. Do not reproduce every formal axis in every sentence; expand less salient details in the introduction and point to the governing definition. Never remove a material qualification just to shorten the abstract.

Give a cost in a meaningful unit and regime. Distinguish per-gate from per-execution, online from total, asymptotic from measured, and amortized from single-use. A speedup needs a baseline and workload; an asymptotic improvement needs its parameter. Name only the assumption or ideal resource supported by the corresponding claim. One variant's low cost and another's stronger guarantee cannot be combined into a synthetic headline.

Include the new idea when it explains why the result is possible. A named component alone is usually insufficient: identify the role it plays. Use secondary results only when they develop the same contribution or are independently substantial. Close with a supported consequence or material tradeoff, not a generic claim of broad impact.

Citations, a short formula, and result enumeration can be appropriate in an abstract; the examples do not support blanket bans. Follow the target venue and manuscript conventions. Avoid undefined notation and citations that substitute for an explanation. Do not copy source wording or transplant historical numerical claims.

## The introduction: make the result intelligible and assessable

The opening should answer: **What is the task? What specifically remained unresolved? What is achieved here? Why does the new approach overcome the obstacle? Under what conditions does that matter?** These are reader needs, not mandatory section headings. A short introduction may hand off fuller results or related work to the immediately following sections, as in P02, P08, and P09; assess the opening as a whole rather than forcing everything under a heading named Introduction.

1. **Orient and narrow.** Define the relevant task or scenario at the level needed for the contribution. Move from known feasibility to the particular cost, assumption, model, or interaction obstacle. Give application background when it explains the interface or constraints. Avoid a long field history before the paper's target becomes visible.
2. **Establish the gap.** Explain the closest competing approaches and which requested combination they fail to achieve. A gap can be a technical barrier, an unachieved conjunction, or a domain mismatch; it need not be a formal lower bound. Do not turn absent prior constructions into an impossibility claim. Use a compact comparison table when several independent axes would otherwise obscure the argument.
3. **State the results early enough to guide the rest.** Give the object being constructed or transformed, the principal guarantee, assumptions/resources, and cost regime. An informal theorem helps when a quantified bound or tradeoff is central; contribution prose can suffice otherwise. Organize multiple results by purpose, phase, or dependency rather than by the order the research happened. Distinguish the main result from corollaries, implementations, and concurrent work.
4. **Explain the technical idea causally.** When supported by the source, start with the natural approach and the obstacle it encounters. Introduce the new observation, abstraction, or mechanism, then explain how it removes that obstacle. If the failed approach is not documented, explain the supported mechanism directly rather than inventing a failure story. Include just enough interface, invariant, or security intuition to connect the idea to the claim. For a compiler, specify what goes in, what comes out, and what each component accomplishes. A technical overview is not a component inventory or a compressed substitute for the proof.
   For a substantial technical overview, read [technical-overviews.md](technical-overviews.md) for explanation order, simplified cases, component interfaces, and the handoff to formal arguments.
5. **Position and qualify.** Compare against the closest baselines on aligned axes, preserving their remaining advantages. Put limitations where they affect interpretation rather than deferring all of them to the end. Related work may be integrated or separate; a roadmap is useful only when it helps navigation. Neither is a compulsory final paragraph.

The introduction may repeat the abstract's central result because it must stand on its own. Each repetition should add something: motivation, formal scope, a baseline, a mechanism, or a tradeoff. Avoid expanding the abstract sentence by sentence without developing the argument.

## Conditional details for layered protocols and proof systems

- **Preprocessing:** Explain why moving work before inputs arrive matters, what remains online, and who generates or trusts the correlated resource. A lightweight online phase is not a cheap end-to-end protocol. Separate computational assumptions, corruption timing, and cost when phases differ.
- **Interaction and reuse:** Specify the parties, who sends which messages and receives outputs, what setup is outside the count, and what is reused. For NISC, a published first message, a one-shot correlation, and a reusable key are different resources. If output feedback or repeated sessions affect security, make that restriction visible where reuse is claimed.
- **New primitives:** Explain the exposed interface and its benefit to secure computation before listing applications. A PCG seed expansion, correlated preprocessing generation, and the consuming MPC protocol have distinct cost boundaries.
- **Weaker or different security:** Describe what the guarantee permits as well as what it prevents. Separate an argument that a model fits an application from the mathematical guarantee against the defined adversary. Do not promote motivation about deterrence or trust into a theorem.
- **Proof systems and transformations:** When applicable, identify the proved property—soundness, knowledge extraction, zero knowledge, or a stated combination—and the setup and adversary conditions. For a compilation or optimization, distinguish the source theorem from the property established for the transformed system. Do not merge one variant's proof size with another variant's security guarantee.

Use `crypto-prior-work-comparison` when available for substantive comparisons and the existing security/cost references for exact terminology. If that companion is absent, align the compared model, guarantee, cost regime, and primary-source evidence directly. This guide concerns presentation; it does not certify the proof, construction, or benchmark.

## Revision checks

Read the abstract and introduction against the claim sheet and the actual theorem/table statements. Check that the same construction variant, model, phase, resource lifetime, and cost object are being described throughout. Verify numerical claims and any first/best/optimal claim against current primary evidence; qualify or remove unsupported priority language rather than imitate a source's historical rhetoric.

Check that a reader can identify the main result and its significance before the technical overview. Then remove background, comparisons, and secondary results that do not help assess that result. Preserve local terminology and the author's voice. Do not force formal theorem formatting, contribution bullets, a fixed length, or this guide's order onto every paper.

For source-specific examples and the study's selection/version limits, read [abstract-introduction-evidence.md](abstract-introduction-evidence.md). The corpus records observed choices; the recommendations above are editorial synthesis, not evidence that a style causes citations.
