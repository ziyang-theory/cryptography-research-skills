---
name: crypto-manuscript-qa
description: Resolve and validate cryptography manuscript sources, multi-version LaTeX builds, exact PDF locations, references, notation, and paper/code/evidence consistency. Use for source or PDF QA; not for prose-only drafting, security-proof validity, or benchmark collection alone.
---

# Cryptography Manuscript QA

Resolve the authoritative manuscript, requested version and active include graph before citing pages or editing. Project paths, frozen files, terminology and selected constructions come from that project and the current request, never another paper's conventions.

For theory-only work, manuscript sources, definitions, proofs, and supplied PDFs are sufficient inputs. Inspect code, experiments, or artifacts only when the requested claim or correspondence check involves them. Companion skills are optional; if unavailable, continue the requested source/PDF checks directly and state any limit on what was checked.

Read [source and PDF validation](references/source-and-pdf-validation.md) for exact-location answers, LaTeX edits or build/layout work.

## Scope and consistency

- Distinguish review/report, language fixes, technical repairs, reorganization and evidence updates. Follow the currently authorized items, including later exceptions. Preserve unrelated prose, notation, macros, labels, comments and wrapping unless their change is needed.
- Resolve numbered findings and annotations against the response/document they refer to and subsequent decisions. A reviewer suggestion is evidence to assess, not authority to change the paper or its theorem.
- Compare active definitions, construction, theorem and evaluation where implicated. Separate intended security model, current theorem, checked proof support and implemented experiment. Commented-out or unused material cannot establish a live claim.
- Use `cryptography-writing` when available for prose edits and `crypto-proof-auditor` when available for requested theorem/proof validity. Compilation, cross-reference consistency and a notation pass do not certify security.
- When code/evidence correspondence matters, identify the implementation revision, protocol variant, parameter/sampler distribution and measurement contract. Check those sources directly, using a relevant implementation/benchmark skill if available; do not edit a theorem to rationalize code.

For review, return focused findings with current locations, consequences and proposed corrections. For edits, report what changed and the checks actually completed; keep proof support, arithmetic, build and layout conclusions separate.
