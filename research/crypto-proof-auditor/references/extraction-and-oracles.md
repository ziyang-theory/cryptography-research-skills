# Extraction, proof systems, and oracle models

Use this reference for proofs and arguments of knowledge, commitments, PCPs or IOPs, extractor interfaces, random oracles, Fiat--Shamir transformations, and ROM or QROM claims.

## Separate the claimed properties

Audit completeness, soundness, knowledge soundness or extraction, and zero knowledge independently. A sound argument need not be an argument of knowledge; zero knowledge does not imply soundness; witness indistinguishability is not zero knowledge.

Identify the extraction target exactly:

- a relation witness;
- a corrupt party's effective input;
- a committed message;
- a hidden batch index or source-defined “somewhere” object;
- another explicitly defined object.

Extracting one object does not establish a stronger or differently quantified knowledge claim.

## Extractor contract

Record:

- black-box or non-black-box access;
- transcript, code, trapdoor, oracle-query tape, or next-message access;
- straight-line execution, rewinding, forking, or state restoration;
- strict or expected running time;
- extraction or knowledge error and its relation to acceptance probability;
- auxiliary input, advice, adaptive statement selection, and repeated sessions;
- compatibility with concurrency, UC, adaptive corruption, and quantum access.

Check that the extracted object satisfies the claimed relation and remains consistent across multiple openings, sessions, or extractions. An expected-time extractor nested in an adversary-controlled loop may cease to be polynomial time. Rewinding an isolated prover does not automatically justify rewinding a concurrent environment, external state, or a quantum adversary.

For special-soundness or forking extraction, verify that the accepting transcripts share the statement and every required prefix or state, have suitably distinct challenges, and satisfy the source theorem's acceptance conditions. Derive the probability and running time for obtaining such a fork. Ordinary soundness is not itself the step that converts accepting forks into a witness.

## Commitments and equivocation

When a proof uses commitments, audit hiding, binding, extractability, and equivocation as separate properties under their stated party and setup assumptions. Verify that simulated equivocation does not conflict with honest binding, that extraction occurs at the required time, and that malformed commitments or openings follow the governing interface.

## PCP and IOP obligations

Keep prover oracle strings, verifier queries, ordinary messages, rounds, proof length, prover time, and verifier time separate. Check whether later verifier computation retains access to earlier oracle messages and whether the invoked compiler requires public coin, state restoration, round-by-round soundness, or another source-defined property.

Ordinary soundness cannot replace a stronger state-restoration or knowledge property merely because both are called soundness in prose.

## Random-oracle and permutation audit

Record the exact object: a random oracle, random permutation, keyed function, concrete hash, CRS, SRS, or other setup. State who has classical or quantum access, the query budget, domain separation, and whether the model explicitly permits programming.

Whenever freshness or min-entropy is claimed, identify who chooses every allegedly random component in the adversarial execution. Entropy from an honest-generation algorithm cannot be imposed on a malicious prover or protocol party that controls that value.

Distinguish three independent choices: oracle sharing scope, simulator programmability, and the intended composition model. Map access in each world: parties, adversary, simulator, environment, and outside protocols. A local instance may be shared by its participants without being a globally available setup resource; a global resource remains governed by its specified ideal-world interfaces. Neither a UC label nor session-domain separation grants the simulator control of an external oracle. Do not assume a local-oracle proof covers arbitrary outside access to the same domain.

Check that:

- one shared stateful oracle or permutation is maintained consistently;
- a QROM proof does not assume a generic classical query tape: measuring superposition queries disturbs state, arbitrary quantum auxiliary state cannot be cloned and restored, and classical rewinding or forking needs a matching QROM theorem;
- lazy sampling is not mislabeled as programming;
- programmed points were fresh, or an already-queried bad event is defined and bounded;
- inverse queries remain consistent when programming a permutation;
- adaptive programming preserves the required transcript distribution;
- a programmable-model theorem is not promoted to a non-programmable model;
- a classical ROM proof is not promoted to QROM;
- bounded-query statistical security is not mislabeled as a standard PPT ROM theorem;
- concrete-hash use is not presented as a proved instantiation without a matching theorem.

## Fiat--Shamir audit

For each Fiat--Shamir application, verify:

- the source protocol's challenge-generation structure and every public-coin or round-specific hypothesis of the invoked theorem;
- the exact transcript prefix, statement, session identifier, and domain separation bound into each challenge;
- the resulting oracle or setup model;
- the transferred property: soundness, knowledge soundness, zero knowledge, or a subset;
- state-restoration, programmability, rewinding, collision, and pre-query conditions;
- adversarial query factors and accumulated loss.

Replacing verifier messages with hashes does not by itself establish non-interactive soundness, knowledge extraction, or zero knowledge, and it does not yield a standard-model theorem.

Audit literal fresh challenges, receiver-sent expanded seeds, and transcript-derived challenges as distinct variants. Identify the error, commitment, statement, or other checked object that must be fixed before challenge revelation, and verify how the transcript binds it. If the adversary can search over candidate transcripts, include its query budget and derive the conditional per-attempt bound before applying a union bound. A cancellation estimate for a fixed error is only one obligation; it need not establish extraction, simulation, or security of the full transformed protocol. Prior use of the ROM elsewhere in the system does not remove these obligations.
