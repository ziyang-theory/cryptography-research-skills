# Evidence for technical-overview writing

Use this companion to choose examples for a particular explanatory problem. The writing guide contains the reusable instructions; this file supplies source versions and locators. IDs match the abstract/introduction evidence corpus.

## Scope and method

The 2026-09-06 study reused the previous 53-paper corpus: 50 citation-ranked papers within the screened candidate pool, plus three topical NISC supplements (N01–N03), from CRYPTO, EUROCRYPT, and TCC since 2000. It did not recompute rankings or establish an exhaustive worldwide top 50. All 53 preserved PDFs were screened in full for named and embedded technical exposition, and the identified explanatory units were read completely. This is targeted exposition reading, not a cover-to-cover proof audit.

The classification distinguishes named explanatory units from explanations embedded in results, construction, or proof text. A named unit need not be titled Technical Overview or lie in the introduction. A paper may use both forms; an overview of a prior protocol is background, not its new contribution. Classification describes section purpose and is a reader judgment. The source selection is biased toward older, highly cited papers and the chosen MPC-related topics; citation prominence is not evidence of writing quality or proof validity.

PDF locators below refer to the preserved version. Author full versions and later revisions may differ from conference proceedings. In particular, preserve the version corrections recorded for P43 and P44 in the [abstract/introduction evidence](abstract-introduction-evidence.md); historical explanatory prose cannot establish current security. The local study retains all 53 per-paper notes and SHA-256 source hashes. This portable companion includes 18 examples with direct primary-source links and does not depend on that local directory.

## Examples by explanatory purpose

### P10: Founding Cryptography on Oblivious Transfer - Efficiently

