# State, secrets and validation

## State and parsing

Derive the state machine from the protocol: allowed messages, order, session binding, one-use objects, accepted outputs and terminal rejection. Validate adversary-controlled lengths, canonical encodings, dimensions, padding, counters and bindings before unsafe allocation or unintended mutation.

If the protocol requires a one-use terminal attempt, consume or poison pending state even on rejection; do not leave a failed attempt reusable with modified input. Conversely, do not impose terminal consumption on an interface that explicitly permits retries. Withhold provisional output until the checks required for that recipient's output guarantee have succeeded.

Document secret ownership through copies, moves, worker failures and early returns. Redact secrets from debug/log/serialization paths. If erasure is claimed or part of the corruption/measurement model, check all relevant owned allocations; wiping a destination does not prove the source was erased. Scope erasure claims to what is actually controlled, and do not imply constant-time or side-channel security from functional tests.

## Meaningful validation

Choose tests from the changed obligation rather than a fixed universal suite:

- Known-answer or independent-reference checks for honest behavior and the exact workload/variant.
- Reconstruction/authentication equations for every generated coordinate and role implicated by the change; checking only a downstream output may miss unused faulty resources.
- Malformed/tampered peer inputs, wrong bindings, rejected reuse and premature-output attempts for affected interfaces. Assert the intended rejection, not an arbitrary error.
- Relevant zero/empty/small instances, constants, repeated outputs, fan-out, padding, non-power-of-two tails, field widths or truncated values.
- Scalar/reference versus streaming/parallel/SIMD equivalence, including stripe boundaries, counters, scratch reuse and error paths. A small full-reference oracle is useful even when the production layout cannot materialize the full object.
- For prover/verifier code, valid and invalid statements/proofs and the relation's public-input/witness encoding; functional rejection tests alone do not establish soundness or zero knowledge.

Check selectors against live source and confirm tests executed. A changed wrapper must exercise the exact built binary even with custom target directories or profiles. A smoke result covers its selected configuration; broad test counts do not imply ignored performance or alternate-platform tests ran.

Run repository-required checks proportional to the change, preserving unrelated dirty work. Record environment limitations as such, separately from protocol/test failure. Avoid broad refactors or parameter changes merely to make an unrelated check pass.
