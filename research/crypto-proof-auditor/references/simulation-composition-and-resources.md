# Simulation, composition, and resources

Use this reference for real/ideal security proofs, simulator validity, malicious behavior, abort and leakage, protocol scheduling, composition, session reuse, and ideal-to-concrete instantiation.

## Simulation contract

Start from the governing definition and compare its exact random variables. Audit:

- the order of quantifiers over real adversaries, simulators, environments or distinguishers, inputs, auxiliary inputs, setup, and security parameters;
- the real and ideal endpoints, including the adversary's output and all relevant honest outputs jointly;
- the simulator's granted inputs, leakage, ideal calls, setup, oracle access, trapdoors, and persistent state;
- corrupted-party cases, malformed messages, rejects, aborts, and output schedules;
- strict or expected running time and any rewinding or restart behavior;
- classical or quantum access and static or adaptive corruption.

The simulator may not use an honest input, future message, output, corruption state, or trapdoor unavailable through the ideal execution. If the proof extracts an effective corrupt input, check when extraction completes, what happens on failure, and whether the value is submitted before the functionality or schedule requires it.

For a UC claim, check the actual environment quantification and online interactions, including message scheduling, input delivery, outputs, and auxiliary communication. A theorem can analyze an arbitrary target session within a composable experiment; the words “fixed session” alone settle neither validity nor composition scope. Conversely, a comparison of fixed-input final outputs alone does not discharge an interactive-environment definition.

Matching individual output marginals does not match a randomized functionality's joint output distribution. Check correlations among honest outputs, adversarial output, abort, and any later session feedback.

## State, adaptivity, and causality

Construct a trace or happens-before table when timing matters:

| Step | Sender or resource | Recipient | Available dependencies | Adversarial action | State update | Output or abort |
| --- | --- | --- | --- | --- | --- | --- |

Use it to detect:

- a supposedly simultaneous message that depends on its peer's same-layer message;
- hidden ideal calls or setup interactions inside a round claim;
- preprocessing that depends on online inputs;
- simulator or extractor use of unavailable future information;
- oracle programming after the point may already have been queried;
- adaptive-corruption openings inconsistent with exposed messages or erasure rules;
- rewinding of external or concurrent state that cannot be rewound;
- output release followed by an abort decision not allowed by the claimed functionality;
- reuse of one-time randomness, correlations, keys, or receiver messages.

Name what **adaptive** modifies. Adaptive corruption, input selection, statement selection, queries, and programming create different proof obligations.

## Abort, leakage, and delivery

Read the ideal functionality or execution rather than inferring a hierarchy from labels. Determine:

- which party learns which output first;
- who can suppress or replace whose output and at what time;
- whether abort can depend on protected inputs, outputs, predicates, malformed values, or targets;
- whether one, some, or all honest parties are affected;
- which input lengths, circuit descriptions, access patterns, failure bits, transcripts, and auxiliary information are exposed;
- whether output or abort feedback affects later sessions.

Do not promote security with abort to fairness, simultaneous output, or guaranteed output delivery. Treat input-dependent, correlated, wire-triggered, selective-failure, and other qualified abort notions as source-defined until their functionality is inspected.

## Composition and sessions

For every composition step, locate the exact theorem and check:

- stand-alone, sequential, concurrent, or UC premises;
- scheduling and subroutine-respecting conditions;
- session and subsession identifiers;
- fresh randomness versus shared setup or state;
- overlapping inputs and outputs;
- the number, nesting, and concurrency of resource calls;
- simulator running-time requirements;
- whether the replacement exposes the same interface.

A per-session simulator does not establish joint security for adaptively selected sessions with shared state, outputs, or abort feedback. One-shot security does not imply bounded or polynomial reuse, and a stateless proof does not establish reactive security.

## Ideal-to-concrete boundaries

For every ideal primitive, oracle, setup, preprocessing resource, or PCG:

- match syntax, roles, outputs, and security notions;
- state who generates it and under what trust or setup assumption;
- count invocations and identify one-time versus reusable material;
- preserve circuit, input, identity, party, relation, and session dependence;
- include seed, setup, malformed-resource, and accept/reject views;
- identify the composition or instantiation theorem crossing the boundary.

Perfect or statistical online security in an ideal-resource hybrid does not become end-to-end information-theoretic security after computational setup or preprocessing. A ROM theorem does not justify replacing the oracle with a concrete hash absent a separate theorem; label heuristic instantiation as such.

When a resource theorem and a consuming-protocol theorem are claimed to imply a final result, audit the explicit replacement wrapper. Compare trusted honest generation, corrupted-party input selection, exposed private seeds, local expanded values, and abort interfaces. If the resource theorem preserves an exposed seed while replacing the other party's output, determine whether this supplies exactly the distribution the consuming simulator needs and whether it can produce the full interaction causally. Then combine the error and reduction budgets. Matching honest outputs is insufficient to infer realization of an ideal resource with a richer malicious interface. Classify an unstated connection as an unproved obligation unless it has actually been derived; it is not by itself evidence that composition is impossible.

## Construction-specific non-implications

Use these as audit probes, not as claims that every source makes the mistake:

- FSS correctness does not imply FSS privacy or verifiability.
- PCG correctness, stretch, or local expansion does not by itself realize an ideal correlation functionality.
- Garbling correctness, privacy, obliviousness, or authenticity alone does not establish malicious 2PC.
- Non-reconstruction does not imply secret-sharing privacy, and linear sharing does not imply multiplication or strong multiplication.
- A randomized correlation and its chosen-input functionality require an explicit conversion when they have different syntax.
- Component or online security does not establish the security of the composed, concretely instantiated system.

Use the manuscript's local role names and equations. Do not universalize source-specific notions such as robustness, fully black-box access, or named weakened-abort functionalities.
