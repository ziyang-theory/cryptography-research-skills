# Release record: Cryptography Research Skills 0.2.0

Prepared on October 27, 2026 from source commit `54dc589`, with the package version advanced to `0.2.0`. This is the second plugin release candidate after the [published 0.1.0 release](publication-20260921.md).

## Changes since 0.1.0

- Organizes the same twelve skills into Research, Writing, and Implementation collections. The installer preserves legacy collection selections and migrates recognized links from the former layout.
- Expands writing guidance for cryptographic terminology, paragraph coherence, notation, definitions, equations, lemmas, and technical overviews.
- Adds AI Methodology disclosure guidance covering contribution categories, human checks, and unresolved attribution.
- Strengthens proof-review guidance for batching, conditional challenge distributions, release ordering, and resource reuse; expands MPC research examples and correlation accounting.
- Adds safe YAML metadata validation, broader installer and package regression coverage, and eight supplemental behavioral-review fixtures with explicit provenance and grading limits.

The package remains skills-only: twelve skills with local references, no MCP server, hooks, authentication, or publisher-operated endpoint.

## Validation and publication

Local validation completed with Python 3.12.14 and PyYAML 6.0.3:

- All 56 unit tests passed (`python -m unittest discover -s tests -v`).
- Package preflight passed for all 12 skills and 85 files.
- Both the submission and development review fixtures passed their structural/oracle validation. Model behavioral execution was not run for this release.
- An independent rebuild in a fresh temporary output directory produced the identical archive SHA-256.
- `git diff --check` passed.

Existing behavioral results for `0.1.0` do not establish behavioral results for this version. Fixture validation and packaging tests are distinct from model behavioral evaluation and from OpenAI's review.

- Archive: `dist/releases/0.2.0/crypto-research-skills-0.2.0.zip`.
- SHA-256: `ec6cabc6259dbe9f10cc2fd1cebd347dd635e942ae1092b27f5922122b28c53f`.
- Contents: 12 skills, 85 files; 247,029 compressed bytes and 523,898 extracted bytes.
- Build inventory and checksums are retained alongside the archive in ignored `dist/releases/0.2.0/`.

## Portal status

- [Existing plugin management page](https://platform.openai.com/plugins/manage/plugins_6ab0c5fbd69081919fa85386d207bb40).
- [Public directory listing](https://chatgpt.com/plugins/plugins_6ab0c5fbd69081919fa85386d207bb40).
- Draft submission: `appsub_6ae1459fd9a48191bcf6c0aa3e0c2ba4`, uploaded on October 27, 2026. The portal still shows `0.1.0` as the published version.
- The initial upload flagged missing support, privacy policy, and terms URLs. The manifest now links to the existing public package README's support and data-handling sections and the repository's MIT license. No new policy commitments were added. The corrected archive was reuploaded to the same draft.
- Initial archive SHA-256: `af235bf1f88fa2ede7ee7438efd3ba61d60194abb750b55fbc121114627f0ba2`; a copy is retained as `crypto-research-skills-0.2.0-initial.zip` in the release output directory.
- After the corrected upload, the portal showed no blocking metadata findings and one non-blocking request to review the linked privacy explanation against the guidelines. All twelve skill scans subsequently passed. On October 27, 2026, the portal was observed showing version `0.2.0` as **In review**, while `0.1.0` remained published. This is a status observation, not a server-provided submission timestamp.
- The publisher explicitly confirmed all six required attestations and authorized submission followed by publication on approval. The six statements were checked in the portal. They cover OpenAI's terms/guidelines, applicable law, transfers/trades, third-party rights, under-18 suitability, and under-13 targeting/data sharing. Publication is waiting for review approval.
- A ten-minute follow-up was scheduled in the release chat to submit after scans pass and publish after approval, with notifications only on completion, failure, or required publisher action.

## Separate GitHub source release

[GitHub v2.0.0 — Second public release](https://github.com/ziyang-theory/cryptography-research-skills/releases/tag/v2.0.0) was published on October 27, 2026 and marked Latest. It points to source commit `54dc589af0ac14635fc455be9f64d071abe0e4bf`, which contains the same skill sources. It includes release notes and GitHub's source ZIP/tarball. The OpenAI `0.2.0` metadata and release-record commits are maintained on `main` and are not part of that tag. GitHub publication does not establish OpenAI approval or publication.
