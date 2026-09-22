---
name: crypto-manuscript-qa
description: Check cryptography manuscript sources, LaTeX builds, PDF locations, references, layout, and requested paper/code consistency. Use for source or rendered-document QA; not for prose-only drafting, proof validity, or benchmark collection.
---

# Cryptography Manuscript QA

Resolve the authoritative manuscript, requested version, and active include graph before citing pages or editing. Project paths, frozen files, and construction choices come from the current project, never another paper's conventions.

## Check the requested surface

- Distinguish review, language edits, technical repair, reorganization, and evidence updates. Follow the authorized scope and later decisions; preserve unrelated prose, notation, macros, labels, comments, and wrapping.
- Resolve findings and annotations against their actual document/version. Reviewer suggestions are evidence to assess, not authority to change the theorem.
- Compare implicated active definitions, construction, theorem, and evaluation. Keep intended claims, checked proof support, and implemented experiments distinct; unused or commented material establishes no live claim.
- For code/evidence correspondence, identify the revision, variant, parameter/sampler distribution, and measurement contract. Inspect the sources directly; do not alter a theorem to rationalize code. Theory-only QA needs no implementation or experiments.

Read [source and PDF validation](references/source-and-pdf-validation.md) for version/page resolution, affected LaTeX builds, rendered-page inspection, actual hyperlink destinations, or submission checks. Apply only the checks relevant to the change.

For review, give focused findings with current locations, consequences, and proposed corrections. For edits, report changes and completed checks, separating arithmetic, build, and layout results from proof support. Compilation does not certify security. Use writing or proof-audit guidance when that distinct work is requested; companion skills are optional.
