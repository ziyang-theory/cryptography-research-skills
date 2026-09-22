---
name: crypto-research-framing
description: Clarify exploratory cryptography ideas into precise questions, definitions, candidate lemmas, construction approaches, counterexamples, or obstructions. Use to organize research reasoning and choose the next mathematical step, not polish manuscript prose or audit an existing proof.
---

# Cryptography Research Framing

Organize rough ideas into a clear research question and a useful next mathematical step. Separate established facts, assumptions, conjectures, and unresolved choices before developing a candidate. If the idea is not ready for a construction, a precise formulation of the question and obstacle is a useful result; a modest question needs no grand unifying objective.

## Keep the target fixed

Separate the desired capability from the assumptions and setup available to realize it. Fix, or explicitly leave open, the functionality, leakage, adversary and corruption, composition, abort or delivery, interaction, and quantitative goal when relevant. A missing choice does not authorize selecting an easier theorem. Label changes to these conditions as alternative targets and continue work that does not depend on unresolved choices.

A request for research directions does not authorize manuscript edits or experiments. Do not imitate a researcher's persona, infer individual contributions from coauthorship, or use reputation as evidence for a lemma.

## Develop a candidate

1. State the capability and obstacle. Distinguish an impossibility theorem, a limitation of the current approach, and an intuition.
2. Isolate the intermediate object the argument needs: inputs, outputs, joint law, adversarial choices, exposed state, and simulator information. An ideal functionality performing the entire target may only rename the problem.
3. Compare a few meaningfully different mechanisms. For each serious candidate, identify the missing lemma and a plausible failure. Test the smallest instance that retains the relevant correlations, auxiliary information, and adaptive choices; a passing example is not a proof.
4. Connect the local property to its consumer. Assign correctness, privacy, simulation/extraction, consistency, and error bounds to the components actually responsible. Account for repeated use and retained state.

Select additional guidance by the obstacle:

- [Research moves](references/research-moves.md): change a definition, representation, component role, or assumption.
- [Proof representations](references/proof-representations.md): missing reduction capabilities, proof-only modes, or adaptive timing.
- [Definition and interface gaps](references/definition-and-interface-gaps.md): intended use exceeds the available theorem or quantitative bound; includes an optional simulation example.
- [MPC worked examples](references/mpc-worked-example.md): isolate preprocessing and communication, or prove a double-sharing masking claim for a collector's complete view.

These are optional methods and hypothetical exercises, not a sequence every project must complete.

## Return the mathematical result

Give a candidate lemma with a proof attempt, a counterexample identifying the violated requirement, a justified local transformation, or a precise remaining obstacle. State what is derived, assumed, source-supported, or open, and which unresolved premise most affects the next step. Do not promote a local calculation to whole-construction security.

Verify paper-specific mechanisms and theorem premises against versioned primary sources. Separate their claims from proposed adaptations and explanatory failed candidates. Use `crypto-literature-evidence` for additional source research, `crypto-proof-auditor` for a substantive validity audit, or `cryptography-writing` for authorized manuscript drafting only when that separate task is needed.
