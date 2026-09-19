# Security claims, experiments, and reductions

Use this reference when drafting or editing a formal security statement, game-based definition, assumption, or reduction.

## Expose the definition's axes

A complete formal statement commonly fixes:

1. the object and its syntax, parameters, and correctness requirement;
2. the security experiment, execution, or compared distributions;
3. the adversary class, resources, auxiliary input, and oracle access;
4. the setup, hybrid, or ideal resources available to each algorithm;
5. the quantifier order over adversaries, simulators, distinguishers, inputs, and parameters;
6. the success event, baseline, advantage, distance, or failure bound;
7. the computational assumption and reduction loss, if any;
8. the resulting guarantee and any corruption, composition, leakage, abort, or delivery qualification.

Not every sentence must repeat the full definition. It must, however, point to a definition that fixes these axes or state the axes needed to avoid ambiguity.

## State the result at the right abstraction

A main theorem may name a precisely defined property rather than repeat its entire experiment. Introduce the object and distribution before the statement, name its assumptions and parameter regime, and point to the definition carrying the quantifiers. Concision must not combine different notions: distributional correctness, exposed-key privacy, knowledge extraction, realization of an ideal functionality, and security of distributed setup require their own supporting claims.

Keep the applicable statuses separate: the intended research target, the active theorem statement, the scope established by the supplied reasoning, and any implementation being evaluated. A new preliminaries paragraph or chosen model does not upgrade the proof. If a theorem fixes an instance or session, inspect the complete experiment before calling it stand-alone or UC: fixing a target session is compatible with different composition models; the decisive questions are the quantified environment, permitted interaction, and simulator interfaces.

State a recurring qualification where its scope is clear and refer back when useful. Keep it next to a headline whose meaning would otherwise change; avoid repeating the entire caveat in every sentence. Shortening a theorem, moving its proof, or presenting a concrete prototype does not remove the underlying limitation.

## Probability and distribution language

- Distinguish equality of values from **identical distribution** of random variables.
- Distinguish identical distribution from bounded **statistical distance** and from **computational indistinguishability** of indexed ensembles.
- State the probability space: key generation, protocol coins, oracle sampling, adversarial randomness, and any experiment randomness that matters.
- Name the success event in a game or experiment. If reporting advantage, preserve the definition's convention and identify its baseline; success probability and advantage are not interchangeable.
- For an asymptotic claim, index distributions and bounds by a security parameter. A negligible function is asymptotic: a fixed value such as `2^{-128}` should be reported as a concrete error or advantage, not called negligible by itself.
- For indexed ensembles, preserve whether one negligible function must bound all allowed inputs and auxiliary strings after the distinguisher is fixed. Do not move the negligible bound inside an input or auxiliary-input quantifier unless the definition does so.
- For a concrete claim, state the resource bound and resulting success or distinguishing bound. Do not add PPT language merely to make the prose sound formal.
- Do not replace a joint distribution by independently sampled marginals. This is especially important for correlated outputs and randomized functionalities.
- When a theorem has multiple security parameters or error sources, retain them separately. Examples include computational and statistical parameters, field-size error, adversarial oracle-query factors, and additive reduction error.

When the assumption or theorem concerns a sampled object, name its actual ensemble and exposed public description. Uniform independent sampling, sampling conditioned on a predicate, deterministic or seeded generation, bounded rejection with a fallback, and repeated use of one sampled component need not give the same joint distribution. A distance or algebraic certificate can justify that property without transferring the computational hardness assumption. Describe a practical variant separately when the theorem has not been shown to cover it; do not silently redefine the formal assumption to match the implementation.

In seed-, key-, or witness-exposure arguments, retain every value exposed by the definition, along with correlated auxiliary information and shared setup or oracle state. An output-only comparison does not automatically establish the required comparison with those values retained.

## Adversaries and efficiency

Say what is efficient under the definition:

- PPT for a classical probabilistic polynomial-time algorithm;
- QPT for a quantum polynomial-time algorithm;
- an explicit time, circuit-size, memory, communication, or query bound for concrete security.

Uniform and non-uniform adversaries, auxiliary input, advice, and oracle access are separate choices. Preserve each choice. For oracle models, distinguish classical queries from quantum superposition queries and say which participants receive access.

## Reductions

Write the direction explicitly: given an adversary `A` that violates the target security property, construct an algorithm `B` that solves the underlying problem or wins the underlying experiment. Then state, as applicable:

- how `B` runs or invokes `A`;
- what inputs, advice, or oracles `B` and `A` receive;
- whether the use is black-box or non-black-box when the theorem depends on it;
- `B`'s running time and query complexity;
- the relation between `A`'s advantage and `B`'s advantage, including additive errors and guessing factors;
- whether the reduction is classical or quantum and whether it rewinds or programs an oracle.

Call a reduction tight or non-tight only when the relevant resource and advantage loss have been established. A sequence of games or hybrids is a proof organization technique; each transition still needs an exact justification and the losses must be accumulated.

## Hybrid arguments

