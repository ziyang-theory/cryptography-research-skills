# Proof repair and validation

Read this reference only when the user explicitly authorizes proof completion or manuscript edits.

## Classify the repair before editing

Determine which of these applies:

- an omitted derivation follows from the existing premises;
- a local side condition or boundary case is missing;
- the proof needs a new lemma, estimate, simulator, extractor, or reduction;
- the theorem must be weakened or the model narrowed;
- a material assumption must be added;
- the theorem is false as stated.

Do not present a new assumption, theorem weakening, construction change, or unproved lemma as a routine repair. If authorial judgment is required, leave the source unchanged and present the narrow choices and their consequences.

Resolve the current authorized findings against the user's subsequent decisions before editing. An approved local repair does not authorize repairing every dependent section, and a technical repair should not be smuggled into a typo pass. Read neighboring overview, definition, protocol, and proof text to test consistency; report out-of-scope changes needed rather than making them automatically.

## Make the smallest defensible change

Use `cryptography-writing` and its conservative-editing reference when available. In all cases, preserve the author's notation, terminology, macros, equations, citations, labels, comments, qualifiers, and line wrapping except where the verified repair requires a change.

When a missing derivation is genuinely obtainable, supply all steps needed to discharge the obligation and propagate its exact error or reduction loss. When the core idea remains missing, state a precise lemma or proof obligation instead of writing prose that implies completion.

If the theorem's supported scope changes and the user authorizes the broader repair, update dependent theorem statements and affected abstract, introduction, comparison, and conclusion claims consistently. Do not perform unrelated polishing.

## Validate the repair

After editing:

- rerun the audit on the repaired dependency edge and every downstream claim;
- inspect ordinary and word-level diffs;
- check dimensions, parameter inequalities, quantifier order, bounds, and model terminology again;
- use the project-local LaTeX, citation, reference, extraction, and visual-PDF workflow;
- run `git diff --check` and the repository's relevant checks;
- state which obligations are now discharged and which remain open.

A clean build confirms document consistency, not proof validity. If the repair remains conditional on an unverified imported result or new conjecture, say so in the final status.
