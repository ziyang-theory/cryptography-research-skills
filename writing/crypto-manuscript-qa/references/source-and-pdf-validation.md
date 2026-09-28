# Source and PDF validation

## Resolve the live document

Inspect repository status, root TeX/build files, conditionals/includes and candidate PDFs. A submission, full article, supplement and downloaded draft can differ. Identify which is authoritative for the request and match pages to that artifact; use content/version identities when ambiguity matters.

Trace stable labels through the selected build's auxiliary files instead of copying printed table/theorem/appendix numbers. Source comments, excluded branches, unused files and old reviews are not active claims. Shared source may be included inline in one version and as an appendix in another; use the project's label-based or conditional references.

For an undefined reference, first determine whether the target moved, was renamed, or is intentionally excluded. Restoring excluded content can change the manuscript's scope; a warning alone does not justify reintroducing an old appendix, construction variant, or unproved claim.

For “where is this explained?”, give the selected version, displayed PDF page (and PDF index if different), section/figure/theorem, source anchor, and whether the discussion is complete, informal, deferred or only announced. Extract text to locate material; render the relevant pages when equations or layout make extraction uncertain.

## Check manuscript guidance against its evidence

When asked to refresh project guidance, reconcile the current source map with the author's decisions instead of treating either as a complete history. Check actual user messages and later follow-ups before recording an accepted replacement, revert, or deferred issue. An assistant proposal is not an author decision; a live source observation is not necessarily an author preference. Record the scope and provenance needed to distinguish them, and keep dated checkpoints separate from current instructions.

Use live labels and the active include graph to update locations. Replace superseded current guidance while keeping retained revision history explicitly historical. A request to shorten an argument may later become a request to remove its standalone lemma; reading only the initial exchange can restore an obsolete organization. Keep manuscript-specific formulas, formatting, and exceptions local when extracting a reusable method.

Keep evidence types separate in guidance: a wording decision does not verify a literature claim, a dated novelty search has coverage limits, and a build or source review does not certify a proof. Guidance-only edits call for checking changed paths, links, and any skill metadata; they do not themselves authorize changes to TeX, bibliographies, or PDFs or require a manuscript rebuild.

## Edit and verify proportionately

Use the project's build command and verify the entrypoints affected by a shared-source change. Keep generated extraction/rendering files out of tracked sources unless the project intentionally owns them.

After a meaningful LaTeX edit, check the source diff and whitespace, build errors, undefined citations/references and substantive warnings; distinguish new problems from pre-existing ones. Verify that changed text reached the intended PDF. Render affected pages and inspect equations, floats, clipping, overflow and continuity.

If reference links, numbering or appendix structure changed, inspect actual PDF destinations. A correct printed label and successful compilation do not ensure a unique hyperlink anchor or correct target page. Reset theorem/section counters can create duplicate destinations; diagnose within the selected class/build rather than applying a remembered project-specific patch.

For submission preparation, verify the current official venue/version rules, metadata/anonymity and page-count convention. Count main matter, references and supplements under those rules; do not carry a previous venue's page limit or template settings forward. Preserve distinct full/submission entrypoints when that is the project's chosen design.

## Completion evidence

Report the files/version changed, build/render checks and remaining relevant issues. A PDF build does not establish proof correctness, source-to-code security correspondence or submission readiness. Do not substitute a broad implementation report for a requested focused proofreading list.
