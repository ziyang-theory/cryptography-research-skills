# Secure-computation terminology

Use this reference for MPC, 2PC, simulation-based definitions, ideal functionalities, secret sharing, preprocessing, leakage, reuse, and output guarantees.

## Real and ideal executions

For a simulation-based claim, preserve the definition's exact quantifiers and compared random variables. A conventional stand-alone form is: for every admissible real-world adversary `A`, there exists an admissible ideal-world simulator or adversary `S` such that the specified real and ideal ensembles satisfy the required relation for the allowed inputs, auxiliary inputs, and security parameters. Composition-aware definitions may additionally quantify over environments or distinguishers, or combine these roles; preserve their exact order rather than reusing the stand-alone prefix as a universal template.

The real protocol **emulates** the ideal model or process, or **realizes** the ideal functionality; the simulator accounts for what a real adversary could achieve using only the interface and leakage of the ideal process. Do not reverse this direction.

Name what is compared:

- A party's **view** generally contains its input, random tape, received messages, and any locally retained state; it is not merely the transcript.
- A **transcript** records messages and public interaction, subject to the manuscript's definition.
- Semi-honest definitions often compare simulated views jointly with prescribed outputs.
- Malicious definitions often compare the honest parties' outputs jointly with the adversary's output, rather than asserting that a malformed adversarial view has a canonical distribution.
- For a randomized functionality, preserve the joint output distribution and its correlations; matching each marginal separately is insufficient.

Saying that a protocol **computes** a functionality normally asserts correctness for the relevant honest execution. Saying that it **securely computes** or **realizes** the functionality additionally invokes a security definition. Keep the two claims separate.

State the functionality's prescribed outputs and separately identify declared leakage such as input lengths, the function or circuit description, public parameters, access patterns, abort or failure patterns, and auxiliary leakage. “Learns only the output” is false if the definition exposes more. Conversely, output allowed by the functionality is not automatically classified as protocol leakage.

A functionality may be one-shot, reactive, or stateful. For a reactive functionality, state the command interface, state evolution, scheduling, and corruption or abort behavior across activations. Do not infer reactive or reusable security from a theorem for one isolated invocation.

## Adversary and corruption axes

Do not compress independent axes into one label:

- **Behavior:** passive and semi-honest are often corresponding terms for parties that follow the prescribed strategy while retaining their complete view; active and malicious are often corresponding terms for parties that may deviate. Preserve the source's exact corruption interface. Covert security is a separate notion.
- **Corruption timing:** a static adversary fixes the corrupted set at the time specified by the model; an adaptive adversary may choose corruptions during the execution, with the state exposure and erasure rules fixed by the definition.
- **Corruption extent:** state the corrupted set, threshold `t`, or adversary structure and whether an honest- or dishonest-majority regime is assumed. When secret sharing is involved, separately state the relationship to its access structure. Give the numerical relation between `t` and the number of parties when it matters; majority labels vary across sources.
- **Efficiency and assumptions:** state whether the guarantee is perfect, statistical, or computational, and whether adversaries are bounded concretely, PPT, or QPT.

The word **adaptive** is incomplete without its object: adaptive corruption, adaptive input selection, adaptive queries, adaptive statement selection, and adaptive programming are different notions. Passive/active behavior is independent of static/adaptive timing.

**Semi-malicious security** is not standardized. Some definitions constrain corrupted parties to prescribed algorithms while permitting adversarial choices of inputs or random tapes; others add correlation-consistency conditions. Reproduce the governing definition instead of treating the term as a universal midpoint between semi-honest and malicious security.

“Fully malicious adversary” normally describes arbitrary deviation power. It does not by itself imply full security, fairness, or guaranteed output delivery. Rushing and erasures are additional model choices.

When the definition or simulator identifies one, use **effective input**, **substituted input**, or the definition's term for the value submitted to the ideal functionality. Do not assume that every reactive, stateful, or malformed execution has a single canonical effective input, and do not call such a value the party's unknowable “true input.”

## Abort and output guarantees

Read the ideal functionality or execution schedule before naming the guarantee:

- **Security with abort** permits an adversary to prevent some honest outputs in the manner allowed by the ideal process.
- **Selective abort** is definition- and context-dependent. Reserve the term for a governing definition or cited usage that explicitly makes the abort or failure pattern selective with respect to protected, output-dependent, or target-specific information. A post-output abort permitted by an ordinary security-with-abort ideal execution is not automatically called selective abort.
- **Fairness** and **guaranteed output delivery** are distinct properties whose exact definitions and feasibility depend on the task and model.
- **Simultaneous output** is a scheduling property and does not alone imply fairness or guaranteed output delivery.
- **Termination**, **proper termination**, **robustness**, and **full security** are definition-dependent; do not use them as portable synonyms for output delivery.

An ideal functionality is not automatically maximally private or fair. Its explicit leakage, abort interface, delivery order, and scheduling behavior determine the guarantee.

