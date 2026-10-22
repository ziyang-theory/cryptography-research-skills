# Drafting patterns

These are adaptable patterns based on the supplied sources described in [source evidence](source-evidence.md), not official venue language. The checklist below follows the AITCS report's proposed categories; the narrative clauses are original drafting aids. Brackets denote facts to supply, not claims to assume. Use only clauses that match the authors' account, including any claim about human review. Combine patterns for mixed use. Do not add a negative claim about other AI use unless it is established.

## AI Methodology: checklist and Details

Use for a new full methodology section or when the user requests the AITCS format. The report proposes this section for every publicly posted research paper and suggests placement after the introduction or at the end of the main text, before appendices. These are recommendations; honor the user's requested scope, existing manuscript format, and any verified venue policy.

The six categories may overlap. Assess their application to the paper's main results. For categories 1–4, Yes means meaningful influence of a kind for which the authors would consider a comparable human contribution for coauthorship. For categories 5–6, Yes means any substantial contribution of the indicated kind. These are the report's disclosure thresholds, not a decision to grant authorship to a tool. Interaction counts and generated-text volume do not determine the answers.

| Activity | What belongs here |
| --- | --- |
| Asking the research question | Formulating the question, model, definition, relevant assumption, or conjecture: what to study. |
| Coming up with the approach | The overall conceptual plan, such as a reduction, relaxation, or sequence of intermediate claims. |
| Proof development | Important technical ideas that make the plan work, such as a central lemma's technique or crucial inequality. Minor lemmas or constant improvements belong here only when central to the paper's contributions. |
| Writing and exposition | Substantive explanations, proof overviews, argument organization, or explanatory examples. Routine copy-editing belongs under supporting tasks; research ideas also belong in their corresponding categories regardless of who wrote the final text. |
| Checking for bugs | Identifying or correcting consequential errors, such as circularity, a missing hypothesis, or a computation affecting a result. Merely requesting a check does not establish such a contribution; typographical corrections belong under supporting tasks. |
| Other supporting tasks | Substantial assistance with copy-editing, figures, numerical experiments, minor lemmas, literature search, or understanding prior work. Also mark other applicable categories if these tasks influenced the question, approach, or central ideas. |

```text
AI Methodology

Activity                         AI used
Asking the research question      [Yes/No]
Coming up with the approach       [Yes/No]
Proof development                [Yes/No]
Writing and exposition           [Yes/No]
Checking for bugs                [Yes/No]
Other supporting tasks           [Yes/No]

Details. [Contribution-specific account of tools, inputs, proposals,
human development, errors or limitations, and actual checking.]
```

Resolve material unknowns before presenting the table as final; keep an unresolved answer explicitly provisional rather than silently choosing No. No means the category's threshold was not met, not necessarily that no AI interaction occurred. An all-No checklist or a separate no-use statement needs evidence for its full scope. Remove drafting placeholders from a completed section; a provisional draft must identify what remains unresolved.

The Details should explain each Yes through a coherent account, without requiring six separate paragraphs or an interaction log. Name tools and versions where known. Describe human groundwork and inputs, the useful proposals, what was retained or changed, and how claims and attributions were checked. Include consequential unsuccessful attempts, errors, and repairs where relevant. A starter narrative is:

> Before using [tool; model/version if known], [specified authors] had established [human groundwork] and supplied [notes, arguments, pseudocode, data, or other context]. The tool proposed [specific contribution to a named result]. [Specified authors] retained [part], revised or extended [part], and addressed [consequential error or limitation, if any] by [actual correction]. [Specified authors] checked [claims, code, outputs, or attributions] using [actual process and scope]. [Other material assistance, if any].

When relevant, add established intellectual lineage near the idea's introduction in the paper; mentioning the AI tool in Details does not replace credit to prior work. Do not assert that the authors supplied all relevant context if prior chats or memory may have contributed. For reproduction claims, state what the tool received, what was withheld, and which outputs were actually reproduced; distinguish this from an untested reconstruction.

## Editing and proofreading

> **AI assistance.** We used [tool; model/version if known] for language editing and proofreading of [scope]. [The authors / specified authors] reviewed the suggested changes.

Use only for the disclosed editorial role. If a system also supplied proof ideas, substantial drafts, code, or analysis, describe those contributions too. A simple editorial disclosure can be one sentence; it need not acquire a research-style contribution map.

## Implementation or experiments

> **AI assistance.** We used [tool/model] to assist with [specific implementation, benchmark-harness, testing, analysis, or plotting tasks] for [section or artifact]. [Specified authors] reviewed [scope of code] and checked [reported outputs] using [checks actually performed].

Distinguish generating tests from passing them, reviewing code from reproducing experiments, and functional correctness from a security proof. For MPC or proof-system work, identify whether assistance concerned the protocol or prover/verifier implementation, experimental method, or interpretation when that distinction changes the credit. Add writing assistance only if it occurred.

## Research contributions and mixed use

> **Statement on AI use.** [Tool/model] [suggested/developed/generated] [specific construction, proof idea, lemma, or optimization] during [relevant interaction, if useful]. The authors [specified the problem, refined the construction, corrected the argument, or extended the result, as applicable]. We also used [tool/model] for [other actual drafting, coding, or editorial tasks]. [Specified authors] checked [particular arguments, computations, or references] through [actual process, if useful].

Choose attribution verbs from the actual history. If the central idea was generated by the system, say so directly; if it helped express an existing human argument, say that instead. Refer to the affected theorem, lemma, section, or figure when it makes the statement shorter and more informative. Do not turn “we checked Lemma 2” into “all authors verified all proofs.”

## Formalization

> **AI assistance.** We used [tool/model] to assist in generating [proof-assistant code or formalization] for [exact statements]. [Specified authors] [reviewed the code / ran the checker / checked correspondence with the paper, as applicable]. The [checked development / draft formalization] covers [scope] under [relevant assumptions]; [material exclusions] remain outside it.

“Machine-checked” requires an actual successful check of the stated development. Coverage and correspondence with the paper are separate matters; generating code alone establishes neither. If formalization details already appear nearby, cross-reference them instead of repeating a lengthy scope statement.

## Optional responsibility clause

> The authors take responsibility for [the paper's claims and presentation / the implementation and reported results / other agreed scope].

Use when it reflects the authors' position, or label it outside the paragraph as proposed for their adoption. It is not evidence of verification and does not replace missing contribution details. Keep any required venue wording faithful to the current official policy.