[Primary source](https://web.cs.ucla.edu/~sahai/work/web/2008%20Publications/Crypto2008.pdf) · CRYPTO 2008 · Author-hosted CRYPTO 2008 proceedings PDF, 20 pages

**Read:** Section 1.2, “Techniques” (PDF pp. 5–6, proceedings pp. 576–577), in full; Section 3.3 concluding “Proof sketch” (PDF pp. 12–13, proceedings pp. 583–584), in full.

**Use for:** Explain how component guarantees combine and which bad event exceeds their tolerance.

### P11: Unconditionally Secure Constant-Rounds Multi-party Computation for Equality, Comparison, Bits and Exponentiation

[Primary source](https://iacr.org/archive/tcc2006/38760286/38760286.pdf) · TCC 2006 · IACR archive PDF of TCC 2006 paper; downloaded 2026-09-06

**Read:** §3 Bit-Decomposition, PDF pp7–9 before §3.1; Fig.1, PDF p7; §1.3, PDF p4

**Use for:** Give component interfaces before their implementations; separate privacy, correctness, and cost.

### P13: Keyword Search and Oblivious Pseudorandom Functions

[Primary source](https://iacr.org/archive/tcc2005/3378_304/3378_304.pdf) · TCC 2005 · IACR archive PDF of TCC 2005 paper; downloaded 2026-09-06

**Read:** §3, PDF pp7–10; §4.2, PDF pp13–15; §5.2, PDF pp17–20, especially Challenges / Our construction / Notion of privacy

**Use for:** State what a simpler security intuition fails to establish and name the extra property needed.

### P14: An Efficient Protocol for Secure Two-Party Computation in the Presence of Malicious Adversaries

[Primary source](https://eprint.iacr.org/2008/049.pdf) · EUROCRYPT 2007 · 36-page ePrint full version; first-page footnote identifies EUROCRYPT 2007 extended abstract.

**Read:** §3 opening, PDF pp.9–10; §3.1, “High-Level Overview,” PDF pp.10–11; §3.2, explanatory consistency-check discussion, PDF pp.11–15; Figure 2, PDF p.13 / printed p.12.

**Use for:** Explain cross-component consistency obligations when the construction does not admit a fully modular account.

### P16: A New Approach to Practical Active-Secure Two-Party Computation

[Primary source](https://eprint.iacr.org/2011/091.pdf) · CRYPTO 2012 · ePrint 2011/091 author full version, 42 pages

**Read:** Section 1.2, “Overview of Our Approach” (PDF pp. 4–6), including Figure 1, in full; Appendix J, “Full Overview Diagram”, Figure 27 (PDF p. 42), visually inspected in full.

**Use for:** Use one gate and a short dependency graph to motivate authenticated intermediate resources.

### P17: Two Halves Make a Whole: Reducing Data Transfer in Garbled Circuits Using Half Gates

[Primary source](https://eprint.iacr.org/2014/756.pdf) · EUROCRYPT 2015 · 28-page author/ePrint version headed 'In 34th Eurocrypt, Sofia, Bulgaria, April 2015'.

**Read:** §3.1, “Approach,” PDF pp.5–7; combination identity and transition to §3.2, PDF p.7.

**Use for:** Let a telling identity explain how small cases combine and where the saving comes from.

### P20: Universally Composable Security with Global Setup

[Primary source](https://iacr.org/archive/tcc2007/43920061/43920061.pdf) · TCC 2007 · IACR archive PDF of TCC 2007 paper; downloaded 2026-09-06

**Read:** §2 Generalized UC Security, PDF pp7–12; §5.1 High-level description of the protocol, PDF pp21–23; Figs.1 and7, PDF pp9 and23

**Use for:** Motivate model changes through the experiment's operational capabilities.

### P22: Efficient Oblivious Pseudorandom Function with Applications to Adaptive OT and Secure Computation of Set Intersection

[Primary source](https://iacr.org/archive/tcc2009/54440575/54440575.pdf) · TCC 2009 · IACR archive PDF of TCC 2009 paper; downloaded 2026-09-06

**Read:** §1 Technical Roadmap, PDF pp4–5, ending before Related Concurrent Work; formal Fig.1, PDF p10

**Use for:** Label a teaching construction that differs from the actual protocol and identify the change.

### P28: Efficient Pseudorandom Correlation Generators: Silent OT Extension and More

[Primary source](https://www.iacr.org/archive/crypto2019/116940471/116940471.pdf) · CRYPTO 2019 · IACR CRYPTO 2019 archive extended abstract, 30 pages

**Read:** Section 2, “Technical Overview of Constructions”, including 2.1–2.7 (PDF pp. 11–16), in full; stops before Section 3.

**Use for:** Explain a common method once, then isolate each specialization's compatibility requirement.

### P29: Perfectly-Secure MPC with Linear Communication Complexity

[Primary source](https://iacr.org/archive/tcc2008/49480207/49480207.pdf) · TCC 2008 · IACR archive PDF of TCC 2008 paper; downloaded 2026-09-06

**Read:** §4 Protocol Overview, PDF pp6–7; §6.1 Overview, PDF p9 through Definition4

**Use for:** Pair a short global map with a later local overview of the difficult ingredient.

### P36: PSI from PaXoS: Fast, Malicious Private Set Intersection

[Primary source](https://eprint.iacr.org/2020/193.pdf) · EUROCRYPT 2020 · 36-page author/ePrint version associated with EUROCRYPT2020.

**Read:** §4.1, “Overview,” PDF pp.9–10; proof-critical modifications in §4.2 opening, p.10; §5.1, “Overview,” PDF pp.17–18.

**Use for:** Explain why a simple structural case works, what breaks in the extension, and what restores it.

### P38: Two-Round Secure MPC from Indistinguishability Obfuscation

[Primary source](https://iacr.org/archive/tcc2014/83490162/83490162.pdf) · TCC 2014 · IACR archive PDF of TCC 2014 paper; downloaded 2026-09-06

**Read:** §1.3 Our Techniques, PDF pp3–5, ending before §1.4

**Use for:** Use an explicitly hypothetical stronger primitive to expose the idea, then explain the actual proof pivot.

### P39: Round-Optimal Secure Two-Party Computation

[Primary source](https://web.cs.ucla.edu/~rafail/PUBLIC/64.pdf) · CRYPTO 2004 · Author-hosted version, 24 pages; author publication page identifies CRYPTO 2004

**Read:** Section 4 opening informal overview through the four technique bullets, before the formal circuit-family definition (PDF pp. 10–11); the formal description begins on PDF pp. 11–12.

**Use for:** Explain round savings through when information must be fixed, known, and revealed.

### P45: On the Limitations of Universally Composable Two-Party Computation without Set-up Assumptions

[Primary source](https://eprint.iacr.org/2004/116.pdf) · EUROCRYPT 2003 · 30-page full version dated May17,2004; first-page footnote identifies EUROCRYPT2003 extended abstract.

**Read:** §1, named run-in “Techniques,” PDF p.4 / printed p.3; embedded proof-opening intuition for Lemma 3.3, PDF p.10 / printed p.9; Figure 1, PDF p.11 / printed p.10.

**Use for:** Make the lower-bound strategy visible through the simulator's interface and a concrete adversarial experiment.

### P48: Breaking the Circuit Size Barrier for Secure Computation under DDH

[Primary source](https://eprint.iacr.org/2016/585.pdf) · CRYPTO 2016 · ePrint 2016/585 author full version dated September 2, 2016, 47 pages

**Read:** Section 1.2, “Overview of Techniques” (PDF pp. 4–6); Section 3.2, “Overview of construction” through Remarks 3.3–3.5 before Claim 3.6 (PDF pp. 11–13, including Figure 1); Sections 4.1.1 and 4.2.1, both “Overview” (PDF pp. 28–29 and 32), all in full.

**Use for:** Retract temporary pedagogical fictions explicitly and carry representation invariants across abstraction levels.

### N01: Efficient Non-interactive Secure Computation

[Primary source](https://www.cse.iitb.ac.in/~mp/pub/nisc-proceedings.pdf) · EUROCRYPT 2011 · 20-page author-hosted proceedings version, EUROCRYPT2011; explicit NISC topical supplement.

**Read:** §1.2, “Overview of Techniques,” PDF p.5; §3.1, “Overview of New Protocol,” PDF p.10; adjacent security qualification and repair in §3.2, PDF pp.10–11; §3.3 construction and analysis, PDF pp.12–13.

**Use for:** Name intermediate security guarantees and explain how later transformations repair their limitations.

### N02: Reusable Non-Interactive Secure Computation

[Primary source](https://www.iacr.org/archive/crypto2019/116940362/116940362.pdf) · CRYPTO 2019 · IACR CRYPTO 2019 archive PDF, 28 pages

**Read:** Section 2, “Overview of the Techniques”, including 2.1–2.3 (PDF pp. 7–18), in full; Figure 1 on PDF p. 16 visually inspected. Stops before Section 3.

**Use for:** Track deferred obstacles; distinguish an exposition dependency from the formal construction.

### N03: Mr NISC: Multiparty Reusable Non-Interactive Secure Computation

[Primary source](https://eprint.iacr.org/2020/221.pdf) · TCC 2020 · Author ePrint 2020/221, revised 2021-07-01; marked major revision of TCC 2020, including style improvements; PDF retains “Mr NISC” title

**Read:** §2 Technical Overview, PDF pp9–15 before §3; §§2.1–2.3; Eqs.(3)–(6), PDF pp13–14

**Use for:** Organize a nested construction from its security interface down to one representative operation.
