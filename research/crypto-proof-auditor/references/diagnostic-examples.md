# Optional proof diagnostics

Use an example only when it tests an implicated proof obligation. These are small, self-contained counterexamples to particular inferences, not a required audit checklist or evidence that a named protocol is insecure. Retain the entrypoint's read-only scope: identifying a missing premise does not authorize changing the theorem or repairing the proof.

Provenance: adapted from the proposed diagnostics in the user-supplied *Learning from Amit Sahai: A Cryptography Research Distillate* (`amit_sahai_research_distillate.md`, research cutoff 2026-09-20), §3, Moves 3 and 5; §6.4; and §9.2. The report presents these as constructed exercises, not discoveries or historical failed attempts attributed to Sahai or his coauthors. The derivations below are self-contained; the hypothetical result in the first example is not a citation to an obfuscation definition.

## 1. Agreement on most inputs does not meet an exact-equivalence premise

**Setup.** Suppose a result permits replacing `Transform(C_0)` with `Transform(C_1)` only when the two deterministic circuits have the same size and input/output domains and satisfy `C_0(x) = C_1(x)` for every input `x`. Assume the other premises hold. For `n >= 1`, fix `x*` in `{0,1}^n` and define

```text
C_0(x) = 0
C_1(x) = 1[x = x*].
```

Pad the circuits to equal size. For uniform `U` in `{0,1}^n`,

```text
Pr[C_0(U) = C_1(U)] = 1 - 2^(-n),
```

but `C_0(x*) != C_1(x*)`. Padding preserves this disagreement. The probability concerns one uniform input; it is not a bound for an adversary that can choose its input or inspect the transformed object.

**Expected finding.** Invoking the stipulated result is a **confirmed error: violated premise**. Its exact-equivalence condition is false. The replacement remains a **proof gap** unless some other argument discharges it. The example does not refute the stipulated result, assert security or insecurity for any named transformation, or refute the final theorem merely because this proof edge fails.

**Next obligation.** Establish exact equivalence for the circuits actually used, or identify and verify a different result whose premises cover their discrepancy and exposed interface. A small disagreement probability alone does not supply that result.

## 2. One additional opening can exhaust a privacy threshold

**Setup.** For secret bit `w`, choose independent uniform bits `R_1, R_2` and set

```text
(S_1, S_2, S_3) = (R_1, R_2, w XOR R_1 XOR R_2).
```

For either value of `w`, any fixed pair of distinct shares is uniform on `{0,1}^2`. For example, for every `a,b`,

```text
Pr[(S_1,S_3) = (a,b) | w]
  = Pr[R_1 = a, R_2 = w XOR a XOR b] = 1/4.
```

The same calculation holds for `(S_2,S_3)`; `(S_1,S_2)` is uniform by construction. Thus the distribution of each fixed pair is independent of `w`. However,

```text
S_1 XOR S_2 XOR S_3 = w.
```

The full triples for `w=0` and `w=1` have disjoint supports and statistical distance `1`. Opening two shares and later the remaining share exposes the same triple: count the union of observations across the execution, not only the number in one message.

**Expected finding.** For this sharing, the assertion that all three openings preserve secret privacy is a **confirmed error**, witnessed by parity. For a different protocol that invokes only a two-view privacy theorem after exposing three views, the conclusion is instead a **violated premise or proof gap** until its actual joint view is analyzed. This calculation does not establish privacy of full MPC views, commitments, adaptive opening mechanisms, or an MPC-in-the-head proof.

**Next obligation.** Reconstruct every exposed object, retained state, and allowed auxiliary information jointly; check that the invoked privacy theorem covers that exposure. Additional data may be redundant in a particular construction, but that redundancy needs an argument.

## 3. Matching marginals does not preserve correlations

**Setup.** Let `R` be a uniform bit and compare

```text
D_0 = (R, R),
D_1 = (R, 1 XOR R).
```

Each individual coordinate is uniform in both distributions. For the efficient test `D(a,b) = 1[a=b]`, however,

```text
Pr[D(D_0)=1] = 1,
Pr[D(D_1)=1] = 0,
Adv_D := |Pr[D(D_0)=1] - Pr[D(D_1)=1]| = 1.
```

Their supports `{00,11}` and `{01,10}` are disjoint, so their statistical distance is `1`. With equal prior probabilities, the test identifies the distribution with success probability `1` (excess over random guessing `1/2`). These are different advantage conventions for the same test.

**Expected finding.** The implication from matching coordinate marginals to equality or indistinguishability of the joint view is a **confirmed invalid inference**. This example refutes that implication, not an arbitrary protocol or replacement whose actual joint distribution has yet to be identified.

**Next obligation.** Specify the complete view, including correlated public information and any retained state included in the experiment, and prove the required joint or conditional comparison. Independence can suffice for some replacements but is not necessary in general; check what joint surroundings the reduction can actually generate.

## Using these as regression cases

Ask an auditor to identify the failed obligation and the strongest justified conclusion. Evaluate the derivation, its scope, and the missing next lemma; recognizing a familiar example or naming a primitive is insufficient. Reword or replace examples for held-out checks, and preserve the distinction between an invalid proof step and a counterexample satisfying the final theorem's hypotheses. These diagnostic cases alone do not establish that a skill improves audit quality on new proofs.
