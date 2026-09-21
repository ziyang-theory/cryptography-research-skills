# Comparing complete theorem variants

Use these cases to diagnose a specific comparison error, not as a general survey. Selected from §9.2 of the user-supplied *Learning from Brent Waters: A Cryptography Research Distillate* (research cutoff September 21, 2026), then checked against primary sources that day. Only the cited passages were inspected; proofs were not audited. The diagnostic prompts are original adaptations. Preserve the target manuscript's scope when applying them.

## Registered ABE: keep the properties in the same row

**Source.** Roy Stracovsky, Brent Waters, and David J. Wu, *Pairing-Based Registered ABE for Boolean Formulas with a Linear-Size CRS*, [ePrint 2026/1062](https://eprint.iacr.org/2026/1062), May 27, 2026. [Author PDF](https://www.cs.utexas.edu/~dwu4/papers/RegisteredABE-Linear.pdf), 48 pages; SHA-256: `5dfc26dedf821aa129e1ce77fbc01c26dca673cf0b24a5c3838b58a22abbff6d`.

**Source facts.** Table 1 (p. 3) and Corollaries 4.13–4.14 (pp. 30–31; PDF/printed numbering coincides) share linear-secret-sharing policies over the scalar field and q-type Assumption 4.4. Below, `N` bounds users, `lambda` is security, and `K` bounds policy size.

| Corollary | Security and model | Index space | CRS size |
| --- | --- | --- | --- |
| 4.13 | Static, plain model; index set declared upfront, no user corruptions | `{0,1}^lambda` | `N * poly(lambda, log N)` |
| 4.14 | Adaptive, random-oracle model; subexponential security of Assumption 4.4; a priori bound `K` | `[N]` | `N * poly(lambda, K, log N)` |

Static/adaptive use the paper's registered-ABE definitions. “Plain model” retains the structured CRS. [Corollaries 4.13–4.14](https://www.cs.utexas.edu/~dwu4/papers/RegisteredABE-Linear.pdf#page=30).

**Original diagnostic.** Trace a claimed adaptive/plain-model/arbitrary-identifier combination to one corollary. Preserve policy-size costs. An unsupported combination is not an impossibility result.

## NIZK-to-ZAP: retain the quantitative premises

**Source.** Anish Banerjee, Brent Waters, and David J. Wu, *From NIZK Arguments to ZAPs, Generically*, [ePrint 2026/886](https://eprint.iacr.org/2026/886), May 6, 2026. [Author PDF](https://www.cs.utexas.edu/~dwu4/papers/ZAP-Generic.pdf), 58 pages; SHA-256: `c8f889e17792d9e4d1380a9770eeada80d2c914eae2e8d0a33e50053ee3918e9`.

**Source facts.** Informal Theorem 1.1 (p. 2) requires a NIZK argument for NP in the common random string model and a sometimes-constricting generator, both with subexponential security. The resulting ZAP argument has subexponential security, preserving computational versus statistical witness indistinguishability. The following paragraph permits either input, but not both, to have quasipolynomial security, yielding quasipolynomial security. [Theorem 1.1 and qualification](https://www.cs.utexas.edu/~dwu4/papers/ZAP-Generic.pdf#page=2).

Here `(1, epsilon)` bounds advantage by `epsilon(lambda) * negl(lambda)` against polynomial-time adversaries (§2, p. 9); these labels do not themselves assert subexponential running-time security. Formal application retains nonuniformity (Theorems 3.4 and 3.9; Remark 3.13). Section 3.1 (pp. 22–23) requires `(1, mu*epsilon)` NIZK non-adaptive soundness, `(1, epsilon)` NIZK non-adaptive witness indistinguishability, and `(1, epsilon)` versions of the generator's mode indistinguishability, `mu`-guessing security, and target randomness, alongside completeness. [Quantitative extension](https://www.cs.utexas.edu/~dwu4/papers/ZAP-Generic.pdf#page=22).

**Original diagnostic.** Test “any polynomially secure NIZK gives a ZAP.” Identify the missing component, setup distribution, advantage bounds, and adversary class; check the cited implication before asserting a stronger conversion.

## Reuse

The URLs are mutable. Match a future source to the recorded snapshot or recheck its theorem statements and locators. When adapting either case, retain the complete supported variant or list the unresolved premises; do not fill them with desirable features from another row.
