---
name: crypto-protocol-implementation
description: Implement, optimize, reproduce, or review cryptographic research protocols and their paper-to-code correspondence, including MPC, zero-knowledge, and correlated randomness. Use for circuit, transcript, state, sampler, and adapter fidelity or identifying security obligations affected by code changes; not for proof-validity audits or benchmark interpretation alone.
---

# Cryptographic Protocol Implementation

Identify the governing specification and its version before modifying code. Keep the formal construction, implementation choices, test fixtures, and claimed guarantees distinguishable.

For a correspondence review, map the specified steps to live code and report discrepancies. For requested implementation or repairs, make scoped changes and validate the affected behavior. An implementation request does not authorize rewriting the theorem to fit the code.

## Select the checks

- Read [specification and distributions](references/specification-and-distributions.md) for reproductions, protocol variants, correlations, parameter samplers, or setup changes.
- Read [state and validation](references/state-and-validation.md) for peer messages, lifecycle, optimizations, secret handling, or test design.
- Read [optimization strategy and execution](references/optimization-strategy-and-execution.md) for selecting techniques from bottlenecks and tradeoffs; follow its MPC or ZK reference only when that construction is involved.
- Read [security preservation and proof reuse](references/security-preservation.md) when optimizing or replacing a component, changing parameters or scheduling, or deciding which existing security arguments still apply.
- Read [verification scope and trust](references/verification-scope-and-trust.md) when using formal verification evidence, modifying verified code, or choosing an implementation-verification approach.
- Optional companions are `crypto-proof-auditor` when proof validity is requested and `crypto-benchmarking` for experimental evidence. Without them, trace the implicated theorem from its definition and assumptions through the reduction or simulation obligations, reporting unresolved gaps; for measurements, record the exact variant, timed operations, worker/topology settings, repetitions, statistic and raw evidence. Functional tests do not discharge proof obligations or establish performance.

## Core practice

Map the paper's definitions, algorithms and message schedule to APIs, state transitions, serialization, randomness, checks, outputs and aborts. Resolve missing interfaces before presenting a complete reproduction; explicitly mark ideal functionalities, trusted dealers, stand-ins and omitted phases.

For MPC, track party-local views and correlation ownership. For proof systems, track statement/witness separation, setup material, transcript challenges, verification and output acceptance. Apply only the checks pertinent to the selected model and implementation.

For optimization work, identify the target metric and actual or hypothesized bottleneck before choosing a technique. Explain which communication, computation, intermediate storage or repeated work is reduced, what replaces it, and whether the gain survives at the requested workload and phase scope. Respect a requested local optimization; a broader bottleneck does not authorize a protocol replacement.

Classify an optimization by the contract it affects, not the size of the code diff. Preserve protocol-visible behavior unless a variant change is authorized. Byte equivalence, algebraic output equality, distributional equivalence and realization of the same ideal functionality are distinct obligations. Domain separation or an extra transcript check can change the protocol; document it rather than assuming it is merely an implementation detail.

Keep the protocol theorem, executable specification when present, source implementation and compiled executable connected by explicit evidence. Reuse an existing security argument only to the extent that its required contract and hypotheses remain supported. Identifying an open obligation does not authorize a theorem rewrite or require introducing a formal-verification toolchain.

Return the implemented/reviewed scope, source-to-code mapping, variant and setup qualifications, focused checks and outcomes, and unresolved dependencies. For an optimization, identify the preserved or changed contract and the status of affected proof obligations. Distinguish functional correctness, memory/runtime safety, specification conformance, cryptographic security, leakage guarantees and measured performance.
