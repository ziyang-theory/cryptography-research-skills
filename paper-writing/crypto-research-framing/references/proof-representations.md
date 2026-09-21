# Proof representations and missing capabilities

Use when an exploratory construction is blocked by a reduction, setup simulation, adaptive timing, or a shared algebraic operation. First state the exact step the current proof cannot take. An unavailable trapdoor, an unsimulatable joint distribution, a future value, a quantitative loss, and a scoped lower bound are different obstacles. A direct argument may already suffice; do not introduce alternate modes merely because another paper uses them.

When revisiting a known existence result, compare the actual component dependencies and assumptions. Separate a new route from improved parameters or a newly realized functionality. Identify what becomes easier to understand, reuse, or optimize, and count any complexity moved into the new intermediate interface.

## Specify what a different proof object would buy

Start with the unjustified sentence in the outer proof, then define the interface that would justify it. Distinguish actual protocol objects from hypothetical objects used only in intermediate experiments. For each candidate mode, identify:

- who generates it and which challenge, secrets, randomness, and oracle access generation requires;
- its outputs, public information, party state, and simulator-only information;
- the semantic property it supplies, such as extraction from adversarial messages or a consistent explanation of an already-issued object;
- the complete compared view, including exposed seeds, coins, checks, and retained state.

If a compatibility table would clarify the mechanism, give one: rows and columns should be objects that can coexist in the same experiment. Qualify entries by identity, policy, encoding validity, or other correctness premises. Name a deliberately changed behavior and the observer who could test it. A table of intended behavior is a specification, not an indistinguishability proof.

Separate the outer claim that this interface suffices from the claim that an instantiation realizes it. The latter includes generating the right joint distributions under malicious choices; matching public-parameter marginals is insufficient when the experiment also reveals generation coins or local seeds. Do not define an intermediate primitive that merely performs the entire desired task.

## Test the reduction's actual capabilities

Write down what the reduction receives from its challenger and what it generates itself. Attempt a self-test: can those capabilities, without the target adversary, distinguish the challenge distributions? A trapdoor generated for a fresh independent object need not exist for the challenged object, even if their public marginals match.

If the test requires an unavailable trapdoor, an illegal query, or a changed challenge distribution, identify that missing capability. If it really works within the stated interface and cost, it is a candidate attack on the assumption, rather than automatically a defect in the target scheme. A reduction holding information unavailable to the adversary is not itself an error; justify that information under the reduction's experiment.

Localize a transition to its smallest interacting subsystem, then reconstruct the rest of the view. Shared parameters, authentication values, previous queries, and later checks can couple distant components. A conditional sampler, allowed oracle, or suitable multi-instance theorem can justify correlated surroundings; independence is sufficient for some arguments, not mandatory. The sampler must be executable using the challenge interface and meet the relevant time bound.

Return a local obligation: given a specified challenge and auxiliary state, an efficient algorithm generates the entire required hybrid view and translates a distinguisher's output into the claimed assumption violation, with explicit costs and error. Naming a hybrid does not establish this algorithm.

## Use restricted timing to expose a missing operation

For each relevant value, distinguish when it is fixed, known to the simulator, exposed, and later checked. Solve a restricted timing case only if doing so identifies the precise step that becomes unavailable in the target experiment. For example, a proof that hardwires a challenge-dependent value into a previously issued key needs a mechanism that explains that earlier key consistently without knowing the future value at issuance.

Delayed choice, equivocation, extraction, and reconstruction of coins are distinct candidate capabilities. None is supplied by the word “simulatable.” Keep adaptive queries, adaptive input selection, and adaptive party corruption separate. A restricted-order argument does not automatically handle any of them.

Check knowledge against the simulator's actual interfaces, not against the real party's knowledge alone. A different simulation schedule may be legitimate under the definition or a proved rewinding argument; it cannot be assumed merely because it makes construction easier. Real execution, simulation, hybrid order, and explanation order need not coincide. Likewise, composing two-message components can create additional global rounds if their messages depend on each other.

## Make probability and quantifiers part of the interface

State the needed bound before committing to a sampler or proof mode. Keep setup sampling, public exposure, adversarial selection, challenges, conditioning, and success in their actual order. A bound for each fixed input chosen independently of setup need not cover a malicious input chosen after setup. Require the guarantee the target experiment needs, without gratuitously demanding a stronger simultaneous statement.

For abort or rejection, derive the unconditional joint-event expression before simplifying it. A nonabort lower bound does not imply that useful distinguishing advantage survives on the retained transcripts. Identify a proved independence, transcript-uniform survival, or another quantitative argument if one is needed; artificial abort is a possible mechanism, not an automatic repair. Preserve runtime costs when proposing repeated sampling.

## Find a reusable operation or a precise escape from a barrier

When several constructions share a cost, state the common operation with its joint output law, algebraic constraints, size or norm bounds, public helpers, and hardness retained at each challenged component. Give distinct consumers when testing a claim of reuse. Satisfying an equation or compressing public material alone does not prove the required distribution or preserve hardness in the presence of that material.

For an existing negative result, list the hypotheses covering the scheme class, reduction access, assumption type, and security notion. Propose a specific change that leaves one hypothesis, then state what remains to be constructed. A limitation on a reduction class is not a universal impossibility; leaving its hypotheses does not establish a positive result.

End with a candidate lemma, a local derivation, or a precise incompatible set of requirements. Keep its status visible and identify which answer would change the next research step. Passing small examples does not discharge the full security claim.

## Origin and evidence

Adapted from the proposed methods in §§3 and 7–9 of the user-supplied *Learning from Brent Waters: A Cryptography Research Distillate* (research cutoff September 21, 2026). This is repository research guidance, not an attributed personal procedure or a claim that the report's sources have all been independently checked. Paper-specific claims require their own primary-source version and locator. The full report is not bundled, and adopting this reference does not establish improved research quality.
