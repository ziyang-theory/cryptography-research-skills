# Specification and distributions

## Reproduction target

Pin the paper/version, theorem or algorithm, upstream revision, parameters, workload and exposed interface. Classify the result accurately: original-author artifact, pinned development code, paper reproduction, functional reconstruction with stand-ins, or engineering variant. Add orthogonal qualifications such as ideal preprocessing, trusted setup, uncalibrated parameters and partial host validation. A project's selected default is not endorsement by the original authors.

For upstream adapters, isolate patches, preserve applicable attribution/licenses, and record build settings and the executable actually run. Trace phase entrypoints to operations instead of trusting function names. Keep architecture fallbacks and omitted features visible; compilation on one architecture does not validate another.

## Actual random variables

Write down the joint distribution consumed and emitted by each relevant component: field/ring, dimensions, parties' shares, public parameters, secret randomness, dependence/reuse and auxiliary information. Check which values are fixed before adversarial choices or challenge sampling.

Uniform sampling, seeded generation, rejection sampling, certification, repeated blocks, fixed weights and relaxed weights are different distributions unless an argument relates them. Compare the complete published representation, including generation seeds, with the assumption's view. A local distance check, reconstruction identity or dimensionally valid tuple establishes only that checked property.

Shared arithmetic helpers do not imply shared cryptographic samplers. Preserve different noise distributions, domains, zero-payload slots and length/padding rules where they are part of the construction. Bind version/configuration identities where the protocol calls for it; do not relabel incompatible serialized keys or transcripts.

Trusted code that sees all keys is a test/setup fixture unless a matching distributed setup protocol is implemented and supported. Independent KDF outputs do not in general create the required joint correlations. Reusing seeds or deterministically deriving descendants does not by itself establish fresh independent correlations or post-compromise recovery.

## Transformations and claims

Keep literal interactive challenges, PRG-expanded sent seeds, and Fiat–Shamir transcript challenges separate. For transcript hashing, identify which preceding values are fixed, their canonical encoding, statement/session/role binding where required, challenge domain, and domain separation. Existing ROM use elsewhere in a protocol does not prove a new Fiat–Shamir transformation; soundness, extraction, simulation and query-dependent bounds require their own matching argument.

When a required ideal resource is replaced, document the wrapper, distribution/interface and corruption/output guarantees. Matching an honest algebraic relation or a throughput denominator alone does not establish secure composition.

Do not call key width a concrete security level. Separate theorem assumptions for the formal ensemble from implementation samplers and numerical attack screens. A conditional distinguishing calculation on selected instances is not automatically a full-protocol attack, a population estimate or constant-success attack cost. Escalate proof/parameter questions to an explicit analysis with sources, rather than burying them in implementation claims.
