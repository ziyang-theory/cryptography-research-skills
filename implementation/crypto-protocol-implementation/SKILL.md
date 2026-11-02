---
name: crypto-protocol-implementation
description: Implement, optimize, reproduce, or review cryptographic protocol code against its specification. Use for circuit, transcript, state, sampler, and adapter fidelity and security obligations affected by code changes; not a full proof-validity audit.
---

# Cryptographic Protocol Implementation

Connect the governing specification to the code and the behavior being changed. Keep formal constructions, engineering variants, test fixtures and claimed guarantees distinguishable.

## Workflow

1. Identify the specification/version, target code and exposed interface. Map the relevant algorithms and message schedule to APIs, state, randomness, serialization, checks, outputs and aborts. Mark ideal resources, trusted fixtures and omitted phases.
2. For a correspondence review, report discrepancies. For implementation work, make scoped changes. For optimization, identify the target metric, observed or hypothesized bottleneck, replaced cost and added work before choosing a technique.
3. Identify the contract affected by the change. Byte equivalence, algebraic output equality, distributional equivalence and realization of the same ideal functionality are different obligations. Small edits to challenges, checks, parameters or scheduling can change the protocol.
4. Validate changed behavior with focused checks and the project's required checks; for reviews, report available evidence and gaps. Reuse a security argument only where its contract and hypotheses remain supported, without rewriting the theorem to fit the code.

For MPC, track party-local views and correlation ownership. For proof systems, track statement/witness separation, setup, transcript challenges and acceptance. Functional correctness, memory/runtime safety, specification conformance, cryptographic security, leakage and measured performance require distinct evidence.

## Review, repair, and revalidate

Before delivery, review the changed code and validation evidence against the specification and affected contract. For substantial implementation or optimization work, use a separate reviewer when available; supply the original request, specification, code or diff, and check results. A delegated reviewer returns findings without starting another review chain. For a small change or unavailable delegation, perform a focused self-review without claiming independence.

Adjudicate concrete discrepancies, make authorized repairs, and rerun affected checks, including required project checks. For read-only reviews, correct findings and describe repairs without changing code. Use one review-and-revision pass by default; repeat for a specific unresolved failure or a new change. No defect is a valid finding. Finish when the scoped checks pass or report the failing check or missing dependency; do not weaken the specification or present functional tests as a security proof.

## References by task

- [Specification and distributions](references/specification-and-distributions.md): reproductions, variants, samplers, correlations and setup.
- [State and validation](references/state-and-validation.md): peer messages, secret lifetimes, arithmetic preconditions and tests.
- [Optimization strategy and execution](references/optimization-strategy-and-execution.md): bottlenecks and tradeoffs, with selective MPC and ZK routes.
- [Security preservation and proof reuse](references/security-preservation.md): changed components, parameters or schedules and affected proof obligations.
- [Verification scope and trust](references/verification-scope-and-trust.md): formal evidence, verified code and verification-tool selection.

Load only the implicated references. Return the implemented/reviewed scope, source-to-code mapping, variant/setup qualifications, validation results and unresolved dependencies. For optimizations, state the preserved or changed contract and whether the claimed gain is measured or still hypothetical.
