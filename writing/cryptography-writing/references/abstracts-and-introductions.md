# Abstracts and introductions

Use for new writing or authorized structural revision. Local edits keep the manuscript's organization. The optional corpus is MPC-focused; transfer its choices according to the contribution, not as universal conventions.

## Find the central contribution

Recover the task, closest baseline, unresolved obstacle, main result, enabling idea, and material qualifications from the manuscript. Attach existing theorem/definition/table locators where useful. This is drafting scaffolding, not a required form in the paper. A feasibility result, cost improvement, new model, compiler, and specialized application need different openings; subordinate secondary results to one intelligible thread.

When drafting or revising the abstract, introduction, and technical overview together, keep one contribution statement with its supporting sources for each variant. Give the sections complementary jobs:

| Section | Reader should learn |
| --- | --- |
| Abstract | What changed, with the conditions needed to interpret the advance. |
| Introduction | Why that particular advance matters relative to the actual alternatives. |
| Technical overview | Which mechanism or invariant makes the advance possible, and what formal argument remains. |

Consistent claims need not have identical detail. Expand the reason, mechanism, or qualification rather than stretching the same summary three times. For a new draft, explaining the mechanism before finalizing the abstract can expose missing premises; this is an optional drafting order, not a reason to reorganize existing prose. A changed theorem condition must propagate to each affected passage within the authorized edit scope; flag occurrences outside that scope.

## Abstract

A useful progression is **task or bottleneck → result and decisive conditions → enabling idea → consequence or tradeoff**. A result-first, question-first, or application-first opening may fit better.

| Contribution | Useful progression | Corpus examples |
| --- | --- | --- |
| Efficiency | Costly component; new bound against its baseline; mechanism and price | P04, P17, P44 |
| Several protocol phases | Task/adversary; online result; preprocessing conditions and cost | P01, P19 |
| Framework or compiler | Missing conjunction; transformation interface; distinct conditions for each consequence | P05, P10, P23 |
| Primitive definition or construction | Missing interface and its consumer; functionality and security; realization and application conditions | P23, P28 |
| New model | Existing mismatch; proposed guarantee; motivation versus formal result | P35 |
| Application | Concrete computation/privacy requirement; generic solution's limitation; specialization | P02, P03, P06 |
| Feasibility or minimal interaction | Exact question and setup; achieved construction; remaining restriction | N01–N03 |

State the principal contribution with an accurate verb: construct, prove, characterize, define, implement, or measure. Explain the change from the previous situation, rather than listing ingredients. Place conditions that determine the headline's meaning next to it; less salient details can follow in the introduction or governing definition.

Give costs with their unit and regime: online versus total, per-gate versus per-execution, amortized versus single-use, analytical versus measured. A speedup needs a baseline/workload; an asymptotic claim needs its parameter. Never combine one variant's efficiency with another's guarantee. Explain the new component's role, not only its name. Close with a supported consequence or tradeoff rather than generic impact language.

Citations, formulas, and enumeration may be appropriate under local conventions. Avoid undefined notation and citations standing in for explanation. There is no universal sentence count, citation ban, or required abstract structure.

## Introduction

Meet the reader's needs: what is the task, what remained unresolved, what is achieved, why does the mechanism work, and under which conditions does the result matter? These are not mandatory headings. A short introduction may hand off results or related work to the next section (P02, P08, P09).

- **Orient and narrow.** Give only background that explains the target cost, assumption, model, interaction, or application constraint. For an operational model, derive its requirements from when inputs, functions, or participants become fixed and when parties must be available.
- **Establish the gap.** Show which relevant combination previous approaches miss. A missing construction is not an impossibility theorem, and failure to establish the target guarantee is not itself an attack. A compact comparison table helps when several independent axes matter.
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

Compare the requested sections with the actual theorem and tables: same variant, model, phase, lifetime, and cost object. Verify numerical and first/best/optimal claims against appropriate primary evidence; remove unsupported priority language. Check that the main result is intelligible before the technical overview, then remove background or secondary results that do not help assess it.

For a substantial revision, distinguish three questions: can the reader recover the advance and enabling idea; does each claim have support; and does the prose explain component roles without needless repetition? As a targeted check, mentally remove a qualifier such as "online," "amortized," or "with abort." If the apparent theorem changes, retain that qualifier or an equally clear nearby restriction. Smooth prose does not resolve a missing bound or security argument; identify the missing fact, and use visibly unresolved placeholders only in an authorized working draft.

[Source evidence](abstract-introduction-evidence.md) records examples, versions, and selection limits. The corpus illustrates alternatives; it does not show that a writing style causes citations or certify the source papers' technical claims.

The cross-section coordination and revision checks also adapt §§2, 7–8 of the user-supplied *Writing the Abstract, Introduction, and Technical Overview of an MPC Paper* (research date September 22, 2026). Its separate 30-paper selection, citation signals, and reported reading depth are not incorporated into this skill's original corpus or verification claims.
