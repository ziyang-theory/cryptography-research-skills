# Proof systems, commitments, and oracle models

Use this reference for interactive or non-interactive proofs and arguments, PCPs and IOPs, zero knowledge, extraction, commitments, random oracles, setup, and succinctness.

## Proofs and arguments

Follow the manuscript's formal definition. Under standard modern usage:

- a **proof system** has soundness against computationally unbounded cheating provers;
- an **argument system** has soundness against the bounded prover class stated by the definition.

Some sources use “proof” informally for both. Do not replace a locally defined term merely to normalize style, but preserve the formal distinction in theorem statements and security definitions.

Keep the main properties separate:

- **Completeness** bounds rejection of valid instances under the honest prover and verifier; for a relation-based system, state the quantification over valid instance-witness pairs.
- **Soundness** bounds acceptance of false statements against the allowed cheating prover class.
- **Knowledge soundness** or a **proof/argument of knowledge** requires an extractor satisfying the definition; it is stronger than merely observing that an accepting statement has some witness.
- **Zero knowledge** compares the specified real verifier view or output with a simulated distribution. It is separate from soundness and knowledge soundness.

State completeness, soundness, and knowledge errors with their probability spaces. For knowledge extraction, state the extractor's access and resources when relevant: black-box or non-black-box access, transcript or oracle access, straight-line execution or rewinding, classical or quantum access, strict or expected polynomial time, and extraction or knowledge error. Rewinding is a technique, not a synonym for simulation or extraction.

Also name the extraction target: a witness, committed message, hidden batch index, or other source-defined object. Witness extraction, committed-message extraction, somewhere extraction, and trapdoor extraction are not interchangeable, and somewhere extractability does not by itself establish ordinary knowledge soundness.

## PCPs, IPCPs, and IOPs

For PCPs and IOPs, distinguish the prover's oracle strings from the locations read by the verifier. Report oracle or proof length, verifier query complexity, number and direction of ordinary messages, round complexity, prover time, and verifier time separately. In an IOP, later verifier computation may retain oracle access to earlier prover messages. Preserve the source's exact IPCP and public-coin conventions rather than inferring them from a generic label.

## Zero knowledge and witness indistinguishability

A zero-knowledge statement should name:

- the verifier class, such as honest-verifier or arbitrary malicious verifiers;
- the simulator and its inputs, auxiliary input, advice, and oracle access;
- the real and simulated random variables;
- whether the zero-knowledge guarantee is perfect, statistical, or computational, and the corresponding relation between the real and simulated random variables;
- any setup, programming, adaptivity, or concurrency scope.

“Reveals nothing” is acceptable only as intuition immediately tied to a formal definition. **Witness indistinguishability** hides which witness was used among allowed witnesses; it is generally weaker than zero knowledge and is not a synonym for it.

The adjective **adaptive** must name its object, such as adaptively chosen statements, oracle queries, corruptions, or proofs. Preserve whether choices occur before or after setup, oracle sampling, prior transcripts, or prior answers.

## Commitments

Keep commitment properties independent:

- **hiding** protects the committed message from the receiver before opening;
- **binding** prevents the committer from opening one commitment inconsistently, under the definition's quantifiers and computational bounds;
- **extractability** supplies an extractor for the committed value under a separate definition;
- **equivocation** supplies a simulator that can produce a simulated commitment with the allowed opening behavior;
- **homomorphism** is an algebraic property and does not imply the security properties above.

State whether each property is perfect, statistical, or computational and which party may be malicious. Equivocation in a simulation does not mean an honestly generated commitment fails binding. A commitment scheme and an ideal commitment functionality are different objects.

## Random-oracle terminology

A random oracle is a single uniformly sampled random function with the specified domain and range, exposed through oracle queries to the participants named by the model. For classical oracle access, lazy sampling gives a stateful implementation of that shared function; it does not create an independent oracle for each caller. Do not carry this classical table-based account into the QROM without a quantum-accessible formulation.

Keep these objects and models separate:

- a concrete hash function;
- a keyed pseudorandom function;
- a random oracle in the ROM;
- a quantum-accessible random oracle in the QROM;
- a common or structured reference string;
- a programmable, non-programmable, or restricted-programmability oracle model.

A ROM proof does not automatically transfer to a concrete hash-function instantiation; describe such an instantiation as heuristic unless a separate theorem justifies it. Specify who may query the oracle and whether queries are classical or quantum.

When saying that a simulator or reduction **programs** the oracle, identify the permitted interface. Relevant distinctions include supplying a finite set of programmed query-answer pairs, choosing programmed points or answers adaptively, and implementing the oracle interface while forcing selected answers and maintaining consistency. State who programs, when points are chosen relative to adversarial queries, and whether a point may already have been queried. Merely answering fresh queries by lazy sampling is not oracle programming, and the ROM alone does not grant programmability.

A bounded-query random-oracle theorem against a computationally unbounded adversary is not a standard PPT ROM theorem. State the query budget, who receives oracle access, whether the simulator may program the oracle, and whether the claimed error is statistical within that oracle model. Replacing the oracle with a concrete hash function does not preserve the model or automatically turn the theorem into a computational or statistical standard-model claim.

Separate oracle sharing scope from programmability and composition scope. Specify whether participants share one oracle within a protocol instance, instances have independent oracles, or arbitrary outside protocols and the environment access a global resource. Then specify the real and ideal interfaces and the simulator's permitted control. Calling an oracle local does not itself limit a theorem to stand-alone security, and calling it global does not establish UC security. Session tags can separate query domains; they do not by themselves establish multi-session composition or prevent outside parties from making the same encoded queries.

For a Fiat--Shamir compilation, state the source protocol's challenge-generation structure and any public-coin hypothesis required by the invoked theorem, what transcript data determines each challenge, the result's oracle or setup model, and the theorem transferring soundness, knowledge soundness, or zero knowledge. Preserve query-dependent loss and any state-restoration, round-by-round, or programmability hypothesis; non-interactivity alone establishes none of these properties.

Distinguish literal independent verifier challenges, a transmitted seed expanded into challenges, and transcript-derived challenges. Already using a random oracle elsewhere does not discharge the transformation's soundness, extraction, or simulation obligations. Identify which values must be fixed before a challenge is learned, what binds them, and whether an adversary can try multiple candidates. Derive any query-dependent bound from that experiment rather than importing the original independent-challenge bound.

## Succinctness, rounds, and setup

Treat **succinctness** as a quantified efficiency claim, not a decorative synonym for “short.” State the relevant measure and baseline:

- proof or argument length;
- total communication;
- verifier time or query complexity;
- prover time;
- dependence on the instance size, witness size, circuit size, security parameter, and error.

Separate prover time, verifier time, oracle queries, messages, communicated bits or symbols, and rounds. If a source counts one back-and-forth exchange as a round, say so or report the number of messages and speaking order.

Name the setup resource precisely: CRS, SRS, public parameters, random oracle, preprocessing key, or other functionality. **Transparent** setup normally describes how public randomness or parameters are generated; it does not necessarily mean that no setup or preprocessing exists. State trust, parameter dependence, updateability or reuse, and offline cost only when supported by the definition or construction.

“Without a trusted setup” excludes a trusted parameter-generation process under the stated model; it does not by itself exclude a random oracle, transparent public randomness, preprocessing, or another ideal resource. Name every remaining model resource.
