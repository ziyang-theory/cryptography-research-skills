# Verification scope and trust

Use this reference when a project has formal evidence, claims a verified implementation, or requests a verification approach. Ordinary implementation work need not introduce a prover or a new specification hierarchy.

## Connect the checked objects

Identify the exact source, specification, proof and executable revisions/configurations. For each claimed connection, name what was proved, tested, assumed or left unverified. A protocol model, a translated source program, an extracted implementation and a compiler-produced executable are different objects; separate proofs about disconnected objects do not establish an end-to-end claim.

Record the theorem's statement, preconditions, adversary interface and property: functional correctness, memory/runtime safety, symbolic or computational protocol security, or a specified leakage property. For bounded symbolic checks, retain the modeled inputs, path/loop bounds and unsupported behavior. Success within that model is not automatically an unbounded protocol theorem.

Review axioms, admitted statements, abstract library models and excluded execution paths that affect the claim. In particular, a malicious-security model must not silently require adversarial messages to arise from an honest algorithm on some input. Distinguish a proved honest-party invariant from an unjustified restriction on adversarial behavior. Do not repair failed verification by weakening the statement or adding an unreported assumption.

## Record what remains trusted

For the actual pipeline, identify applicable trusted components: proof kernel and solver interfaces, axioms, source translations and standard-library models, unverified compiler stages, unsafe code, FFI/assembly, randomness sources and platform assumptions. Do not label every component trusted if a checked result covers it; state the scope of that result.

For Rust, check the selected translator/backend's supported language features against the actual code, including unsafe operations, intrinsics, concurrency and external calls. Pin the artifact and toolchain needed to reproduce the result. Verify current capabilities in official documentation when choosing tools; a historical paper configuration is not evidence of current backend support or interoperability.

A proof about translated Rust does not automatically cover the binary emitted by `rustc`/LLVM. Compiler correctness for functional behavior alone does not establish preservation of a two-execution leakage property. Identify an applicable preservation theorem or analysis at the relevant compiled level. A constant-time result remains relative to its observation/machine model; version pinning establishes neither that property nor coverage of all physical channels.

## Validate changes at the claimed level

Recheck affected formal obligations and their callers, and run the project's required proof build when formal evidence is part of the deliverable. Inspect changes to statements, assumptions and admissions as well as build success. An unchanged theorem may still have acquired stronger hypotheses. A broken tactic can reflect proof-script fragility; a successful build can certify an inadequate statement.

Complement formal checks with focused integration, differential and adversarial-input tests from [state and validation](state-and-validation.md). Record unrun checks and unsupported targets separately. For a claimed security-preserving optimization, report which contract was re-established and what still relies on assumptions or unverified code.

If asked to select a verification approach, start from the missing obligation and the project's existing toolchain. A small pilot involving a deterministic kernel and a security-sensitive state transition can test source coverage, specification adequacy and proof-maintenance cost before committing to a larger effort. Do not assume that combining a Rust translator, equivalence checker and cryptographic prover yields a supported end-to-end pipeline.
