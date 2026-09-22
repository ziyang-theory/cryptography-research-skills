# Evidence for technical-overview writing

Use this companion to choose examples for a particular explanatory problem. The writing guide contains the reusable instructions; this file supplies source versions and locators. P/N IDs match the abstract/introduction evidence corpus; M IDs identify the separately selected supplemental cases below.

## Scope and method

The 2026-09-06 study reused the previous 53-paper corpus: 50 citation-ranked papers within the screened candidate pool, plus three topical NISC supplements (N01–N03), from CRYPTO, EUROCRYPT, and TCC since 2000. It did not recompute rankings or establish an exhaustive worldwide top 50. All 53 preserved PDFs were screened in full for named and embedded technical exposition, and the identified explanatory units were read completely. This is targeted exposition reading, not a cover-to-cover proof audit.

The classification distinguishes named explanatory units from explanations embedded in results, construction, or proof text. A named unit need not be titled Technical Overview or lie in the introduction. A paper may use both forms; an overview of a prior protocol is background, not its new contribution. Classification describes section purpose and is a reader judgment. The source selection is biased toward older, highly cited papers and the chosen MPC-related topics; citation prominence is not evidence of writing quality or proof validity.

PDF locators below refer to the preserved version. Author full versions and later revisions may differ from conference proceedings. In particular, preserve the version corrections recorded for P43 and P44 in the [abstract/introduction evidence](abstract-introduction-evidence.md); historical explanatory prose cannot establish current security. The local study retains all 53 per-paper notes and SHA-256 source hashes. This portable companion includes selected examples with direct primary-source links and does not depend on that local directory.

## Examples by explanatory purpose

### P10: Founding Cryptography on Oblivious Transfer - Efficiently

