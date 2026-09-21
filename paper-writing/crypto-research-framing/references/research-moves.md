# Choosing a research move

Read the relevant cases when a research question needs a new definition, representation, component, or assumption. These are methodological proposals, not guarantees of novelty or success. Choose according to the obstacle; do not force every project through the full list.

## Change the capability along one dimension

Use when the existing task fails to express a useful behavior. Vary who chooses a policy, when it is fixed, which outputs are released, or which parties may cooperate. Exhibit two situations the old task treats alike but the proposed task must distinguish. State the changed correctness and security conditions, including the new attack that must be excluded.

The obligation is substantive usefulness and realizability under explicit premises. Added syntax or a renamed parameter is insufficient. Cooperation that reconstructs a secret in one setting may be unauthorized collusion in another. Do not generalize merely to make a contribution sound broader.

## Separate the desired task from its setup

Use when a proposal replaces interaction with preprocessing, trust, hardware, or an oracle. First give all components ideal implementations: does the idealized task already leak too much or give the wrong participant control of abort or delivery? If so, stronger components do not fix the task.

Record which effect comes from the functionality and which from the available setup. A distributed realization of ideal preprocessing is a separate obligation. Moving work earlier can improve online cost while increasing setup cost or changing trust. Preserve both conclusions.

When removing an authority, trace each former responsibility: generating secrets, certifying inputs, maintaining public or private state, handling updates, enforcing consistency, and controlling failure. Identify its new owner or the theorem making it unnecessary. Removing key escrow or an online dealer need not remove a CRS, registration work, or all trust.

## Reformulate a blocked guarantee

Use when an actual impossibility or a precise failed premise obstructs the target. Compare the original requirement, the exact changed clause, and a useful application that still follows. Recheck every quantifier at the point where a theorem is invoked; an average-case resemblance need not satisfy an all-input premise.

An alternative definition earns its place through a meaningful consequence and a supporting argument. It does not solve the original problem merely by being satisfiable. Do not treat a failed candidate as an impossibility theorem, or weaken security without making the change visible.

## Change the mathematical representation

Use when the current formulation hides a tractable operation on distributions, equations, ranks, or local constraints. Specify the map on instances and witnesses, its cost, and how adversaries and their auxiliary information are represented. Write the directions actually needed:

`original property => property of the representation => desired conclusion`.

The directions need not form an equivalence. Identify the operation the representation enables, such as amplification, local checking, extraction, or efficient evaluation. A matrix reformulation that proves only correctness, loses correlations, or expands the instance beyond the target cost does not discharge the security or efficiency obligation.

## Reuse a protocol in another role

Use when a protocol's executions, internal views, or guarantee could supply a specific object needed by an outer argument. Distinguish executing it among real parties, simulating virtual parties locally, and invoking its theorem inside a reduction.

List what the verifier or adversary jointly sees: openings, commitments, indices, messages, previous challenges, and auxiliary state. Match that exposure to the component's privacy premise. Assign soundness or detection to a separate argument; privacy alone does not enforce consistency. Opening an extra view can cross a privacy threshold, and virtual honest-majority assumptions do not establish an honest majority among real participants.

## Preserve native algebra or separate conflicting requirements

Use native algebra when generic encoding discards structure relevant to cost. Compare direct relations with their encoded version, including setup, field conversion, representation size, and required security properties. Preserve the target adversarial view, not only honest outputs. A specialized construction may need a different proof and need not inherit the generic compiler's composition guarantee.

When no candidate satisfies all requirements, state those requirements separately: correctness, size, locality, degree in each class of variable, hidden support, and distributions the reduction can sample. Explain which condition each candidate violates. For example, compressing a table by publishing secret-dependent occupied indices can reduce size while invalidating privacy. Check those indices jointly with the rest of the view.

If useful, compare candidates that fail for different reasons and ask whether a representation can separate the conflicting conditions. Label invented examples as explanatory candidates, not historical attempts by a paper's authors. Do not fabricate a failed baseline to create a narrative.

## Match assumption exploration to the project

Use when choosing between foundational exploration and a deployment claim. For a proposed hardness assumption, specify the underlying algorithmic problem, input distribution, adversarial resources, and what an attack would teach. Explain whether it has content beyond restating the desired cryptosystem's security. Evidence against a particular attack family is not a general hardness guarantee.

For efficiency comparisons, use a common security parameterization and include reduction losses, honest costs, setup, and amortization. Scientific interest in a conjecture does not establish deployment confidence; conversely, a theory project need not use only mature deployment assumptions. State the goal and evidence without treating either preference as universal.

## Origin and evidence

Adapted from the user-supplied *Learning from Amit Sahai: A Cryptography Research Distillate* (research cutoff September 20, 2026), especially §§3 and 7–8. These instructions are repository adaptations of its proposed research actions. They do not attribute a personal method, endorsement, or discovery sequence to Sahai or his coauthors. The full report is not bundled; its claims of source access are not records of this repository's verification. Consult primary sources before making paper-specific claims. No improvement in agent research quality is established by adopting these instructions.

The responsibility mapping also draws on the proposed action in §3, Move 9, of *Learning from Brent Waters: A Cryptography Research Distillate* (research cutoff September 21, 2026), under the same attribution and validation limits.
