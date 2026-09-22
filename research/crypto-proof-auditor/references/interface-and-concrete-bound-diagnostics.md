# Interface and concrete-bound diagnostics

Load only the implicated case. These self-contained examples test particular implications; they are not a new general audit checklist or attacks on unspecified constructions. Preserve the read-only audit scope and distinguish a failed proof step from a counterexample to the final theorem.

Provenance: adapted from the user-supplied *Learning from Mihir Bellare: A Cryptography Research Distillate* (`mihir_bellare_research_distillate.md`, research date 2026-09-21), §3, Moves 4, 6, and 9; §5; and §8. The report's proposed exercises motivate these diagnostics. No example below is attributed to a particular paper; the event-recognition example uses its own explicit computational premise.

## 1. A PRF theorem does not swap secret and public arguments

**Hypotheses.** Assume `G_n: {0,1}^n x {0,1}^n -> {0,1}^n` is a secure PRF family with the first argument as key. Define

```text
F_n(k,x) = 0^n       if k = 0^n,
           G_n(k,x)  otherwise.
```

In the ordinary PRF experiment the oracle is `F_n(K,.)` for uniform secret `K`, compared with one consistently sampled random function. Couple it to `G_n(K,.)` using the same key: the entire adaptive query transcript is unchanged unless `K=0^n`. Thus, for every oracle distinguisher `D`, with advantage defined as the absolute acceptance-probability difference,

```text
Adv_prf[F_n](D) <= Adv_prf[G_n](D) + 2^(-n).
```

This is one key-sampling event, not an extra `2^(-n)` per query. Now make the second argument a uniform secret `X` and give the adversary oracle access to `F_n(.,X)`. Querying `0^n` and testing whether the answer is `0^n` accepts with probability `1` in this experiment and `2^(-n)` for a random function. Its advantage is `1-2^(-n)`.

**Finding and limit.** This refutes the implication from ordinary PRF security to security with the argument roles swapped. It does not refute an independently proved guarantee for a particular primitive or a game whose admissible inputs exclude this query. Identify the exact altered interface and the missing theorem; do not silently reuse the original PRF assumption.

## 2. Ignoring a key bit preserves ordinary AE but defeats one key-commitment notion

**Hypotheses.** Take a nonce-based authenticated-encryption scheme with uniform key `K`, nonce `N`, associated data `a`, and perfect correctness on valid inputs. Assume its ordinary single-hidden-key confidentiality and ciphertext-integrity guarantees, with the original nonce restrictions and no key-revelation interface. Add an independent uniform bit `b` to the key, and define both algorithms to ignore it:

```text
Enc'_(K,b)(N,a,M) = Enc_K(N,a,M),
Dec'_(K,b)(N,a,C) = Dec_K(N,a,C).
```

Every encryption/decryption oracle transcript in those experiments has exactly the original distribution. The original bounds transfer through forwarding the same queries, with only wrapper overhead.

Now define the commitment experiment explicitly: an adversary outputs two distinct valid key strings `k_0,k_1` and a common tuple `(N,a,C)`; it wins if both decryptions return a plaintext rather than rejection. Choose any valid base key `K`, set `k_0=(K,0)`, `k_1=(K,1)`, and encrypt any valid message under `K` to obtain `C`. Correctness gives

```text
k_0 != k_1,
Dec'_k_0(N,a,C) = Dec'_k_1(N,a,C) = M != rejection.
```

The adversary wins with probability `1`.

**Finding and limit.** Ordinary single-key confidentiality and integrity do not imply this adversarially chosen, distinct-key commitment property. The example does not produce different plaintexts, break the inherited AE experiments, or settle notions using independent challenger-generated keys or identifying functionally equivalent keys. Match the precise commitment game before claiming a separation.

## 3. Raw CBC-MAC fails when its accepted length domain is enlarged

