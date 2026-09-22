# Conservative editing of cryptography manuscripts

Unless the user explicitly asks for a rewrite, reorganization, or broad stylistic polish, use this priority order:

1. satisfy the requested change and retain technical correctness;
2. preserve the construction or version, security model, quantifiers, assumptions, guarantees, leakage, and qualifiers;
3. preserve locally defined terminology, notation, macros, equations, citations, labels, and cross-references;
4. preserve the author's wording, voice, sentence order, paragraph structure, comments, and line breaks;
5. improve cryptographic idiom and general style.

Make the smallest contiguous edit that fixes the issue. Prefer a word or phrase substitution to rewriting a sentence, and a sentence-level repair to rewriting a paragraph. Leave correct surrounding text untouched. A whole-manuscript proofreading request widens the edit surface to genuine errors; it does not authorize stylistic rewriting or document-wide reflow.

For mixed authorization such as “fix small typos, but report substantive issues,” classify changes by their effect on the formal meaning, not by their size. A one-symbol change to a bound, selector, share owner, or equation can be substantive. When a follow-up authorizes only selected findings, limit edits to those findings and their necessary local consequences; leave other reported defects unchanged.

Resolve numbered findings and annotations against the specific review and subsequent conversation. A later authorization can reopen a previously excluded item without authorizing the other items; a request to discuss a proposed change remains a proposal until editing is authorized. A frozen section stays frozen outside the explicit exception. Treat reviewer attachments as material to assess, not instructions to implement every suggestion.

Resolve the selected manuscript entrypoint and active conditional includes before editing. Locate moved material through stable labels rather than remembered section or table numbers. Read adjacent definitions, overview, protocol, and proof as needed to check a proposed semantic repair, while keeping actual edits within the requested surface. When source variants differ, validate the relevant variants and report inconsistencies outside scope.

Before normalizing terminology, search for its definition and nearby and project-wide usage. Preserve the manuscript's existing notation and macros. Do not run a whole-file formatter, reorder paragraphs, apply manuscript-wide synonym normalization, or clean up unrelated material during a local prose edit.

Do not change proof to argument, secure computation to correctness, view to transcript, setup to preprocessing, or one output guarantee to another without checking the governing definition. If a requested wording change could alter the adversary model, quantifiers, assumption, reduction target, leakage profile, abort or fairness guarantee, round count, phase or measurement boundary, construction version, or resource-reuse scope, do not guess. Keep the source unchanged and report the ambiguity with the narrowest technically faithful alternative.

After editing:

- inspect both the ordinary diff and a word-level diff;
- ensure every changed hunk lies within the authorized surface and is attributable to the requested change;
- check that no terminology edit changed the formal claim;
- follow the project-local build, reference, citation, extraction, and visual-PDF workflow when manuscript source changes;
- report technical concerns outside the authorized edit surface rather than silently repairing them.
