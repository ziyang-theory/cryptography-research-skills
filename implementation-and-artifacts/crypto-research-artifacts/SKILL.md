---
name: crypto-research-artifacts
description: Prepare, document, anonymize, validate, or package reproducible cryptography research artifacts for paper supplements, evaluation, or archival release. Use for claim-to-command maps and detached package validation; not for protocol proofs, benchmark execution alone, or manuscript editing.
---

# Cryptography Research Artifacts

Build a reviewer workflow around the accompanying paper and the author's requested release scope. Separate reproducibility, correctness, performance evidence and security claims.

Read [release workflow](references/release-workflow.md) for policy, packaging and validation. Read [claims and reviewer commands](references/claims-and-commands.md) when designing the README, experiment guide or claim records.

## Essential decisions

- Resolve the exact paper version/entrypoint and release stage: initial supplement, artifact evaluation, or archival release. Verify applicable venue rules from current official sources when making compliance claims; historical guides are examples.
- Honor the requested action: planning, local cleanup, package creation, validation or publishing. “Do not create the artifact yet” permits planning/cleanup in scope, not a package. Local preparation does not authorize external submission.
- Respect the project's export policy. Retaining historical observations privately and exporting them are separate decisions. Do not impose either mandatory inclusion or blanket exclusion of old measurements on future projects.
- Include what the selected claims require: source, pinned dependencies, required fixtures, configurations, runnable experiments, analysis and interpretation. Preserve necessary attribution and licenses; do not invent a first-party license choice.
- Give reviewers a small deterministic entrypoint and staged experiments with realistic requirements. Keep developer history and irrelevant variants out of the initial workflow without hiding limitations material to the claims.
- Validate a fresh extraction away from the developer checkout and bind results to the final package checksum. Report PASS, FAIL and NOT RUN honestly, with scope.

Optional companions are `crypto-benchmarking` for measurement semantics, `crypto-protocol-implementation` for code changes, and `crypto-manuscript-qa` for requested manuscript correspondence or edits. Without them, record included operations, units and aggregation for measurements; map code changes to the governing specification and focused tests; and check each selected paper claim in the exact source/PDF version against its packaged configuration and evidence. The local claim map and detached-validation procedure remain the basis for the release.
