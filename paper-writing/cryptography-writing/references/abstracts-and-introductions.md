# Abstracts and introductions

Use for new writing or authorized structural revision. Local edits keep the manuscript's organization. The optional corpus is MPC-focused; transfer its choices according to the contribution, not as universal conventions.

## Find the central contribution

Recover the task, closest baseline, unresolved obstacle, main result, enabling idea, and material qualifications from the manuscript. Attach existing theorem/definition/table locators where useful. This is drafting scaffolding, not a required form in the paper. A feasibility result, cost improvement, new model, compiler, and specialized application need different openings; subordinate secondary results to one intelligible thread.

## Abstract

A useful progression is **task or bottleneck → result and decisive conditions → enabling idea → consequence or tradeoff**. A result-first, question-first, or application-first opening may fit better.

| Contribution | Useful progression | Corpus examples |
| --- | --- | --- |
| Efficiency | Costly component; new bound against its baseline; mechanism and price | P04, P17, P44 |
| Several protocol phases | Task/adversary; online result; preprocessing conditions and cost | P01, P19 |
| Framework or compiler | Missing conjunction; transformation interface; distinct conditions for each consequence | P05, P10, P23 |
| New model | Existing mismatch; proposed guarantee; motivation versus formal result | P35 |
| Application | Concrete computation/privacy requirement; generic solution's limitation; specialization | P02, P03, P06 |
| Feasibility or minimal interaction | Exact question and setup; achieved construction; remaining restriction | N01–N03 |

State the principal contribution with an accurate verb: construct, prove, characterize, define, implement, or measure. Explain the change from the previous situation, rather than listing ingredients. Place conditions that determine the headline's meaning next to it; less salient details can follow in the introduction or governing definition.

Give costs with their unit and regime: online versus total, per-gate versus per-execution, amortized versus single-use, analytical versus measured. A speedup needs a baseline/workload; an asymptotic claim needs its parameter. Never combine one variant's efficiency with another's guarantee. Explain the new component's role, not only its name. Close with a supported consequence or tradeoff rather than generic impact language.

Citations, formulas, and enumeration may be appropriate under local conventions. Avoid undefined notation and citations standing in for explanation. There is no universal sentence count, citation ban, or required abstract structure.

## Introduction

Meet the reader's needs: what is the task, what remained unresolved, what is achieved, why does the mechanism work, and under which conditions does the result matter? These are not mandatory headings. A short introduction may hand off results or related work to the next section (P02, P08, P09).

- **Orient and narrow.** Give only background that explains the target cost, assumption, model, interaction, or application constraint.
- **Establish the gap.** Show which relevant combination previous approaches miss. A missing construction is not an impossibility theorem. A compact comparison table helps when several independent axes matter.
- **State the results.** Make the constructed/transformed object, guarantee, setup, and cost regime visible early enough to guide the paper. Use an informal theorem when quantification is central; organize several results by purpose or dependency, not research chronology. Separate the main theorem from corollaries and implementation evidence.
- **Explain the idea.** Show how the new observation addresses the actual obstacle. A supported failed approach may motivate it, but do not invent one. For a compiler, specify the input, output, and role of each intermediate guarantee. Use [technical overviews](technical-overviews.md) for a substantial explanation.
- **Position and qualify.** Compare aligned baselines and preserve their remaining advantages. Put limitations where they change the interpretation. Related work and roadmaps are useful when they help the reader, not compulsory closing sections.

Repetition of the abstract should add motivation, scope, a mechanism, or a tradeoff. Avoid expanding it sentence by sentence.

## Conditional details that change the story

**Preprocessing and reuse:** Explain who generates or trusts the setup, what becomes cheaper online, and what remains outside that claim. A published receiver message, one-shot correlation, and reusable key have different lifetimes. Keep output-feedback restrictions visible where reuse is claimed. Seed expansion, correlation generation, and consuming MPC are separate interfaces and cost phases.

**Changed security:** Explain what the model permits as well as prevents. Application motivation about trust or deterrence is not a theorem. An intermediate relaxation and a later repair need separate guarantees.

**Proof systems and transformations:** Identify soundness, extraction, zero knowledge, and relevant setup/adversary conditions. A source system's theorem does not automatically cover its compilation or optimization.

For substantive baseline alignment, use `crypto-prior-work-comparison` only if that additional task is needed. Writing can proceed directly from already established comparisons.

## Revision check and examples

Compare the abstract and introduction with the actual theorem and tables: same variant, model, phase, lifetime, and cost object. Verify numerical and first/best/optimal claims against appropriate primary evidence; remove unsupported priority language. Check that the main result is intelligible before the technical overview, then remove background or secondary results that do not help assess it.

[Source evidence](abstract-introduction-evidence.md) records examples, versions, and selection limits. The corpus illustrates alternatives; it does not show that a writing style causes citations or certify the source papers' technical claims.