[Primary source](https://web.cs.ucla.edu/~sahai/work/web/2008%20Publications/Crypto2008.pdf) · CRYPTO 2008 · Author-hosted CRYPTO 2008 proceedings PDF, 20 pages

**Read:** Section 1.2, “Techniques” (PDF pp. 5–6, proceedings pp. 576–577), in full; Section 3.3 concluding “Proof sketch” (PDF pp. 12–13, proceedings pp. 583–584), in full.

**Use for:** Explain how component guarantees combine and which bad event exceeds their tolerance.

### P11: Unconditionally Secure Constant-Rounds Multi-party Computation for Equality, Comparison, Bits and Exponentiation

[Primary source](https://iacr.org/archive/tcc2006/38760286/38760286.pdf) · TCC 2006 · IACR archive PDF of TCC 2006 paper; downloaded 2026-09-06

**Read:** §3 Bit-Decomposition, PDF pp7–9 before §3.1; Fig.1, PDF p7; §1.3, PDF p4

**Use for:** Give component interfaces before their implementations; separate privacy, correctness, and cost.

### P12: Multiparty Computation with Low Communication, Computation and Interaction via Threshold FHE

Gilad Asharov, Abhishek Jain, Adriana López-Alt, Eran Tromer, Vinod Vaikuntanathan, and Daniel Wichs, [primary source](https://www.iacr.org/archive/eurocrypt2012/72370479/72370479.pdf), EUROCRYPT 2012. Version: 18-page merged proceedings PDF, matching the existing P12 corpus source.

**Read:** §1.1, PDF pp. 3–4, checked 2026-09-22 following the supplied MPC writing guide. Selected introduction passages, not the proofs.

**Mechanism:** The encryption key is available after round I, although the evaluation key is not. Parties can therefore encrypt inputs while generating the evaluation key in round II, then evaluate locally and send decryption messages in round III.

**Use for:** Justify overlap through information available before each message. Separate a valid schedule from correctness and security arguments.

**Qualification:** The malicious-security conversion preserves rounds through semi-malicious security and UC NIZKs; generic coin-flipping would add rounds. The stated three-round result assumes LWE and UC NIZKs in the CRS model with static malicious corruptions. Communication independent of circuit size additionally assumes circular security. Scheduling alone proves none of these security claims.

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

## Supplemental mechanism cases

M01–M03 were selected using the user-supplied Amit Sahai research distillate and checked against primary sources on 2026-09-20. M04–M05 were selected using the Brent Waters distillate and checked on 2026-09-21. M06–M07 were selected using the Mihir Bellare distillate and checked on 2026-09-21. M08 was selected using the supplied MPC writing guide and checked on 2026-09-22. These are supplements to the 53-paper study, not additions to its ranking or coverage claims. Attribute mechanisms to the listed source authors. The suggested writing uses are adaptations, not attributed personal habits or reconstructions of discovery. Reading depth is recorded individually; none is a proof audit.

### M01: Internal MPC views become proof objects

Yuval Ishai, Eyal Kushilevitz, Rafail Ostrovsky, and Amit Sahai, [*Zero-Knowledge Proofs from Secure Multiparty Computation*](https://www.cs.ucla.edu/~sahai/work/web/2009%20Publications/SIAM-IKOS-2009.pdf), SIAM Journal on Computing 39(3), 2009; published electronically September 2, 2009. Version: 32-page author-hosted journal PDF.

**Read:** §1.1, PDF pp. 3–5 / printed pp. 1123–1125, in full; Figure 3.1 and Theorem 3.1, PDF p. 10 / printed p. 1130, also visually checked. Selected passages, not the full paper.

**Mechanism:** The prover shares a witness across virtual MPC inputs, commits to the resulting views, and opens a challenged pair. The overview assigns privacy to the MPC's security against two semihonest parties and soundness to detecting inconsistent views.

**Use when:** A component changes roles. Explain the new exposure and the exact guarantee that survives it before listing the outer protocol's steps.

**Qualification:** Theorem 3.1 assumes an MPC protocol with perfect correctness and semihonest 2-privacy, for $n\geq3$. The resulting ZK protocol uses ideal commitments and has soundness error at most $1-1/\binom{n}{2}$. More openings or merely statistical correctness require additional arguments. View privacy alone does not establish the complete ZK protocol.

### M02: Preserve the statement's algebra

Jens Groth and Amit Sahai, [*Efficient Non-interactive Proof Systems for Bilinear Groups*](https://web.cs.ucla.edu/~sahai/work/web/2008%20Publications/Eurocrypt_Groth2008.pdf), EUROCRYPT 2008, pp. 415–432. Version: 18-page author-hosted proceedings PDF.

**Read:** §1.3, PDF pp. 6–7 / printed pp. 420–421, in full; §1.1's informal result, PDF p. 3 / printed p. 417; Figure 1, PDF p. 4 / printed p. 418, visually checked. Selected passages, not the full paper.

**Mechanism:** The overview treats bilinear-group equations as equations over modules, then explains homomorphic commitments and how commitment randomness changes the equations. Figure 1 makes the supported equation language explicit.

**Use when:** A representation enables the construction. Show which equations and operations it preserves, then explain why those properties help the proof. This case also counters a blanket preference for reducing every statement to Boolean circuits.

**Qualification:** The informal result distinguishes NIWI from NIZK and conditions the latter on the equation type. An algebraic correctness identity does not supply zero knowledge; preserve the chosen language, reference-string distribution, and instantiation's assumption.

### M03: Expose conflicting constraints through candidate repairs

Aayush Jain, Huijia Lin, and Amit Sahai, [*Indistinguishability Obfuscation from Well-Founded Assumptions*](https://arxiv.org/pdf/2008.09317v1), arXiv:2008.09317v1, August 21, 2020. Version: 42-page v1 PDF; locators are not proceedings locators.

**Read:** §4's opening and Technical Overview, PDF pp. 10–13 / printed pp. 8–11, through the handoff to Construction, in full; the two simple cases on printed p. 10 visually checked. Selected passages, not the complete construction or proof.

**Mechanism:** For a structured-seed PRG, storing a full correction defeats expansion; selectively applying sparse corrections makes evaluation depend on sensitive error locations. The overview develops oblivious low-degree correction through matrix factorization, then bucketing to handle correlated bad outputs.

**Use when:** Two requirements appear incompatible. Name what each candidate achieves and violates, then explain the extra operation that reconciles them. Keep the source's hypothetical cases labeled as such.

**Qualification:** This is a component explanation, not a summary or validation of the iO theorem. The final mechanism also handles exceptional buckets by zeroizing and accounting for a public flag; the toy factorization alone does not prove pseudorandomness. The text's order is not evidence of discovery order.

### M04: Explain proof-only modes through a reduction self-test

Brent Waters, [*Dual System Encryption: Realizing Fully Secure IBE and HIBE under Simple Assumptions*](https://link.springer.com/content/pdf/10.1007/978-3-642-03356-8_36.pdf), CRYPTO 2009, pp. 619–636. Version: 18-page proceedings PDF.

**Read:** §1's contribution and self-test discussion, PDF pp. 3–4 / printed pp. 621–622; §3 opening and §§3.1–3.2, PDF pp. 6–9 / printed pp. 624–627. Selected passages; self-test page visually checked.

**Mechanism:** The proof changes the challenge ciphertext, then keys individually, to semi-functional forms. The overview asks whether the reduction could identify a key's form by testing decryption itself. Its embedding forces equal tags for the same identity, so that test fails regardless of the key's form.

**Use when:** Auxiliary modes drive the security argument. Explain their semantics, the apparent distinguishing test, and why the reduction's available interface prevents it. Keep the experiment sequence separate from real execution.

**Qualification:** Semi-functional generation is explicitly excluded from the actual system. Decryption compatibility presupposes matching identities and unequal tags. Explaining the failed self-test does not establish the complete hybrid-view distribution or prove an arbitrary mode-changing construction secure.

### M05: Restore the noise and the rounding margin

Brent Waters, [*A New Approach for Non-Interactive Zero Knowledge from Learning with Errors*](https://simons.berkeley.edu/sites/default/files/2025-07/CRY25-2%20Brent%20Waters_slides.pdf), Simons Institute [talk](https://simons.berkeley.edu/talks/brent-waters-ut-austin-ntt-research-2025-07-15), July 15, 2025. Version: official 28-page slide deck.

**Read:** Slides 11–14, including the construction and the oversimplified/actual binding analyses, in full and visually. Selected slides only; video not watched and the associated paper's proof not reviewed for this case.

**Mechanism:** The idealized derivation makes the rounded bit depend only on the commitment and parameters. The actual expression includes $e_i^T\pi_i$; different short openings can change rounding. The next slide bounds this perturbation and rejects values near rounding boundaries.

**Use when:** A clean identity explains the idea but omits an error term. Put the actual expression beside it and supply the norm bound and margin needed for the inference. Small error alone does not preserve a threshold decision.

**Qualification:** Rejection needs its own accounting: slide 14 identifies a correctness-error option or an alternative accounting through hiding error. This is an exposition example, not a complete NIZK theorem, parameter prescription, or verification of either repair.

### M06: Let the reduction loss motivate the change

Mihir Bellare and Phillip Rogaway, [*The Exact Security of Digital Signatures: How to Sign with RSA and Rabin*](https://cseweb.ucsd.edu/~mihir/papers/exactsigs.pdf), EUROCRYPT 1996. Version: 17-page author-hosted PDF dated March 14, 1996.

**Read:** §§1.2–1.4, PDF/printed pp. 4–6; §4.2 opening, Theorem 4.1, and signing-query simulation, pp. 11–12. Selected passages; theorem page visually checked.

**Mechanism:** The introduction quantifies its FDH reduction's multiplicative loss before motivating PSS's randomized encoding. Theorem 4.1 instead gives additive error terms and explicit runtime overhead. The signing simulation chooses a prospective signature and programs hash answers to make it valid, while accounting for prior-query conflicts.

**Use when:** The contribution improves a quantitative guarantee. Start with the term that obstructs the target bound and explain how the proof or construction removes it. For reanalysis alone, keep the construction fixed in the explanation; this PSS example changes it.

**Qualification:** This is a historical comparison with the paper's FDH analysis in the random-oracle model, not a claim about today's best FDH bounds or recommended RSA parameters. Reduction slack is not evidence of an attack achieving that loss.

### M07: Motivate a definition through its consuming argument

Mihir Bellare and Oded Goldreich, [*On Defining Proofs of Knowledge*](https://cseweb.ucsd.edu/~mihir/papers/pok.pdf), CRYPTO 1992; 28-page author PDF, August 26, 1992.

**Read:** §§1.1–1.3, pp. 3–6; §§2–3, pp. 7–9 (PDF/printed). Selected passages; Definition 3.1 visually checked.

**Mechanism:** Definition 3.1 addresses a consuming protocol's needs with a universal extractor and constant $c>0$. Its validity clause, for $x\in L_R$ and $p(x)>\kappa(x)$, bounds expected witness-extraction work by $|x|^c/(p(x)-\kappa(x))$, given $x$ and oracle $P_x$ under §2's convention.

**Use when:** Explain a consumer's failed inference before the definition repairing it.

**Qualification:** Preserve expected-time and oracle qualifications. This excerpt omits the definition's non-triviality clause and does not establish a general composition theorem.

### M08: Maintain the representation between gates

Elette Boyle, Niv Gilboa, and Yuval Ishai, [*Secure Computation with Preprocessing via Function Secret Sharing*](https://ntt-research.com/wp-content/uploads/2022/07/Secure-computation-with-preprocessing-via-function-secret-sharing.pdf), TCC 2019. Version: 32-page author/employer-hosted full version, identified by its first-page footnote; not proceedings pagination.

**Read:** §1 opening and “The idea in a nutshell,” PDF pp. 2–3 / printed pp. 1–2, through the variants. Selected passages, not the security proof.

**Mechanism:** Both parties maintain a common masked wire value $\widetilde w_j=w_j+r_j$. The dealer supplies FSS keys for offset gates $h(x)=g(x-r_{\mathrm{in}})+r_{\mathrm{out}}$. Evaluating the keys on a masked input gives additive shares whose exchange reconstructs the next masked value. In the circuit-dependent variant, adjacent gates share the corresponding wire mask.

**Use when:** A representation connects repeated local procedures. State the invariant, show one transition, then explain what the next component consumes.

**Qualification:** This explanation concerns the semihonest two-party protocol with trusted-dealer preprocessing over finite Abelian groups. Correct propagation does not establish privacy of joint views, malicious security, or a concrete dealer realization. Generating preprocessing remains a separate obligation; efficient FSS must support the required offset-function family.
