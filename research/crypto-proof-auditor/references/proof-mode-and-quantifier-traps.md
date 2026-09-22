# Proof-mode and quantifier diagnostics

Use only the case implicated by the disputed inference; the general workflow remains in [reductions-hybrids-and-bounds.md](reductions-hybrids-and-bounds.md). These are hypothetical experiments, not claims about a named construction or instructions to redesign a protocol. A read-only audit reports the failed obligation and does not silently supply a trapdoor, change the target experiment, or weaken a theorem.

Provenance: adapted from the user-supplied *Learning from Brent Waters: A Cryptography Research Distillate* (`brent_waters_research_distillate.md`, research cutoff 2026-09-21), §3, Moves 2, 3, and 6; §4; §§7.3–7.5; and §§9–10. The report proposes diagnostic exercises and evaluation criteria; these self-contained calculations are not reconstructions of Waters's proofs or claims of improved audit performance.

## 1. A simulator secret that would solve the challenge directly

**Toy interface.** A challenger samples independent uniform bits `b,K` and gives the reduction only `X = K XOR b`. The reduction has fresh independent coins, no correlated advice, and no oracle revealing `K`. Here `b` is the challenge mode. A proposed embedding additionally assumes that the reduction holds the actual `K` as a simulator secret, playing the role of a trapdoor.

For each mode, `X` is uniform. Thus every bit-output algorithm `B` with the stipulated interface satisfies

```text
Pr[B(X)=1 | b=0] = Pr[B(X)=1 | b=1],
Pr[B(X)=b] = 1/2.
```

With `K`, the reduction instead computes `X XOR K = b` and succeeds with probability `1`, without invoking its adversary. Sampling an independent `K'` gives `Pr[K'=K]=1/2`; knowing a secret for a separately generated object does not recover the secret for this challenger-generated object.

**Finding and limit.** Under this exact interface, the claimed access to `K` is unavailable, and generating its required joint correlation with `b,X` is impossible. A proof that assumes that access has a **confirmed interface error**; an unspecified method for obtaining the required state is a **proof gap**. This is not an impossibility of proof-only modes or evidence against a final protocol theorem. In another experiment a self-test might be a legitimate attack on the assumption, or the premise might explicitly grant the secret; inspect that interface before diagnosing the problem.

**Next obligation.** Give a sampler for the required joint state from the actual challenge and permitted auxiliary information, or identify which claimed capability was never available. Simulator-only state must be accounted for even when the adversary never receives it.

## 2. Frequent survival can discard all useful advantage

**Toy experiment.** Sample independent uniform `b` in `{0,1}` and `U` in `{0,1,2,3}`. Give an algorithm the transcript `(U,Y)`, where `Y = b XOR 1[U=3]`; the algorithm outputs `Y`. Its success event is `S = {U in {0,1,2}}`. A reduction retains that answer only on nonabort event `E = {U in {0,3}}` and outputs an independent fair bit otherwise. These choices are implementable from the transcript; no cryptographic hardness is asserted for this example.

```text
Pr[S] = 3/4,
Pr[E] = 1/2,
Pr[S | E] = 1/2,
Pr[reduction succeeds]
  = Pr[E AND S] + (1/2) Pr[NOT E]
  = 1/4 + 1/4 = 1/2.
```

With advantage defined as success probability minus `1/2`, the algorithm's advantage is `1/4` and the reduction's is `0`. The tempting expression `1/2 + Pr[E](Pr[S]-1/2) = 5/8` is wrong. For this fallback rule and positive survival probability, the exact identity is

```text
Pr[reduction succeeds] - 1/2
  = Pr[E] (Pr[S | E] - 1/2).
```

**Finding and limit.** Multiplying the original advantage by a nonabort lower bound is a **confirmed invalid inference** without a suitable dependence argument. The example refutes that implication, not every reduction that aborts. Proved independence, suitable transcript-uniform survival bounds, or a different joint-event analysis may justify a particular reduction.

**Next obligation.** Derive the unconditional success or distinguishing expression for the actual experiment and its abort fallback. Do not prescribe artificial abort automatically: first determine which bound or mechanism controls the relevant dependence and can be implemented within the reduction's access and running time.

## 3. A fixed-key bound does not cover setup-dependent key selection

**Toy experiment.** For `n >= 1`, sample public setup `C` uniformly from `{0,1}^n`; every `n`-bit string is an admissible key. Define `Bad(C,k)` to mean `k=C`. For every fixed `k` chosen independently of setup,

```text
Pr_C[Bad(C,k)] = 2^(-n).
```

Yet the efficient algorithm `A(C)=C` has

```text
Pr_C[Bad(C,A(C))] = 1,
Pr_C[for every k, NOT Bad(C,k)] = 0.
```

The first bound therefore implies neither a high-probability simultaneous guarantee over all keys nor security against an efficient key selector that sees setup. A union bound over all `2^n` keys yields only the vacuous upper bound `1` here.

**Finding and limit.** Swapping these quantifiers is a **confirmed invalid inference**; applying fixed-key reasoning to the stronger game leaves a **proof gap or scope overclaim**. The toy attack applies because `k=C` is admissible and setup is exposed before key choice. If an actual definition prevents either condition, this example is not its counterexample. Nor does every malicious-key game require the stronger simultaneous guarantee against all, including inefficient, choices.

**Next obligation.** State setup and key-selection order, admissibility, and algorithm quantifiers explicitly. Prove the guarantee the actual game requires, retaining any dependence of adversarial choices on previously exposed information.

## 4. Pairwise independence can disappear after exposing a seed component

**Toy family.** Let `p >= 3` be prime, take independent uniform `A,B` in `F_p`, and set `F(t)=At+B`. For fixed distinct `u,v`, the map `(A,B) -> (F(u),F(v))` is invertible, so each output pair has probability `p^(-2)`. If `A` is then exposed, however,

```text
F(v) = F(u) + A(v-u).
```

Compare the full views `(A,F(u),F(v))` and `(A,F(u),Z)`, where `Z` is fresh uniform in `F_p`. The equality test for that equation accepts with probabilities `1` and `1/p`, respectively, giving distinguishing advantage `1-1/p` under the difference-of-acceptance-probabilities convention. Unconditioned pairwise independence does not justify the replacement with this seed component retained.

**Finding and limit.** Dropping the exposure is a **confirmed error in the compared view**. This does not make every correlated hybrid invalid. As a positive control, given independent uniform `A,Y`, set `B=Y-Au` and output `(A,Y,Y+A(v-u))`. This efficiently samples exactly `(A,F(u),F(v))`; correlation is preserved by a valid sampler. An actual reduction must have the specified input distribution or justify its replacement.

**Next obligation.** Retain the exposed seed functions and show that the assumption's interface permits generation of the needed joint or conditional distribution. Independence is sufficient in some settings, not a universal requirement.
