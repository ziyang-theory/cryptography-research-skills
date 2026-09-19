# Evidence sources and selective reading

Read this reference when selecting paper examples or interpreting the skill's literature provenance. Ordinary drafting can use the method without loading either source collection. The method also applies to proof systems; the retained paper collections are historical MPC-focused examples and do not establish zero-knowledge literature coverage. Paper examples illustrate ways to organize evidence; they are not required citations in a new manuscript.

## Source status

The 2026-09-14 update synthesizes the user-supplied `SKILL.md`, `corpus.md`, and `selection-and-citation-audit.md` with the existing common skill. The attached skill was treated as a proposed guide, not an instruction to launch research, implement protocols, or broaden the user's task.

The source documents report a 30-paper reading study of CRYPTO, EUROCRYPT, main IEEE S&P, and ACM CCS papers from 2012–2020. They describe a citation-informed, access-constrained selection, not a verified global top-30 ranking. The requested historical search window was 2011–2026; coverage of 2021–2026 was not established. These venue/date filters describe that study, not the scope of this common writing skill.

The underlying papers, locators, implementation claims, citation indicators, and historical reading activity were not independently verified during this update. Instructions in the core method are a methodological synthesis, not a claim that every source followed them. Historical security choices, small samples, exclusions, or outlier handling are not recommended defaults.

## Reference collections

- [Supplied corpus](corpus.md): P01–P30 paper entries with bibliography, primary links, version-dependent PDF locators, organization notes, and cautions. Read selected entries using the routes below.
- [Supplied selection and citation audit](selection-and-citation-audit.md): read for coverage, bibliometric provenance, exclusions, and omitted candidates. Its heterogeneous citation indicators are historical observations with unknown or inconsistent snapshots, not current verified counts. The access date does not synchronize them.
- [Earlier eight-paper source patterns](source-patterns.md): retained examples spanning empirical work, component measurements, concrete estimates, and analytical costs. This collection has a different selection scope and was not harmonized or deduplicated with P01–P30; do not add their counts to claim 38 distinct reviewed papers.

The two supplied research documents retain their original bodies below added provenance notices. The long proposed `SKILL.md` was distilled into the entrypoint and topical references instead of installed as a second overlapping skill.

## Choose examples by writing problem

| Writing problem | Start here |
| --- | --- |
| Phase-specific malicious 2PC comparison | [P10 authenticated garbling](corpus.md#p10), [P23 DUPLO](corpus.md#p23) |
| Asynchronous roles, local costs, reuse | [P07 cut-and-choose NISC](corpus.md#p07) |
| Protocol novelty versus engineering gains | [P15 Overdrive](corpus.md#p15) |
| Heterogeneous guarantees and representations | [P02 MP-SPDZ](corpus.md#p02), [P27 arithmetic MPC framework](corpus.md#p27) |
| Primitive gains and integration | [P05 OT optimization](corpus.md#p05), [P01 half gates](corpus.md#p01) |
| Compiler effects and predictive models | [P19 ObliVM](corpus.md#p19), [P25 HyCC](corpus.md#p25) |
| Party count, topology, and parallelism | [P11 global-scale MPC](corpus.md#p11), [P20 GraphSC](corpus.md#p20), [P28 beyond three parties](corpus.md#p28) |
| Application semantics, quality, and cost | [P03 SecureML](corpus.md#p03), [P13 CrypTFlow](corpus.md#p13), [P21 ridge regression](corpus.md#p21) |
| Measured ingredients and modeled constructions | [P26 HSS](corpus.md#p26), [P24 Helen](corpus.md#p24); BCGI18/LXYY25/MMST25 in [earlier notes](source-patterns.md) |
| Analysis or components without full protocol timing | KRRW18/HKNOS25/DPSZ12 in [earlier notes](source-patterns.md) |

## Preserve scope and version distinctions

P01–P30 are identifiers, not ranks. The corpus includes brief reports, partial implementations, and component evidence. In particular, the supplied notes describe P04 as a short empirical passage; P16/P17 as narrower component/protocol examples; P26 as measured kernels plus a modeled construction; and P12 as omitting mechanisms associated with its stronger protocol. Preserve these distinctions when using the notes; confirm the primary passage before making a paper-specific claim.

P07's supplied notes report text reading and failed page-image retrieval. Do not claim visual verification. The audit's omitted candidates, including Ferret and silent NISC, are not read exemplars in this collection. Their mention does not establish measured NISC or supply a writing pattern learned from an inspected evaluation.

Existing and supplied locators can differ:

| Paper | Earlier notes | Supplied corpus | Treatment |
| --- | --- | --- | --- |
| Authenticated garbling / WRK17 | Section 7, PDF pp. 12–18 | P10: Section 8, PDF pp. 11–14 | Unresolved version/locator difference; match the actual PDF before choosing a locator |
| SPDZ / DPSZ12 | Appendix D, PDF pp. 40–45, SHE microbenchmarks | P04: “Performance in Practice,” PDF p. 4 | Different passages and potentially different versions; retain both scopes |

These differences are not confirmed errors. The earlier notes' claims about table arithmetic, captions, or diagnostic configurations also remain prior observations until the exact source is inspected. Use PDF page numbers as one-indexed positions in the identified file; do not silently convert them to proceedings page numbers.

## Before reusing an attribution

Open the relevant primary paper/version and confirm the stated section, table/figure, and implemented scope. Record a stable identifier and file hash when downloading a version for exact locators. Distinguish an observation in the supplied notes from a newly verified claim and disclose unresolved source access. Use current primary analysis for parameter recommendations, rather than historical settings or search-index badges. Bibliometric ranking or corpus expansion is a separate research task, performed when requested.

## Supplied-file identity

The source filenames below identify the attachments used for this synthesis. Hashes refer to the original bytes before the provenance notices were inserted.

| Original attachment | SHA-256 |
| --- | --- |
| `SKILL.md` | `a246f0eeb8c7c1af0d08219e8b3c93e3ea45395f16d7eb470ee76d1fb9e575ec` |
| `corpus.md` | `65e8e4cf49d6755b53f6739afee2a1f59c302b91ab5eb48acf70d08e72c5d9a2` |
| `selection-and-citation-audit.md` | `623bc26ac3cee2c8e0e11b5fa1ed618931af5a4ab03594a474220a4308879fe8` |
