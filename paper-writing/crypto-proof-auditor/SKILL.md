---
name: crypto-proof-auditor
description: Audit or complete cryptographic proofs, reductions, simulators, and security theorems. Use for proof-validity questions; read-only unless completion or source edits are requested. Not for prose-only, code-conformance, or PDF reviews.
---

# Crypto Proof Auditor

Determine whether the conclusion follows under the stated definition, model, and assumptions. An audit is read-only unless completion or edits are requested. Never conceal a gap by silently adding an assumption, weakening the theorem, or changing the construction. Different proof organization or labels alone are not defects.

## Audit workflow

1. Resolve the active theorem, definitions, construction, proof, and source revision. Separate the intended target from the supplied statement and checked argument. Identify imported results you will check and those left unverified.
2. Fix the theorem's objects, domains, parameter regime, quantifier order, and permitted dependencies. Record the adversary/corruption model, setup and oracle interfaces, compared joint outputs or success event, leakage, assumptions, bound, abort/delivery guarantee, and composition or reuse scope.
3. Trace each part of the conclusion to the lemmas, calculations, simulators, extractors, or reductions supporting it. Check hypotheses, types, parameter substitutions, model compatibility, efficiency, and accumulated error. A dependency graph is useful for a large proof, not a required deliverable for a local question.
4. For game or hybrid arguments, check complete experiments, endpoints, each adjacent justification, challenge embedding, the correctly correlated surrounding view, and the final advantage/runtime bound. For simulation, check that every action uses information available at that time. Inspect the actual experiment rather than importing a familiar template.
5. Test disputed inferences with boundary parameters, adversarial choices, conditioning, schedules, reuse, or small counterexamples as relevant. A counterexample to a step need not refute the theorem; failure to find one is not a proof. Do not call a missing derivation routine until checked.
6. Compare the established conclusion with the claimed scope. Mathematical proof support, implementation conformance, and empirical evidence are distinct conclusions; tests and builds do not establish a security theorem.

## Read only the needed detail

- [Audit method](references/audit-method.md): dependency tracing, probability, quantifiers, counterexamples, and optional diagnostic examples.
- [Reductions and bounds](references/reductions-hybrids-and-bounds.md): game hops, conditioning, sampler changes, concrete loss, and tightness.
- [Simulation and composition](references/simulation-composition-and-resources.md): malicious behavior, causality, abort, sessions, and ideal-resource replacement.
- [Extraction and oracles](references/extraction-and-oracles.md): knowledge claims, commitments, proof systems, Fiat--Shamir, ROM, and QROM.
- [Repair and validation](references/repair-and-validation.md): authorized completion or edits.

A theory audit requires no implementation or experiments. These references are self-contained; optional writing or implementation skills are useful only when that additional work is requested.

## Report findings

Lead with supported findings, ordered by consequence. For each, give the claim and source anchor, failed obligation, evidence, consequence, smallest defensible repair or missing lemma, and residual uncertainty. Scale the format to the question; a fixed worksheet is unnecessary. Identify valid challenged steps as well as invalid ones when adjudicating a disputed inference.

Distinguish **confirmed error** (invalid inference or counterexample), **proof gap** (missing obligation), **unstated assumption**, **scope overclaim**, **ambiguity**, **unverified dependency**, and **presentation issue**. State impact and confidence; keep speculative concerns as questions.

End with the strongest supported disposition: theorem refuted by a counterexample satisfying its hypotheses; supplied proof incomplete; only a stated narrower scope established; or no confirmed defect found in the audited surface. State coverage and unchecked dependencies. An outline can contain no identified defect while still failing to discharge the theorem. An informal audit does not certify correctness or constitute machine-checked verification.