Privacy with knowledge of outputs, output substitution, input-dependent or correlated abort, selective failure, and wire- or predicate-triggered abort are source-defined interfaces or weakenings. State what incorrect output, predicate, protected input, or delivery pattern the adversary may control; whether abort occurs before or after it learns its output; and whether one, some, or all honest parties are affected. Do not order or translate these notions without the governing ideal functionalities or a cited reduction.

## Parties, clients, and servers

In a client/server model, identify input clients, output clients, and computation servers separately; roles may overlap. State the number and corruption threshold for each role, whether servers have inputs or outputs, whether clients participate beyond input or output delivery, and which links are client-to-server, server-to-client, server-to-server, or broadcast. Do not silently treat the number of servers as the total number of protocol actors.

## Composition and hybrid resources

Keep these notions separate:

- a **sequence of hybrids** is a proof technique relating distributions or games;
- an **`F`-hybrid model** grants ideal access to a functionality `F` as a resource;
- **stand-alone**, **sequential-composition**, **concurrent**, and **universally composable** security are different theorem scopes.

Use UC terminology only when the model and theorem are actually UC. A stand-alone simulator does not establish concurrent or UC security merely because the proof uses an ideal functionality.

Invoke a modular sequential-composition theorem only when its scheduling, session, state, setup-reuse, and running-time hypotheses hold. Shared setup or state across invocations, overlapping or concurrent calls, and expected-polynomial-time simulation require a theorem that explicitly covers them.

An ideal functionality can specify the target task or serve as a resource for a higher-level protocol. A theorem in a hybrid model is not automatically a theorem about a concrete implementation of that resource; state the composition or instantiation theorem needed to cross the boundary.

When combining a resource generator with a consuming protocol, define the setup wrapper before stating the final result: who samples which public and private state, what corrupted parties may choose or receive, what is freshly generated, and which calls are replaced. Match the generator's security experiment to the consumer's simulator, including exposed seeds or keys and accept/reject behavior. Correct output distributions alone may not cover the consumer's full ideal interface. State the final guarantee under the composition argument actually supplied and retain the combined advantage and reduction budgets; do not silently inherit a stronger intended target.

State whether an ideal resource is invoked once, through a bounded or unbounded number of copies, or reactively; whether invocations share state or setup; and how session and subsession identifiers are scoped. One-time access does not justify a reusable or multi-session claim.

When a theorem discusses **black-boxness**, name the relevant object and interface: a construction may access an ideal functionality or a primitive's algorithms or next-message functions; a reduction may receive oracle access to an adversary or primitive; and a non-black-box construction or reduction may inspect or embed implementation code. These interfaces are not interchangeable; primitive algorithms may expose message syntax, handles, randomness, or checks absent from the ideal functionality.

## Secret sharing

Use the local convention, while keeping the following roles explicit:

- a dealer or sharing algorithm distributes **shares** of a secret to parties;
- a **qualified** or **reconstructing** set can reconstruct the secret;
- a **privacy** or **forbidden** set satisfies the source's stated privacy condition, which in a perfect scheme may require its joint share distribution to be independent of the secret;
- a merely **non-reconstructing** set need not be private: in a ramp or non-perfect scheme it may learn partial information;
- an **access structure** records reconstructing sets. A privacy structure, forbidden-set family, secret-sharing adversary structure, or MPC adversary structure may record different families under source-specific conventions.

Do not infer that privacy sets are exactly the complement of the access structure, or translate between access and adversary structures, unless the source states the required perfectness, duality, or correspondence. Threshold notation also varies: state whether `t` denotes the maximum corrupted or private-set size, a reconstruction threshold, or another boundary.

Do not call individual shares “secrets.” In secret-sharing literature, an **ideal secret-sharing scheme** may refer to share-size efficiency; it is not thereby an ideal functionality.

When multiplication or active robustness matters, distinguish linearity, multiplicativity, strong multiplication, verifiable sharing, and error-correcting or robust reconstruction. None follows merely from privacy and reconstruction; preserve the source's threshold and adversary-structure hypotheses.

## Setup, preprocessing, and phases

Setup, preprocessing, offline computation, and online computation are not interchangeable:

- identify what correlated material, keys, shares, or public parameters are generated;
- state which inputs, circuit, relation, party identities, or session identifiers the material may depend on;
- state who generates it, what trust or ideal resource is assumed, and whether it may be reused;
- separate the security and cost of generating the resource from the security and cost of consuming it;
- label online-only communication or timing as such rather than presenting it as an end-to-end concrete cost.

A common reference string may follow a specified distribution; a common random string is the uniform special case in formalisms that distinguish them. Do not conflate either with a PKI, correlated randomness, a random oracle, or preprocessing.

State the reuse scope of each receiver message, public key, reference string, oracle, correlation seed, and preprocessed correlation. One-shot security does not imply bounded- or polynomially-many-session reuse. Say what remains fixed, what is freshly sampled, whether state evolves, how sessions are chosen, and which outputs or abort bits feed back to the adversary or environment.

When reporting rounds or communication, distinguish messages, bits or field elements, logical rounds, simultaneous-message layers, ideal calls, and concrete transport. Use [constructions-and-costs.md](constructions-and-costs.md) for detailed accounting.
