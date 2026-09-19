---
name: crypto-proof-auditor
description: Audit cryptographic theorem statements, proofs, proof sketches, reductions, hybrid arguments, simulators, and extractors for concrete gaps and unsupported scope. Use when asked to verify, audit, stress-test, diagnose, or complete a cryptographic proof or claimed security theorem. Read-only and defect-first by default. Do not use for prose-only editing, code or artifact verification, PDF/build work, raw benchmark accounting, or generic non-cryptographic proofs.
---

# Crypto Proof Auditor

Audit whether the stated conclusion follows under the stated definitions, model, and assumptions. Search for concrete defects and missing obligations; do not rewrite the proof merely because another presentation would be cleaner.

For prose and reports, use precise cryptographic terms and concrete descriptions. Preserve established technical meanings and quoted or formally defined terminology. The companion `cryptography-writing` skill provides further terminology guidance when available.

## Authorization and evidence

A request to audit, verify, review, explain, or find gaps is read-only. Edit a manuscript or attempt a proof completion only when the user explicitly requests source changes or completion. Never hide a gap by silently adding a hypothesis, weakening a theorem, changing a construction, or replacing a proof with intuition.

An informal audit is not a machine-checked proof. Code, tests, benchmarks, and a successful LaTeX build can corroborate specified behavior or find counterexamples; they do not establish a cryptographic security theorem.

An audit of a theoretical result needs its definitions, construction, proof, and relevant mathematical dependencies, not an implementation or experiments. Companion skills are optional; if unavailable, continue using this workflow and its references rather than blocking the audit.

## Use the surrounding skill stack

- Use `cryptography-writing` when available for terminology and authorized prose edits. The audit workflow below is self-contained; no particular repository or protocol is required.
- Follow applicable project-local guidance to resolve the authoritative source, notation, cited pages, construction semantics, and project invariants.
- Use `crypto-protocol-implementation` when available, or inspect the code directly, when the request separately asks whether an implementation matches the proof. Keep proof validity and artifact conformance as distinct conclusions.

## Route the audit

- Read [references/audit-method.md](references/audit-method.md) for a full proof audit, dependency tracing, mathematical validity, counterexample search, or a disputed inference.
- Read [references/reductions-hybrids-and-bounds.md](references/reductions-hybrids-and-bounds.md) for reductions, games, hybrid transitions, conditioning, bad events, concrete or asymptotic reduction loss, and tightness.
- Read [references/simulation-composition-and-resources.md](references/simulation-composition-and-resources.md) for real/ideal simulation, malicious behavior, abort or leakage, composition, sessions, reuse, protocol schedules, and ideal-to-concrete resources.
- Read [references/extraction-and-oracles.md](references/extraction-and-oracles.md) for proofs or arguments of knowledge, extractors, commitments, PCPs or IOPs, random oracles, Fiat--Shamir, ROM or QROM, and oracle programming.
- Read [references/repair-and-validation.md](references/repair-and-validation.md) only when proof completion or source edits are authorized.
- For a narrow question, read only the implicated references. For an end-to-end security-proof audit, read all four audit references.

## Presentation and authorized repairs

For an authorized new simulation-based security proof, substantial rewrite, or proof completion, describe the simulator first, then present separate consecutive `Hyb_0:`, `Hyb_1:`, ... definitions, justifying each adjacent transition before introducing the next hybrid. In LaTeX use `$\mathsf{Hyb}_0$:`. This organization also applies to perfect-security proofs: exact distributional equalities and conditional-distribution arguments can justify transitions. Do not omit hybrids merely because a direct equality-of-distributions argument is available.

Depart from this organization only when it conflicts with the governing definition or would require vacuous or ill-defined intermediate experiments, and explain the specific reason. Never invent a simulator, assumption, or proof step to satisfy the format. For claims whose governing definition does not call for simulation, follow the appropriate proof form. Preserve existing organization during local repairs unless reorganization is authorized.

During a read-only audit, retain the source's labels in findings and distinguish presentation requirements from validity: different labels or organization alone are not a technical defect, whereas an undefined intermediate experiment or an unjustified transition may be a proof gap or error.

## Core workflow

