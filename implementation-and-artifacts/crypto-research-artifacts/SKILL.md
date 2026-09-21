---
name: crypto-research-artifacts
description: Prepare, document, anonymize, validate, or package cryptography research artifacts. Use for reviewer workflows, claim-to-command maps, and validation from a fresh extraction; not protocol proofs or benchmark execution alone.
---

# Cryptography Research Artifacts

Build the smallest complete reviewer workflow for the selected paper claims and release scope. Reproducibility, correctness, performance evidence and security support are distinct outcomes.

## Workflow

1. Resolve the exact paper version/entrypoint, selected claims and release stage. Verify current official venue rules when making compliance claims; historical guides are examples.
2. Map each selected claim to its configuration, evidence and reproduction command. Include required source, pinned dependencies, fixtures, analysis and interpretation. Keep ideal resources, unsupported platforms and unresolved instantiation claims visible.
3. Prepare the requested deliverable using the project's release layout and export policy. Planning, local cleanup, packaging, validation and publishing are different actions; follow the user's authorized scope. Retain attribution and licenses without inventing a license choice.
4. For a built package, validate a fresh extraction away from the developer checkout and bind the report to the final checksum. A planning request receives a validation plan; documentation edits need checks of the affected instructions and paths. Revalidate affected commands when package contents change.

Start reviewers with a deterministic correctness example, then staged experiments with realistic requirements. Developer history and optional variants need not lead the workflow, but limitations that qualify selected claims must remain discoverable. Include historical observations only when the export policy and reproduction route call for them; required input fixtures are a separate category.

## References by task

- [Release workflow](references/release-workflow.md): policy, anonymity, package construction and detached validation.
- [Claims and reviewer commands](references/claims-and-commands.md): claim records, README structure, experiment progression and formal-evidence qualifications.

Load the relevant sections. Report PASS, FAIL and NOT RUN by validation scope, the resulting package or plan, and remaining limitations. A build or smoke run does not establish publication performance or instantiate a security theorem; packaging cannot repair missing evidence.
