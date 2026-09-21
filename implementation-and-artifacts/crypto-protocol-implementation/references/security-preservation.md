# Security preservation and proof reuse

Use this reference to identify the security obligations of an implementation change. It guides change-impact analysis; it does not turn an implementation request into a full proof audit or require mechanization.

## Identify the contract used by the caller

Locate the governing protocol definition/theorem, the executable specification or reference implementation when available, the changed source, and the build target. Identify which connection the change affects. If a layer or supporting argument is absent, record the missing connection rather than inventing a verified specification.

A security-relevant contract can cover mathematical outputs, state transitions, messages and lengths, parsing/rejection behavior, abort and output delivery, corruption-exposed state, joint randomness, allowed interleavings, and leakage. Select observations from the intended adversary and execution model. Equal honest return values do not cover secret logging, secret-dependent memory access, or newly accepted malicious behavior.

For a stateful cryptographic component, especially preprocessing or a correlation generator, resolve:

- Its algebraic relation and complete joint distribution, including auxiliary information exposed to corrupted parties.
- Who chooses inputs, keys, indices and queries, and when those choices can depend on earlier observations.
- Ownership of secret state, one-use material, persistent keys, session identifiers, and permitted sharing across calls or modules.
- Setup and oracle access, call/output limits, failure and leakage behavior, and the caller's corruption, composition and output guarantees.

A matching function signature or honest algebraic relation is insufficient. For a PCG replacement, identify the pseudorandomness claim with the specified seed/key exposure retained. A seed expander replacing ideal randomness needs a matching cryptographic argument.

## Classify the semantic change

More than one row can apply. A small edit to a verifier or challenge schedule can affect the protocol theorem.

| Change | Obligation to identify |
| --- | --- |
| Representation or local algorithm: packed limbs, SIMD, loop fusion | Same specified values and relevant effects under actual caller preconditions; memory safety and applicable leakage property |
| Circuit, gadget or arithmetic/Boolean representation | Preserved functionality, numerical semantics and allowed leakage; constraints enforce the intended relation against adversarial witnesses |
| Sampler or randomness reuse | Complete joint distribution, or a quantified statistical/computational replacement with the allowed exposed state |
| Primitive or preprocessing replacement | The exact component security contract and composition hypotheses used by the caller |
| Batching checks, moving challenges, merging rounds or moving work into preprocessing | Changed adversarial choices and observations, simulation or game transitions, abort/output behavior and bounds |
| Parameters: field, seed, error distribution or repetitions | Theorem admissibility, revised concrete bounds and justification of the instantiated hardness assumption |
| Local parallelism, concurrent sessions or new scheduling | State separation, intermediate observations, random-stream allocation and applicable scheduling/composition conditions |
| Compiler, flags, intrinsics, FFI, assembly or target CPU | Validity of the source-to-executable argument and leakage analysis for the selected build |

Distinguish local parallel evaluation from changing the distributed message schedule. Independent arithmetic tasks do not establish independence of their random streams or permit shared secret state across sessions. Record when intermediate results become observable; a final-output equivalence may exclude those observations.

## Determine what can be reused

**Same contract, new implementation.** Either relate both implementations to a stable specification or justify an old-to-new equivalence. The relation must preserve the observations, probability distributions and adversarial interactions required by the security definition. Ordinary inclusion of allowed outputs or traces can be too weak for probabilistic or adversarially scheduled code. Reuse the caller's argument only if it uses no stronger property than the re-established contract.

**Same security contract, new cryptographic component.** Locate the component theorem and the composition or instantiation result that permits substitution. Match corruption interfaces, setup, shared keys/state, session separation, query limits, scheduling and abort/output behavior. A stand-alone theorem does not automatically support concurrent or UC use. An authorized change of wire encoding can require an interface adapter and parsing/rejection argument; security need not require identical transcript bytes when the applicable definition instead compares realizations of the same functionality with its specified public leakage.

**Changed contract or distribution.** State the proposed new contract and identify the affected callers, assumptions, simulator steps or hybrid transitions. Localize new reasoning to those dependencies without assuming that a small textual patch suffices. Record the exact compared experiments/views and classify each proposed replacement as exact, statistical or computational. Leave unsupported replacements open rather than treating a successful test as their justification.

When a replacement argument is supplied, check its direction: an allowed adversary against the modified object must be converted to one covered by the existing argument. Retain the governing quantifiers, available oracle/setup interfaces, simulator dependencies, reduction overhead and query bounds. Account for every changed experiment and repeated replacement in the definition's advantage convention; do not assign a universal additive error per code edit. Use [specification and distributions](specification-and-distributions.md) for history-dependent sampling and challenge timing.

## Keep a proportionate change record

Use the project's existing review or implementation notes to connect: old/new source identities; changed contract and affected dependencies; proposed equivalence, component theorem or reduction; revised parameter/bound status; focused validation and remaining obligations. Distinguish an obligation merely identified, an informal argument, a checked formal result, and a trusted assumption.

For an implementation-only request, make the authorized code change and report any unresolved security support without rewriting the paper to fit it. If the requested deliverable requires preserving a guarantee that remains unsupported, report that limitation explicitly. A proof-validity audit can use `crypto-proof-auditor` when available; this reference remains usable without that companion.
