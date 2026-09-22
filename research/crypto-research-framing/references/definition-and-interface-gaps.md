# Diagnose the gap between intended use and the available theorem

Use when a useful construction lacks the theorem its consumer needs, or when an existing theorem gives an inadequate quantitative bound. State the unsupported use before proposing a new primitive. Select the relevant gap; these are alternatives, not a checklist every project must complete.

| Gap | Decisive question | Useful next result |
| --- | --- | --- |
| Definition | Which allowed attack or composition does the current notion omit? | A separation and a candidate definition, followed by an implication to the intended guarantee |
| Assumption | Which exact proof step consumes the stronger premise? | A replacement lemma exporting the same property from a weaker premise |
| Quantitative bound | Which event or simulation cost forces the expensive parameter? | A sharper reduction for the fixed construction, or a construction change that removes the cost |
| Input interface | Who controls each argument, when, and with which exposure? | A matching theorem or a counterexample for the changed use |
| Modularity | Which internal technique do distinct consumers repeatedly reprove? | A precise component interface and application theorem tested with another realization |
| Model versus application | Which relevant behavior lies outside the formal experiment? | A scoped limitation and a separately justified extension |

## Separate reanalysis from construction changes

Keep the intended functionality, corruption, leakage, setup, and cost objective fixed unless the user permits a change. First ask what the existing algorithms already provide. Separately consider whether a small change to randomization, encoding, or domain handling enables a better proof. Removing a premise or a loss from the statement is not a reanalysis.

Map an assumption to the exact operation or event it justifies. Remove it provisionally and locate the first unproved step. A weaker replacement must suffice for that same step under its actual input distribution and exposure; a weaker-sounding assumption is not evidence. Breaking a sufficient assumption need not yield an attack on the construction.

When a loss depends on users, sessions, queries, gates, or checks, identify the event it counts. Replacing that count by corruptions or active instances needs a selection, coupling, or embedding argument under explicit structural hypotheses. Typical workloads alone do not bound an adversary. A changed operational restriction is a changed target until accepted as such.

## Specify the consumer's quantitative interface

Begin with the sentence the outer proof needs to justify. For an extractor, distinguish its input and oracle access, success condition, knowledge error, rewinding, and expected versus strict running time. For a simulator, specify the information available when it must produce and later explain state.

An elementary accounting example: if a subroutine is invoked with probability `p>0` and its expected cost conditional on invocation is at most `T/p`, its expected contribution is at most `T`. A conditional bound `T/(p-kappa)` for `p>kappa` gives only `T*p/(p-kappa)`, which can grow as the gap shrinks. This calculation requires the stated conditional bound at the actual invocation; an unconditional runtime bound or an acceptance probability from another experiment cannot be substituted. Expected time does not become strict polynomial time without a justified conversion and its error cost.

For a proposed change of definition, prove the implication consumed by the application before using the simpler experiment. List the allowed functionality, input samplers, auxiliary information, leakage, setup, adversarial behavior, and runtime overhead. Existence of a simulator, an efficient procedure to construct it, and applicability to the current protocol are separate claims.

Read [compatible-input-simulation.md](compatible-input-simulation.md) only when a worked example of such an implication would help. It isolates a sufficient condition for one passively corrupted party's view, including an efficient compatible-input constructor; it is not a malicious-MPC or composition theorem.

## Check the arguments of a cryptographic call

For each relevant argument to a keyed function, commitment, encoding, or sampler, record its owner, distribution, secrecy, choice time, freshness, and relation to other arguments. Recheck the theorem when an optimization swaps public and secret inputs, fixes a formerly random key, accepts a larger domain, or exposes generation coins. The implementation may evaluate the same function while using a different security experiment.

Test the smallest counterexample that exercises the change. A key-uniqueness question needs a definition that actually excludes distinct valid keys; a fixed-length theorem needs a domain-preserving encoding argument before covering mixed lengths. A generic construction from an assumption does not certify a specific deployed instantiation.

## Make the proposed argument executable

Write the reduction's final decision rule, not only its challenge embedding. For each branch on validity, success, consistency, or a bad event, identify an efficient test using its supplied inputs and oracles. An event can separate distributions statistically without giving a computationally bounded observer a test. Conversely, a coupling bound on a bad event need not detect that event online when the probability is established analytically.

Use one falsifiable next obligation: a local reduction, a compatible-input constructor, a separation, an assumption replacement, or a corrected cost calculation. An optional independent attempt followed by source comparison can expose missing premises; it is a learning method, not a reason to withhold the answer or require the user to solve an exercise first.

## Origin and scope

Adapted from §§3–4 and 7–8 of the user-supplied *Learning from Mihir Bellare: A Cryptography Research Distillate* (September 21, 2026). The classification and proposed actions are repository adaptations, not a personal methodology attributed to Bellare. The conditional runtime calculation is elementary; no extraction or composition theorem is imported from an inaccessible paper. Verify primary sources before asserting a paper-specific result. These instructions are not evidence of improved research performance.