1. Resolve the exact theorem, governing definitions, authoritative source revision, and requested audit surface. Separate the intended target, active theorem, supplied proof, and implementation interpretation; ignore commented or superseded statements as current claims. State which imported results will or will not be independently checked.
2. Freeze the **theorem contract**: objects and syntax; domains and parameters; quantifier order and permitted dependencies; adversary and corruption model; setup, network, oracle, or hybrid resources; target functionality or relation; prescribed outputs and leakage; assumptions; comparison or success bound; abort and delivery guarantee; composition, concurrency, session, and reuse scope.
3. Build a claim-to-obligation graph from every conjunct of the conclusion to definitions, assumptions, local lemmas, calculations, reductions, simulators, extractors, composition theorems, and cited external results.
4. Validate every dependency edge: hypotheses, domains, dimensions, interfaces, parameter substitution, quantifier order, model, runtime, query complexity, error bounds, and reduction loss. For a hybrid chain, also check exact endpoints or explicit bounds relating the endpoint experiments to the claimed distributions, well-defined experiments, controlled adjacent changes, challenge embedding, generation of the correctly correlated surrounding view, transition type, polynomial chain length, and the resulting bound on distinguishing advantage.
5. Stress-test disputed edges using extreme or degenerate parameter choices, malformed messages, adversarial schedules, adaptive choices, conditioning, oracle-query collisions, session reuse, and small counterexamples. Failure to find a counterexample is not a proof.
6. Reconcile the proof conclusion with the theorem, abstract-level claim, and any implementation or efficiency interpretation. Do not promote a proof sketch, hybrid-model theorem, one-shot theorem, or restricted adversary result beyond its established scope.
7. Report findings first, ordered by downstream impact. Separate technical status, impact, and confidence.

## Finding taxonomy

Use the narrowest supported status:

- **confirmed error:** a contradiction, invalid inference, violated premise, or concrete counterexample;
- **proof gap:** a necessary obligation is absent, although the claim may still be true;
- **unstated assumption:** the argument works only after adding a material hypothesis;
- **scope overclaim:** the proof establishes a weaker model, guarantee, parameter regime, or composition scope than stated;
- **ambiguity:** materially different formal readings change validity;
- **unverified dependency:** an imported result, version, or parameter mapping was not checked;
- **presentation issue:** no technical defect is identified, but the exposition obscures the actual argument.

Do not call an omitted step routine unless the missing derivation has been checked. Do not call a theorem false merely because its proof is incomplete; distinguish an invalid intermediate step from a counterexample to the theorem itself.

## Finding record

For each actionable finding, give:

```text
[F-01] Impact | confidence | status
Claim and source anchors:
Required obligation or dependency edge:
What the proof establishes:
Why it is insufficient:
Derivation, counterexample, or adversarial trace:
Consequence for the stated theorem:
Smallest defensible repair or missing lemma:
Residual uncertainty:
```

Use **main-claim blocking**, **major**, **local**, or **presentation** for impact. Use **high** or **medium** confidence for findings; place lower-confidence suspicions in residual questions instead of presenting them as defects.

Use the full record for substantive findings. For a narrow local audit, collapse redundant fields but retain the claim and source anchor, failed obligation, evidence, consequence, and repair. When the user asks to distinguish valid from invalid steps or disputes a particular inference, explicitly identify material challenged steps that are valid as well as those that fail.

End with one evidence-calibrated overall disposition: **the theorem is refuted by a counterexample** only when a candidate satisfies its hypotheses and violates its conclusion; **the supplied proof does not establish the theorem as stated** when a blocking error or gap remains; **the argument supports only a stated narrower scope** when the checked dependencies discharge that weaker claim; or **no confirmed defect was found in the audited surface**. Keep theorem falsity, proof incompleteness, and unchecked dependencies separate.

If no defect is found, say: “No confirmed defect was found in the audited surface.” Then list the inspected coverage, unverified dependencies, and residual risks. Do not say that the proof is correct without a formal verification basis.

If the supplied text is only an outline and omits the dependencies that would discharge the theorem, say: “No defect was identified in the outline, but the supplied material does not by itself discharge the theorem.”
