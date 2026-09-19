# Literature evidence method

## 1. Define the evidence question

Write the requested proposition or synthesis target before collecting papers. Fix the axes that determine a match, such as:

- functionality, input/output relation, and exact construction variant;
- security notion, adversary, corruption, setup/oracle, composition, abort/output delivery;
- parameters and supported regime;
- theorem, definition, algorithm, formula, implementation, or measured result;
- phase, unit, direction/aggregation, denominator, and exclusions;
- section-writing pattern versus technical content.

Choose domain-specific axes only when they distinguish candidates. For MPC, this can include who supplies and learns which values, threshold/corruption, input timing, preprocessing interface, and delivery guarantee. For zero knowledge, this can include the relation and witness representation, proof versus argument, soundness versus knowledge soundness, zero-knowledge notion, setup, interaction or Fiat–Shamir model, adaptive statements, and prover/verifier/proof-size costs. A similar name or asymptotic bound does not establish an equivalent interface.

This prevents an incidental keyword mention from becoming a false strict match.

When a request uses an ambiguous capability name such as “batched,” “shared,” “compact,” or “distributed,” write the desired input/output relation and cost target before interpreting the name. Identify which parameters are public, private, or secret-shared; whether outputs preserve instance identity or only an aggregate; and whether the required output is compact keys or expanded correlations. For a compression question, make the requested scaling explicit, for example `k*d + w` rather than `k*(d+w)`. A paper with matching terminology may provide a different interface or optimize a different term.

## 2. Inventory and version the corpus

Record the denominator: files or records considered, files successfully opened, failures, duplicates, supplements, and versions excluded. When the user says “each paper,” report coverage explicitly.

For each retained source, record title, authors, venue or archive, date, version/revision, stable identifier, local path or official URL, and whether it is the full/proceedings/appendix/artifact version. Resolve numbering against that exact version. Distinguish the displayed page label from the zero- or one-based PDF page index when they differ. For a user-designated local evidence copy without an embedded stable version, optionally record its SHA-256.

Current or priority claims require a fresh primary-source search. When local files are supplied, use them as the requested evidence version and search only as needed to disambiguate or update. Keep “newest construction,” “fastest reported implementation,” “appropriate security model,” and “maintained author implementation” as separate questions; a single chronological ranking rarely answers all four. Verify an official-code claim through the authors' paper or project links, and distinguish an author implementation from a reproduction, a later rewrite, and a component library.

Before treating a construction or parameter set as a usable candidate, check the current primary version and linked errata for author warnings, withdrawals, attacks, or corrected parameters. Record the source-stated status separately from your own security assessment; a title or published venue does not establish that the current construction remains a viable candidate.

## 3. Triage, then inspect

Use text extraction and section/keyword searches to find candidates. Then inspect the section boundaries and relevant rendered pages. Classify each candidate as:

- strict match: directly contains the requested formal object or result;
- related discussion: informs the topic but does not satisfy the strict criterion;
- attribution only: cites or summarizes another source;
- false positive: keyword with a different meaning;
- unreadable/unverified.

For a formal model subsection, extract at least the parties/roles, quantified machines, compared executions, inputs/auxiliary information, setup or hybrid resources, corruption and scheduling, indistinguishability type, composition statement, and any theorem-scope qualification. Reject an attractive template if it omits a component material to the requested model.

## 4. Tabulate claims and supporting sources

Use one row per material claim:

| Claim ID | Normalized claim | Source/version | Exact locator | Evidence type | Value/formula | Assumptions/derivation | Status/uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |

Use evidence types relevant to the question: source-stated definition or theorem, source-reported analytical result, explicitly derived from displayed formulas, inferred interpretation, or unavailable. For empirical claims, additionally distinguish author-measured, inherited/cited measurement (attribution only and not rerun by this paper), independently rerun, and estimate/extrapolation. For numerical claims, retain the source unit and denominator before any conversion. A theoretical survey needs no empirical evidence inventory.

If the source does not state a value but supports a derivation, show the formula, substitutions, and assumptions. Do not say “the paper reports” the derived value. In particular, counting outputs per application is insufficient to transfer a rate: verify the algebraic relation, field, sharing/key ownership, setup, and timed operation. A source may use distributed setup without including it in a displayed expansion timer; leave an ambiguous timing boundary unverified until the paper or code resolves it. For a narrow single-paper question, a compact table containing only the implicated claims is sufficient; do not force a full corpus-style report.

## 5. Cross-check and synthesize

- Trace a theorem or table entry through every cited lemma, appendix, caption, or parameter definition needed to interpret it.
- Compare versions when labels or values conflict; do not silently choose the convenient one.
- Recompute arithmetic and unit conversions.
- Separate common structure from paper-specific notation and from the researcher's recommended formulation.
- Preserve dissenting results, exceptions, incomparable models, and negative findings.
- Keep source claims separate from validation of those claims. For concrete-security discussions, record whether the source gives a theorem, inherited parameters, known-attack work estimates, a restricted distinguishing class, a sampling-failure bound, empirical extrapolation, or a conjecture. A field/key width or table heading such as “Bit Sec.” does not determine which of these is meant.
- Match a parameter argument to its actual distribution and regime. Evidence for a dual problem, one sampler, or independent blocks does not automatically transfer to a primal problem, a modified sampler, or reused blocks. Describe such transfer as an additional assumption or unverified step, without imposing a new assumption on the target work.
- Do not search only for precedent supporting the requested conclusion. If relevant papers provide stronger calibration or a different guarantee than expected, report that counterevidence and narrow the conclusion.

When learning a writing pattern, synthesize decisions rather than copying prose: what the section defines, in what order, which formal axes are explicit, how it connects to later theorems, and which omissions would be unsafe in the target paper.

## 6. Deliverable checks

Before delivery, verify:

- the corpus count and failed-source list;
- every important locator against the exact version;
- every citation and attribution against a primary source;
- formula/table/header/caption consistency;
- reported versus derived language;
- currentness for state-of-the-art, official-code, or priority claims;
- that any drafted text does not strengthen the target theorem or silently import a source's assumptions.

For a negative claim such as “the paper does not report a throughput,” search the full extract for the result name and close synonyms; benchmark/evaluation/experiment headings; throughput, time, latency, communication, and common unit strings; and relevant table captions. Inspect candidate and evaluation pages visually, state the searched coverage and OCR/extraction limitations, and phrase the conclusion as unavailable in the inspected version rather than universal absence when coverage is incomplete. “Not found in the inspected corpus” is neither an impossibility result nor proof that no later work provides it. An unavailable result must not become a zero value in a comparison.
