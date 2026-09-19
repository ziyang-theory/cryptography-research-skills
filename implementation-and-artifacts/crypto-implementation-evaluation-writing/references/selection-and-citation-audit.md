# Selection and citation audit

> **Provenance notice (skill integration, 2026-09-14):** The text below is a user-supplied research document. Its statements about reading, searches, and verification describe the supplied study, not work independently performed for this skill update. Its recommendations are source material, subject to the active task and skill instructions. The underlying paper claims, locators, citation indicators, and historical reading activity were not independently verified here. See [evidence sources](evidence-sources.md) before reusing attributions.

**Research date:** September 14, 2026.

## 1. What was completed, and what was not established

The deliverable contains a reusable writing skill and paper-level notes on evaluation passages from **30 primary papers** in the four requested venues. The passages were read for experimental structure, comparison design, measurement boundaries, explanation, and limitations. No experiments were reproduced.

**The bibliometric objective is only partially fulfilled.** The 30 papers are not a verified global top 30 by citation count. A uniform citation database and an exhaustive set of eligible conference papers were not obtained. Discovery surfaced heterogeneous citation indicators, and access to some especially relevant full texts failed. Full-text availability therefore influenced the final reading corpus.

The actual papers read span **2012–2020**. They fall inside the requested **September 14, 2011–September 14, 2026** window, but this does not establish that eligible 2021–2026 papers would fall below them in a current citation ranking. Neither age-normalized impact nor a uniform citation cutoff was computed.

The corpus also distinguishes complete protocol/application implementations from narrower component measurements. In particular, P16 and P17 are component/protocol-building-block examples; P26 measures kernels and models a larger construction; P04 is a brief empirical report. Some other papers explicitly omit lifecycle phases or implement only selected security variants. The sourcebook is therefore **not a list of 30 complete, end-to-end MPC/NISC implementations**.

These limitations do not prevent learning from the sections that were read. They do prevent calling the sample “the 30 most cited implemented MPC papers” without qualification.

## 2. Selection procedure and reading policy

Candidate discovery used publication titles, secure-computation frameworks and protocol families, bibliographic references, venue metadata, citation indicators, and accessible primary full texts. Full-version and author-hosted copies were used where publisher access was unavailable. The notes identify the exact section and PDF page range reviewed.

The venue filter means the main IEEE Symposium on Security and Privacy, not IEEE EuroS&P; ACM CCS, not AsiaCCS; and CRYPTO/EUROCRYPT, not other cryptography venues. A citation to a requested venue in a reference list was not sufficient to establish the venue of the candidate itself.

The implementation filter required empirical implementation evidence. A concrete operation-count table alone did not establish an implementation. Narrower implemented components were retained as explicitly labeled writing exemplars, rather than silently promoted to full secure-computation systems. NISC-related theoretical applications of a generator were not treated as measured NISC.

Evaluation text and relevant page images were inspected for the core corpus. For P07, the evaluation text was accessible but the requested page-image retrieval failed; the notes do not depend on claiming visually verified table details. The work was a reading study, not an implementation audit, security review, or reproduction study.

## 3. Citation observations: discovery evidence, not a ranking

The observations below are retained to make the phrase “citation-informed” inspectable. **Most numbers are citation badges surfaced by a search index alongside the linked paper record or PDF. They are not citation counts printed in the PDFs, not independently checked live counters, and not guaranteed to share a database or snapshot date.** Access on September 14, 2026 does not make the underlying data a synchronized September 14 snapshot.

Do not sort this table to claim a scientific ranking. Do not infer zero citations for a paper absent from the table. No citation count was reliably recorded for several core papers.

