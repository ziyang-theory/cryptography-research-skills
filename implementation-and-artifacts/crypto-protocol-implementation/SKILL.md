---
name: crypto-protocol-implementation
description: Implement, optimize, reproduce, or review cryptographic research protocols and their paper-to-code correspondence, including MPC, zero-knowledge, and correlated randomness. Use for transcript, state, sampler, and adapter fidelity; not for proof-validity audits or benchmark interpretation alone.
---

# Cryptographic Protocol Implementation

Identify the governing specification and its version before modifying code. Keep the formal construction, implementation choices, test fixtures, and claimed guarantees distinguishable.

For a correspondence review, map the specified steps to live code and report discrepancies. For requested implementation or repairs, make scoped changes and validate the affected behavior. An implementation request does not authorize rewriting the theorem to fit the code.

## Select the checks

- Read [specification and distributions](references/specification-and-distributions.md) for reproductions, protocol variants, correlations, parameter samplers, or setup changes.
- Read [state and validation](references/state-and-validation.md) for peer messages, lifecycle, optimizations, secret handling, or test design.
- Optional companions are `crypto-proof-auditor` when proof validity is requested and `crypto-benchmarking` for experimental evidence. Without them, trace the implicated theorem from its definition and assumptions through the reduction or simulation obligations, reporting unresolved gaps; for measurements, record the exact variant, timed operations, worker/topology settings, repetitions, statistic and raw evidence. Functional tests do not discharge proof obligations or establish performance.

## Core practice

Map the paper's definitions, algorithms and message schedule to APIs, state transitions, serialization, randomness, checks, outputs and aborts. Resolve missing interfaces before presenting a complete reproduction; explicitly mark ideal functionalities, trusted dealers, stand-ins and omitted phases.

For MPC, track party-local views and correlation ownership. For proof systems, track statement/witness separation, setup material, transcript challenges, verification and output acceptance. Apply only the checks pertinent to the selected model and implementation.

Preserve protocol-visible behavior during an optimization unless a variant change is authorized. Byte equivalence, algebraic output equality, distributional equivalence and security equivalence are distinct obligations. Domain separation or an extra transcript check can change the protocol; document it rather than assuming it is merely an implementation detail.

Return the implemented/reviewed scope, source-to-code mapping, variant and setup qualifications, focused checks and outcomes, and unresolved dependencies. Distinguish code correctness, specification conformance, security support and measured performance.