For a new simulation-based proof or an authorized substantial rewrite or completion, present the hybrids after describing the simulator, including for perfect security. A change in how an experiment samples or computes values can be a meaningful hybrid even when it preserves the observed distribution exactly. Justify the complete joint view and relevant retained state across such changes, including any conditioning; zero distinguishing advantage does not make a transition vacuous. Merely repeating the same experiment under a new label is not a meaningful change. Follow the entrypoint's requirement to explain any exception to this organization.

Define `Hyb_0, ..., Hyb_m` as complete experiments or indexed distributions over the observation space fixed by the security definition. Specify the security parameter, inputs and auxiliary input, setup and randomness, adversarial interaction, outputs, and state needed to make each hybrid unambiguous. Prefer `Hyb_0` and `Hyb_m` to be identically distributed to the claimed endpoints. If an endpoint differs, make that a separate transition and bound it; do not hide an endpoint gap in prose.

Present the argument one hybrid at a time, with a separate label and colon: `Hyb_0:`, `Hyb_1:`, and so on (`$\mathsf{Hyb}_0$:` in LaTeX). A descriptive family or corruption index is allowed, with consecutive numeric steps within each chain. Define `Hyb_0` first. For each `i >= 1`, define `Hyb_i` relative to `Hyb_{i-1}`, state what changes and what is inherited, and justify exactly that adjacent transition before introducing the next hybrid. A later endpoint comparison or telescoping sum does not replace these individual arguments.

For a parameterized repetition, give a complete rule for every consecutive index and a uniform proof of the edge `Hyb_{i-1}` to `Hyb_i`, including its index-dependent surrounding state and loss. Explicitly identify the first and last members and how they join the preceding and following hybrids. This avoids listing polynomially many copies without omitting any intermediate experiment; an ellipsis or grouped family name alone is insufficient.

For every adjacent pair:

- isolate one controlled semantic change and update all causally dependent fields needed to keep the experiment coherent; “one change” need not mean one literal variable or message;
- classify the relation as exact equality or identical distribution, statistical distance with an explicit bound, or computational indistinguishability under a named assumption or lemma;
- for a computational transition, state the challenger interface, where its challenge is embedded, how the reduction generates every unchanged component, how the distinguisher's output is translated, and the resulting runtime, query, and advantage loss;
- preserve the joint distribution of the surrounding view, including correlations, adaptive choices, conditional distributions, oracle state, and transcript-dependent behavior.

Independence is a convenient sufficient condition in an elementary product hybrid, not a general requirement. The actual obligation is that the reduction can efficiently generate the correctly distributed surrounding view, perhaps by conditional sampling, permitted oracle access, or a multi-instance assumption. Whether this is possible depends on the reduction's interface, not merely on whether a primitive uses public or secret keys.

For a standard asymptotic hybrid proof, require `m = m(lambda)` to be polynomially bounded. For a fixed distinguisher `D`, let `p_i = Pr[D(Hyb_i) = 1]`. Record the telescoping bound

`|p_0 - p_m| <= sum_{i=0}^{m-1} |p_i - p_{i+1}|`

and retain the individual exact, statistical, computational, bad-event, and guessing terms before simplifying. If an endpoint gap `epsilon` is converted into an adjacent gap of at least `epsilon/m`, account for how the reduction selects or is advised of the edge and for any resulting `1/m` loss. A polynomial number of negligible terms is negligible only under the required uniform bounds.

Do not require the number of reductions to equal the number of distinct assumptions. Instead, map every computational edge or justified family of edges to the exact assumption, theorem, or closure lemma that discharges it. One assumption may support many edges, and one reduction may batch several changes; multiplicity and all losses still belong in the final bound.

## Assumptions and proof scope

State assumptions precisely and treat them as assumptions or conjectures, not established facts. An information-theoretic or unconditional guarantee remains relative to its network, setup, oracle, and hybrid resources. State whether the execution assumes private or authenticated channels, atomic broadcast, ideal OT or OLE, correlated preprocessing, a random oracle, or another resource, and whether the comparison is perfect or statistical with an explicit error.

A proof of security is relative to its definition, model, and assumptions. It does not by itself establish:

- security of an implementation against side channels or implementation flaws;
- security after replacing an ideal primitive, oracle, or functionality without an instantiation theorem;
- concurrent or composable security from a stand-alone theorem;
- fairness or output delivery absent from the ideal functionality;
- post-quantum security from a classical reduction.

Use **theorem** and **proof** only for completed statements and reasoning. Use **proof sketch**, **heuristic argument**, **evidence**, **conjecture**, or **assumption** when that is the actual status.

An illustrative implementation can be described by what it establishes—functional behavior and measured costs at specified parameters—without assigning a concrete security level. Key or field width, successful validation, and a limited attack screen are not interchangeable with a security lower bound. Preserve the distinction between an attack's one-trial advantage, its amplified cost, and the reduction bound for the complete construction.

## Final claim audit

Before accepting a formal sentence, ask:

- What exact experiment, execution, or pair of distributions does it refer to?
- Who is quantified first, and what may later algorithms depend on?
- What resources and oracle access are available?
- What is the success event or distinguishing relation and bound?
- Which assumption supports the claim, and what loss does the reduction incur?
- What setup, composition, corruption, leakage, and output guarantees remain outside the claim?
