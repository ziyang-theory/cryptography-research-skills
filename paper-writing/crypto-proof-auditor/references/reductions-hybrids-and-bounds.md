# Reductions, hybrids, and bounds

Use this reference to audit reductions, game hops, hybrid arguments, bad events, conditioning, concrete loss, and tightness.

## Reduction contract

For a reduction `B^A`, record:

- the target security violation attributed to `A`;
- the exact underlying problem or experiment that `B` must solve;
- the challenge distribution embedded for `A`;
- setup, keys, trapdoors, advice, randomness, and oracle interfaces available to `B` and `A`;
- whether access is black-box, non-black-box, classical, or quantum;
- runtime, memory, and query overhead;
- the exact relation between the target advantage and `B`'s success or advantage.

Verify the direction: a successful target adversary must yield an algorithm violating the named assumption. Check that `B` can sample the entire environment seen by `A`, answer every request consistently, and translate `A`'s success event into its own without circularly assuming the target claim.

Audit all guessing, artificial-abort, rejection-sampling, conditioning, fork, rewind, and bad-event factors. A reduction that succeeds conditioned on a `1/N` guess normally incurs that factor. If the reduction repeats until a rare event, check both its distribution and expected or strict running time.

## Hybrid transitions

For a hybrid argument, make every adjacent change explicit and retain the source's labels when reporting findings. Direct distributional arguments, games, and other valid representations are assessed on their mathematical obligations, not their notation. Exact changes in sampling or computation may be meaningful even when the observed joint distribution and retained state are unchanged.

For a repeated indexed family, verify a complete rule for every consecutive index and a uniform justification of `Hyb_{i-1}` to `Hyb_i`, with the correct surrounding state and bound for each transition. Check the endpoints and their connections to neighboring hybrids. An ellipsis must not conceal an undefined experiment or unjustified jump. A table can help with a long chain:

| Edge | Changed component | Relation | Justification | Bad event | Advantage bound | Reduction cost |
| --- | --- | --- | --- | --- | --- | --- |

Check that:

- `Hyb_0` is the required starting experiment and `Hyb_m` is the claimed endpoint, or every boundary discrepancy is exposed as a separate bounded transition;
- every hybrid is a complete, well-defined experiment over the required observation space and is efficiently emulatable wherever a reduction must generate it;
- each edge makes one controlled semantic change and changes only the components covered by its justification, while coherently updating any causally dependent state or messages;
- exact equality, statistical distance, and computational indistinguishability are not interchanged;
- each computational edge or justified family of edges names the exact assumption or lemma that discharges it, and any reduction records its challenger interface, challenge embedding, output translation, and loss;
- the reduction can sample the unchanged surroundings with the correct joint correlations, conditional distributions, and oracle or transcript state;
- transcript-dependent and adaptive choices retain their distribution;
- conditional transitions are converted back to unconditional bounds;
- an identical-until-bad step supplies a coupling or first-divergence argument, names the game in which `Pr[bad]` is bounded, and justifies any transfer of that probability between games;
- all bad events are bounded across parties, sessions, queries, and hybrids;
- the number of hybrids is polynomially bounded when efficiency and asymptotic negligibility rely on it;
- the total loss includes the triangle-inequality, union, or game-sequence accumulation, including any random-index, guessed-edge, or non-uniform-advice factor.

Independence is sufficient for the elementary product hybrid but is not necessary in general. Audit whether the reduction can generate the correct surrounding joint or conditional distribution; this may instead use conditional sampling, permitted oracle access, or a multi-instance assumption. Do not infer simulability merely from the primitive being public-key, or its failure merely from the primitive being symmetric-key: inspect the actual challenge and oracle interface.

Do not compare the number of reductions with the number of distinct assumptions. Verify instead that every computational edge or edge family is discharged. One assumption can be invoked many times, and one reduction or closure lemma can justify several edges; count every invocation and loss that affects the final bound.

