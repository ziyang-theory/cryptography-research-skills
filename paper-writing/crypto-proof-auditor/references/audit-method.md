# Proof-audit method

Use this reference for the general logical and mathematical core of a cryptographic proof audit. Follow the source's exact definitions and use precise cryptographic terminology; `cryptography-writing` supplies optional further guidance. This reference tests whether the obligations are actually discharged.

## Fix the audited surface

Record the exact theorem, lemma, proof section, definitions incorporated by reference, source revision, and source anchors. Distinguish:

- a local inference audit;
- a theorem-and-proof audit;
- a full security-claim audit including definitions and imported results;
- an attempt to complete or repair a proof.

Do not quietly expand a scoped audit into a claim about the whole paper. External leaves remain unverified until checked against the cited primary source and the exact version used by the manuscript.

Resolve the active entrypoint, conditional text, and stable theorem labels when multiple versions exist. A comment, older PDF, review attachment, or previous proposed repair is evidence of history, not automatically the current claim. Keep the author's intended security target distinct from what the current statement and proof establish; a model declaration cannot supply missing quantifiers or simulation obligations.

## Normalize the theorem contract

For every quantified object, record what it may depend on. A proof that fixes an input `x` and then constructs `S_x` does not establish a definition requiring one simulator chosen before all inputs.

Capture at least:

| Field | Audit question |
| --- | --- |
| Objects | Which protocol, scheme, relation, functionality, distributions, or algorithms are quantified? |
| Parameters | Which security, statistical, field-size, circuit-size, query, and party-count parameters vary? |
| Quantifiers | In what order are adversaries, simulators, extractors, inputs, witnesses, auxiliary inputs, setup, and randomness chosen? |
| Resources | Which channels, oracles, setup, ideal functionalities, preprocessing, and persistent state are available? |
| Hypotheses | Which algebraic, efficiency, threshold, corruption, and parameter constraints are required? |
| Conclusion | Is the claim correctness, privacy, realization, extraction, soundness, zero knowledge, rounds, or efficiency? |
| Bound | What probability space, comparison relation, baseline, error, distance, or advantage is claimed? |
| Scope | Is the result stand-alone or composable, one-shot or reusable, classical or quantum? |

Reproduce the governing definition; do not replace it with a familiar template.

If a theorem abbreviates its conclusion as “secure” under an earlier definition, expand that definition for the audit. In particular, verify whether correctness means only an algebraic relation or a specified joint output distribution. Do not add a realization, knowledge, or setup-security claim merely because it would make the final application convenient.

## Build and audit the dependency graph

Use nodes for definitions, assumptions, imported theorems, local lemmas, parameter inequalities, protocol invariants, and final claims. Label each edge with:

- the exact result invoked;
- the object and parameter substitution;
- all side conditions;
- the portion of the conclusion consumed;
- the error, distance, or reduction loss contributed;
- any model, resource, or interface boundary crossed.

For each edge, ask:

1. Are the domains, types, dimensions, and ownership conventions compatible?
2. Are all hypotheses established at the call site?
3. Is the proof using a stronger conclusion than the dependency supplies?
4. Are quantifier order and uniformity preserved?
5. Do setup, oracle, adversary, corruption, output, and composition models match?
6. Are runtime, query, round, and error losses propagated?

Every conjunct of the root theorem needs a dependency path. Detect circular reasoning; a cycle requires an explicit simultaneous induction, fixed-point argument, or other well-founded justification.

## Type-check algebra and protocol state

Maintain a symbol table with each symbol's domain, codomain, dimension, randomness, ownership, and lifetime. Check:

- scalar, vector, matrix, group, ring, field, and extension-field operations;
- index ranges, empty sums, off-by-one cases, and output lengths;
- nonzero and invertibility premises before division;
- rank, distance, threshold, access-structure, and interpolation hypotheses;
- injective or unambiguous encodings and domain separation;
- initialization and preservation of state, transcript, and induction invariants;
- consistency of shares, masks, authentication tags, openings, and decoded outputs.

A numerical test can refute a universal identity but cannot prove it for all parameters.

## Audit probability and conditioning

Reconstruct the joint probability space: setup, keys, preprocessing, protocol coins, adversarial coins, oracle sampling, randomized functionality outputs, and any experiment randomness.

Check:

- equality of joint distributions, not only their marginals;
- pairwise versus mutual independence;
- unconditional versus conditional independence;
- whether a conditioning event has positive probability;
- whether abort, rejection, rewinding, or adaptive selection biases allegedly fresh randomness;
- whether a product or repetition bound has the needed independence or conditional bound;
- whether all events in a union bound are defined on a common probability space and every per-event bound holds simultaneously over the summed index set.

A union bound requires neither independence nor one common bound: nonuniform bounds `Pr[E_i] <= delta_i` are valid when their sum is controlled. If the proof reuses a single `delta`, verify that it holds uniformly for every summed index. Conversely, small joint-occurrence probabilities do not imply the complement-conditioning bound needed by a lopsided or adaptive argument.

## Audit asymptotics and uniformity

Record which quantities tend to infinity and which may depend on which others. Check:

- pointwise versus uniform negligible, `o(1)`, and big-O bounds;
- independence of hidden constants from every varying parameter;
- polynomial versus superpolynomial numbers of events, hybrids, queries, or sessions;
- fixed concrete errors versus asymptotic negligible functions;
- separate computational, statistical, field-size, extraction, and query-dependent errors;
- the order in which constants, thresholds, and security parameters are selected;
- strict versus expected polynomial time;
- boundary values, integer rounding, empty domains, zero-gate circuits, and maximal allowed corruption.

A zero-width or omitted-component benchmark can be a useful separate variant while lying outside the theorem's domain. Check that parameter limits still define every sampled set and operation; do not silently extend the theorem to accommodate an experiment.

Do not sum exponentially many negligible quantities without a uniform quantitative bound. Do not choose a threshold after obtaining constants that themselves depend on that threshold.

## Search for counterexamples without overclaiming

For a disputed implication:

1. Negate the exact obligation rather than the final theorem by default.
2. Freeze irrelevant parameters and try the smallest admissible domain.
3. Test degenerate objects, correlated distributions with matching marginals, boundary corruption thresholds, repeated identifiers, and earliest or latest abort.
4. Use bounded exhaustive search, a CAS, SAT, or SMT only when the finite model faithfully represents the obligation and the result is reproducible.
5. Record every hypothesis satisfied by the candidate.

A counterexample to an intermediate step shows that step is invalid; it refutes the theorem only if it satisfies the theorem's hypotheses and violates its conclusion. Failure to find a counterexample leaves an unsupported obligation unsupported.

## Evidence standard

Flag a finding only when it identifies a precise failed obligation, materially affects the audited claim or its intelligibility, and is supported by a derivation, model mismatch, counterexample, or explicit missing dependency. Keep speculative concerns as questions. Separate a source omission that is derivable from existing premises from a substantive gap requiring a new idea.