**Interface.** Fix an `n`-bit block permutation `E_K`. Raw CBC-MAC starts at zero, applies `s_i=E_K(s_(i-1) XOR m_i)`, and returns the full final block. Assume the same key authenticates both one- and two-block messages, with no length encoding, domain separation, or extra finalization.

Query the one-block message `m`, receiving `t=E_K(m)`. Output the unqueried two-block message `m || (m XOR t)` with tag `t`. Its chaining values satisfy

```text
s_1 = E_K(m) = t,
s_2 = E_K(t XOR (m XOR t)) = E_K(m) = t.
```

This is a one-query existential forgery with success probability `1`; freshness holds because the forged message has a different length.

**Finding and limit.** A fixed-length theorem does not justify the enlarged domain. The attack is outside a game that accepts only one fixed length, and it does not analyze variants with a proved encoding or finalization mechanism. Check the actual authenticated domain before reporting either the attack or a repair.

## 4. A reduction certifies an upper bound, not a matching attack

**Hypothetical resource contract.** For an application adversary using at most `t` elementary time steps and `q` queries, suppose a reduction constructs `B` with

```text
t_B <= 2t + q c,     q_B <= q+1,
Adv_application(A) <= 2^20 Adv_primitive(B),
```

where `c` is a stated per-query simulation cost in the same time model and there are no omitted additive errors. For `t=2^40`, `q=2^20`, and `c=2^10`, the primitive bound must cover

```text
t_B <= 2^41 + 2^30,     q_B <= 2^20 + 1.
```

If the assumed primitive advantage bound is `2^(-100)` throughout that resource range, the derived application bound is `2^20 * 2^(-100) = 2^(-80)`. A primitive bound known only at time `2^40` or only for `2^20` queries is insufficient for this substitution.

**Finding and limit.** Reporting the original `2^(-100)` application bound is unsupported by this calculation. Reporting a matching `2^(-80)` attack is also unsupported: an upper bound is not a lower bound or an adversary. Do not turn this one advantage bound into an unqualified “80-bit security” label. A sharper analysis may improve certification without changing the construction or any known attack.

As a separate statistical calculation, `2^20` checks with per-step failure probability at most `2^(-40)` conditional on no earlier failure give an overall bound at most `2^(-20)`. The first-failure events are disjoint, and summing their bounds needs no independence. This calculation applies only when those are the checks and conditional bounds established by the protocol, not merely its gate count.

## 5. A large event-probability gap need not yield an efficient distinguisher

**Explicit computational premise.** Assume an efficiently computable, secure length-doubling PRG `G_n: {0,1}^n -> {0,1}^(2n)`: `G_n(U_n)` and `U_(2n)` are computationally indistinguishable for uniform seeds and strings under the chosen PPT model. Define the mathematical event

```text
E(x) := there exists s in {0,1}^n such that G_n(s)=x.
```

Its probabilities satisfy

```text
Pr[E(G_n(U_n))] = 1,
Pr[E(U_(2n))] = |image(G_n)| / 2^(2n) <= 2^(-n).
```

An exact efficient test for `E` would therefore distinguish with advantage at least `1-2^(-n)`, contradicting the stated PRG premise. The event witnesses a large statistical distance; it is not automatically an admissible computational distinguisher. Enumerating all `2^n` seeds gives a correct but exponential-time test; this does not establish an exponential lower bound for every recognition algorithm.

**Finding and limit.** A proof that outputs the indicator of an arbitrary semantic event without supplying its efficient recognition algorithm has an **unjustified reduction step**. Under this explicit premise, the proposed exact test cannot be PPT. This is no unconditional claim that false statements or other semantic events are hard to recognize. If the actual interface supplies a suitable trapdoor, decision oracle, or verifiable witness, analyze that richer comparison separately; for statistical distance the witnessing event need not be efficiently decidable.

**Next obligation.** Write the reduction's decision rule and charge its running time and permitted information. Supply an efficient predicate with the required probability gap, or state why the invoked security notion permits an inefficient observer.