A sequence of hybrids is a proof technique; an `F`-hybrid model is an ideal-resource model. Do not use one to justify the other.

## Probability and advantage bounds

State separate bounds for:

- correctness failure;
- statistical or simulation distance;
- computational distinguishing advantage;
- field, code, or interpolation failure;
- extraction or knowledge error;
- oracle collision, pre-query, and programming error;
- cut-and-choose, repetition, and session error;
- guessing, abort, and hybrid factors.

Do not collapse independent parameters or error sources into a single symbol unless the theorem proves the stated relation. If `m` adjacent hybrids each cost at most `epsilon`, the direct bound is normally `m epsilon`, even when polynomial `m` preserves negligibility. A fixed value such as `2^{-128}` is a concrete error, not itself a negligible function.

For a fixed distinguisher `D`, write `p_i = Pr[D(Hyb_i) = 1]` and verify

`|p_0 - p_m| <= sum_{i=0}^{m-1} |p_i - p_{i+1}|`.

If the proof infers from endpoint advantage `epsilon` that some edge has advantage at least `epsilon/m`, check how the reduction selects that edge and whether a `1/m` factor, a sign choice, or non-uniform advice is being used. A superpolynomial chain, or non-uniform per-edge negligible bounds without a common polynomially controlled bound, does not automatically preserve negligibility.

## Assumption and parameter mapping

Verify that the reduction's output lies in the assumption's required class and parameter regime. Check:

- uniform versus non-uniform algorithms and advice;
- PPT versus QPT and classical versus quantum oracle access;
- assumption instance size and distribution;
- query, circuit-size, memory, and time bounds;
- auxiliary input and adaptive choices;
- whether the assumption is decisional, computational, extractive, knowledge-based, or correlation-intractable in the exact form invoked.

Treat conjectured code distance, heuristic hash instantiation, ideal-permutation modeling, and unproved correlation robustness as assumptions or evidence, not completed reductions.

## Sampler changes and exposed information

Compare the actual ensembles, not just the generation algorithm's name. Record public seeds and descriptions, conditioning predicates, search bounds, fallback behavior, independence, component reuse, and what the adversary learns. An algebraic or minimum-distance certificate establishes its own property; it does not automatically transfer computational hardness to a differently sampled public object.

For a claimed transfer through conditioning, determine whether the implemented distribution is exactly the original one conditioned on the stated event. Check the event's probability, whether the reduction can recognize or sample it using its permitted information, and how conditioning affects both compared worlds. Derive the advantage and running-time factors. Reusing a selected component may change correlations in a way that cannot be modeled as deleting a rare bad event.

For many-instance privacy from a single-instance theorem, check the challenge interface, permitted auxiliary information, shared parameters and oracle state, freshness of generation coins, and adaptive choice of instances. The reduction must generate the other instances and all correlated side information with the correct joint distribution. Correlated descriptions alone do not refute the reduction; fresh local coins alone do not establish it. Verify any invoked single-instance theorem in precisely this interface and accumulate the number of replacements and their resource budgets.

If an adversary receives an actual seed or key, retain it in the compared view. Showing security of the expansion outputs after dropping that seed does not prove the exposed-seed statement. Likewise, a public matrix's marginal distribution cannot be substituted for its joint distribution with the public seed or certificate that describes it.

## Tightness and theorem matching

Call a reduction tight only after comparing the relevant time, query, and advantage functions. A polynomial loss can preserve an asymptotic theorem while materially changing a concrete claim. Compare the final derived bound with the theorem statement, abstract, parameter table, and claimed security level; preserve every additive term and parameter restriction that affects the result.

A limited attack screen can bound one attack's behavior on specified instances without lower-bounding security against all attacks. Keep one-trial advantage, success amplification and its work, underlying-assumption attacks, and complete-construction attacks separate. A reduction's upper bound on construction advantage does not turn a discovered weakness of an assumption into a matching attack on the construction; trace the reduction direction before drawing that conclusion.