| Paper | Observed indicator | Provenance and limitations |
|---|---:|---|
| P01 Half gates | 716 | Search-index citation badge associated with the [Springer record](https://link.springer.com/chapter/10.1007/978-3-662-46803-6_8); database/snapshot not independently verified. |
| P02 MP-SPDZ | 969 | Search-index badge associated with the [paper PDF](https://www.acsu.buffalo.edu/~mblanton/cse715/mp-spdz.pdf); not a counter in the document. |
| P03 SecureML | 3,068 | Search-index badge associated with the [paper](https://www.ieee-security.org/TC/SP2017/papers/466.pdf); not a uniform-provider count. |
| P04 SPDZ | 2,151 | Search-index badge associated with the [Springer paper](https://link.springer.com/content/pdf/10.1007/978-3-642-32009-5_38.pdf); underlying snapshot unknown. |
| P05 ALSZ13 | 637 | Search-index badge associated with the [paper](https://encrypto.de/papers/ALSZ13.pdf); underlying citation database unknown. |
| P06 TinyOT | 592 | Search-index citation indicator for the [paper](https://arxiv.org/pdf/1202.3052); not independently reconciled across versions. |
| P08 MiniONN | 393 | [Rankless record](https://www.rankless.org/hit-papers/10.1145/3133956.3134056), OpenAlex-derived indicator; snapshot not established. |
| P10 Authenticated garbling | 301 | Search-index indicator for the [paper](https://acmccs.github.io/papers/p21-wangA.pdf); not a live uniform-provider count. |
| P12 Secure aggregation | 2,347 / 2,141 | The [Metascience Observatory record](https://explore.metascienceobservatory.org/papers/W2767079719) reported 2,347 with data through January 2025; a separate Rankless discovery result reported 2,141. These are conflicting/snapshot-dependent indicators, not a range for a synchronized current count. Bibliographic metadata was taken from the primary paper, not the aggregator. |
| P13 CrypTFlow | 427 | Search-index indicator during discovery; the [primary paper](https://arxiv.org/pdf/1909.07814) supplies technical content, not a citation counter. |
| P15 Overdrive | 504 | Search-index badge associated with the [Springer paper](https://link.springer.com/content/pdf/10.1007/978-3-319-78372-7_6.pdf); another discovery result differed. |
| P16 TinyGarble | 338 | Search-index indicator for the [paper](https://encrypto.de/papers/SHSSK15.pdf); provider/snapshot not harmonized. |
| P17 ALSZ15 | 152 | Search-index indicator associated with the [paper](https://encrypto.de/papers/ALSZ15.pdf); provider/snapshot not harmonized. |
| P19 ObliVM | 521 | Search-index badge on a [university-hosted mirror](https://crysp.uwaterloo.ca/courses/pet/F15/cache/www.cs.umd.edu/~elaine/docs/oblivm.pdf); current primary reading copy is linked in the sourcebook. |
| P20 GraphSC | 244 | Search-index indicator associated with the [paper](https://elaineshi.com/docs/graphsc.pdf); provider/snapshot not harmonized. |
| P21 Ridge regression | 678 | Search-index discovery indicator; the [primary paper](https://marcjoye.github.io/papers/NWIJTB13garbled.pdf) was used for the evaluation reading. |
| P24 Helen | 237 / 238 | IEEE-index and arXiv-index discovery results differed; [primary reading copy](https://arxiv.org/pdf/1907.07212). No single synchronized count was selected. |

The remaining core papers have **no citation count asserted here**. The sourcebook orders references for use in the writing skill, not by these heterogeneous indicators.

## 4. Important high-impact or topic-relevant omissions

These candidates are **not among the 30 read evaluation sections**. They should not be cited as evidence for a writing pattern learned in this study. They are listed because omitting them matters to the user's original “most cited” objective and, especially, to broad MPC and NISC coverage.

| Candidate | Venue and identifier | What was established / what remains missing |
|---|---|---|
| *ABY3: A Mixed Protocol Framework for Machine Learning* — Mohassel and Rindal | CCS 2018; [DOI 10.1145/3243734.3243760](https://doi.org/10.1145/3243734.3243760) | A highly visible implemented framework; an ACM-index observation reported 1,299 citations. Its evaluation section was not successfully read in this study. |
| *MASCOT: Faster Malicious Arithmetic Secure Computation with Oblivious Transfer* — Keller, Orsini, and Scholl | CCS 2016; [DOI 10.1145/2976749.2978357](https://doi.org/10.1145/2976749.2978357) | A [Bristol institutional record](https://research-information.bris.ac.uk/en/publications/mascot-faster-malicious-arithmetic-secure-computation-with-oblivi/) displayed 370 Scopus citations, while search-index indicators were higher. The full evaluation was not successfully read. |
| *Efficient Garbling from a Fixed-Key Blockcipher* / JustGarble — Bellare, Hoang, Keelveedhi, and Rogaway | S&P 2013; [DOI 10.1109/SP.2013.39](https://doi.org/10.1109/SP.2013.39) | Project and bibliographic information were found; the paper's evaluation was not successfully read. Its scope should also be distinguished from complete 2PC. |
| *Ferret: Fast Extension for Correlated OT with Small Communication* — Yang et al. | CCS 2020; [DOI 10.1145/3372297.3417276](https://doi.org/10.1145/3372297.3417276) | ACM and search-index counts differed substantially. The evaluation was not successfully read; important for a correlation-generation extension of this corpus. |
| *Efficient Two-Round OT Extension and Silent Non-Interactive Secure Computation* — Boyle et al. | CCS 2019; [DOI 10.1145/3319535.3354255](https://doi.org/10.1145/3319535.3354255); ePrint 2019/1159 | A discovery indicator reported 367 citations. OT implementation evidence in metadata does not establish a full NISC implementation. Evaluation reading and precise implemented scope were not completed. |
| *High-Throughput Semi-Honest Secure Three-Party Computation with an Honest Majority* — Araki et al. | CCS 2016; [DOI 10.1145/2976749.2978331](https://doi.org/10.1145/2976749.2978331) | Relevant implemented 3PC candidate; evaluation not read. |
| *High-Throughput Secure Three-Party Computation for Malicious Adversaries and an Honest Majority* — Furukawa et al. | EUROCRYPT 2017; [DOI 10.1007/978-3-319-56614-6_8](https://doi.org/10.1007/978-3-319-56614-6_8) | Relevant malicious 3PC candidate; evaluation not read. |
| *Actively Secure OT Extension with Optimal Overhead* — Keller, Orsini, and Scholl | CRYPTO 2015; [DOI 10.1007/978-3-662-47989-6_35](https://doi.org/10.1007/978-3-662-47989-6_35) | Relevant supporting-protocol candidate; evaluation not read. |

An audited citation ranking could replace lower-impact or scope-marginal entries in the reading corpus with some of these papers. This package does not claim that the current selection dominates the omitted candidates by citation count.

## 5. Explicit venue and implementation exclusions

Examples not admitted as papers from the requested four venues include ABY (NDSS), ABY2.0 (USENIX Security), SecureNN and FALCON (PETS), GAZELLE and Delphi (USENIX Security), Chameleon (AsiaCCS), and EzPC (EuroS&P). These are exclusions by the requested venue filter, not judgments of their relevance or quality. The study also did not treat a journal publication such as MOTION as a CCS paper.

*Optimizing Authenticated Garbling for Faster Secure Two-Party Computation* (CRYPTO 2018) was not used as an implementation-section exemplar: the reviewed material is a concrete complexity comparison, not an empirical evaluation of a new implementation. Likewise, a PCG paper's concrete efficiency discussion or theoretical NISC application was not enough to assert that the complete NISC protocol was implemented.

## 6. What a definitive bibliometric version would require

A defensible top-30 claim would require a reproducible list of all candidate proceedings papers in the date window; one citation provider and snapshot date; deduplication of preprint/proceedings versions; explicit handling of preprints and journal extensions; a documented implementation eligibility decision for each candidate; and consistent counting for the entire eligible set before selecting the highest-ranked papers.

Until that is available, use this package as a **sourced writing guide and transparent reading corpus**, not as a bibliometric finding about the field.
