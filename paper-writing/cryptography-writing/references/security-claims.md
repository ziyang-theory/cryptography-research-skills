# Security claims, experiments, and reductions

Use for formal statements and full proof drafting. Preserve the governing definition; organization and notation support the argument rather than determining validity.

## Specify the claim

State, or point to definitions fixing, the object and parameters; experiment or compared distributions; adversary resources, auxiliary information and oracle access; setup; quantifier order; success event and bound; assumptions and reduction loss; and corruption, composition, leakage, abort or delivery qualifications. Not every sentence needs the entire model.

Keep the intended target, active theorem, supplied reasoning, and implemented variant separate. Distributional correctness, exposed-key privacy, extraction, ideal-functionality realization, and distributed-setup security need their own support. Fixing a target instance/session does not by itself decide stand-alone versus UC scope: inspect the environment, interaction, and simulator interfaces. Place a qualification next to a headline whose meaning depends on it; avoid repeating it everywhere.

## Probability, quantifiers, and exposure

- Distinguish equal values, identical distributions, bounded statistical distance, and computationally indistinguishable ensembles. Retain the randomness and success event that define the probability space, and the baseline used for advantage.
- Index asymptotic claims by the security parameter. A fixed error such as `2^{-128}` is not itself a negligible function. Preserve uniformity of negligible bounds over allowed inputs and auxiliary strings; moving a bound inside those quantifiers can weaken the definition.
- For concrete claims retain actual resource bounds; do not substitute PPT language. Keep computational, statistical, field-size, query, and guessing terms separate until justified simplification.
- Preserve joint distributions and correlated auxiliary information. In particular, an exposed seed, key, witness, random tape, or shared oracle state remains part of the comparison when the definition retains it.
- Name the actual sampled ensemble. Independent uniform sampling, conditioning, seeded generation, bounded rejection with fallback, and reuse of one sampled component may differ. An algebraic or distance certificate need not transfer a computational hardness assumption to the implemented sampler.

Distinguish PPT and QPT, uniform and nonuniform algorithms, advice and auxiliary input, and classical versus quantum oracle access. State which participants receive the relevant interfaces.

## Make reductions executable

Given an adversary `A` violating the target property, describe how `B` uses it to solve the underlying problem. Specify the challenger interface, challenge embedding, supplied or generated state, permitted queries, final decision rule, runtime, and advantage relation. State black-box access, rewinding, programming, or quantum capabilities where they matter. A tighter certified bound for unchanged algorithms is not evidence of a matching attack against the older bound.

The reduction must generate the correctly distributed surrounding view. Independence is sufficient in some product hybrids, not necessary in general: conditional sampling, a permitted oracle, or a suitable multi-instance theorem may suffice. These mechanisms must be executable with the reduction's actual inputs and cost budget.

## Organize the proof around meaningful comparisons

For simulation, a useful default is to describe the simulator's inputs, interfaces, state, and behavior before comparing real and simulated executions. Follow a direct equality-of-distributions argument when it is clearer, including for perfect security. Do not add duplicate experiments, impose a label style, or change an existing proof merely to fit a template.

When hybrids clarify the argument:

1. Define experiments or indexed distributions over the observation space in the security definition, with enough setup, randomness, interaction, output, and retained state to make them unambiguous.
2. Identify the endpoints. Prefer exact endpoint distributions; explicitly justify and bound any gap to the claimed real or ideal execution.
3. For each transition, state the controlled change and update its causal consequences. Classify it as identical distribution, bounded statistical distance, or computational indistinguishability under a named premise. Justify the complete surrounding view, including conditioning and adaptive choices.
4. For repeated families, give a rule for each consecutive member and a uniform transition argument covering its index-dependent state and error. Identify the first and last members and their connections. A family name or ellipsis alone is insufficient.
5. Accumulate all statistical, computational, bad-event, and guessing terms. Each computational edge or justified family needs an applicable assumption, theorem, or closure lemma; the number of reductions need not equal the number of distinct assumptions.

For `p_i = Pr[D(H_i)=1]`, the telescoping bound is

`|p_0-p_m| <= sum_{i=0}^{m-1} |p_i-p_{i+1}|`.

A standard asymptotic argument uses polynomially many transitions with appropriately uniform negligible bounds. Turning endpoint gap `epsilon` into an adjacent gap of at least `epsilon/m` must account for how the reduction selects or is advised of the edge and any guessing loss. Exact conditional-distribution arguments can discharge zero-error transitions; they still need to match the full view.

## Retain the theorem's limits

Information-theoretic or unconditional security is relative to the named network, setup, oracle, or hybrid resources and any query bound. Instantiating an ideal resource needs its own matching theorem; a classical proof need not transfer to quantum access, and a stand-alone argument need not compose concurrently.

A mathematical proof does not certify implementation correctness or side-channel security. A functional prototype, field/key width, successful tests, or limited attack screen does not establish a concrete security level. Distinguish one-trial attack advantage, amplification cost, and the full reduction bound.

Use theorem/proof, proof sketch, heuristic, evidence, conjecture, or assumption according to the material's actual status. Leave an unsupported step visible rather than filling it with conventional-sounding prose.
