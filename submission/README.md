# OpenAI plugin submission

This directory contains release inputs and review materials for the skills-only **Cryptography Research Skills** plugin. The source skills remain in the two existing collections; the build creates a separate distributable layout.

Version **0.1.0** was submitted, approved, and published on **2026-09-21**. See the [publication record](publication-20260921.md) for the directory link, submitted package checksum, and validation evidence.

## Build the package

From the repository root, run:

```sh
python3 scripts/build_plugin.py --check
python3 -m unittest discover -s tests -v
python3 scripts/build_plugin.py
```

The default outputs are the staged plugin in `dist/crypto-research-skills/`, a versioned ZIP, checksums, and a file inventory. The ZIP is the upload artifact; the original source checkout is not a plugin root. Rebuilding unchanged release inputs should produce an identical ZIP. Generated files are ignored by Git.

`plugin.json` is the portable Agent Plugins 1.0 manifest. The build also derives `.codex-plugin/plugin.json` for the supported Codex compatibility format. Both use the same identity and presentation metadata. Skill directories are copied intact under the package's root `skills/` directory. The package includes `LICENSE`, `CITATION.cff`, a package-specific README, and the logo assets; it does not include this submission dossier or test fixtures.

The SVG in `assets/icon.svg` is the editable logo source. `assets/logo.png` is its 512-by-512 PNG rendering for the listing. The listing intentionally has no `interface.screenshots`: the skills-only upload path excludes that field.

## Publisher and listing

- Publisher: Ziyang Jin (individual developer).
- Public support contact: ziyang@cs.toronto.edu.
- Website: https://github.com/ziyang-theory/cryptography-research-skills.
- Display name: Cryptography Research Skills.
- Technical plugin identifier: `crypto-research-skills`. The shorter identifier keeps every `plugin-name:skill-name` within the portal's 64-character limit; the source repository and individual skill names are unchanged.
- Category: Education & Research.
- Initial version: `0.1.0`.
- Availability preference: all regions permitted by the portal.
- Listing copy and three starter prompts: `plugin.json`, under `extensions.com.openai.interface`.

The publisher name and email, repository website, and region preference were confirmed by the publisher on 2026-09-21. Account verification and policy attestations must be completed in the actual publishing organization. Listing configuration and a local package do not establish submission, approval, or publication.

The package adds no server, network client, hooks, authentication, or telemetry. Host tools may read files, browse, run programs, or edit source when requested by the user; their availability and permissions belong to the host. The package README describes these boundaries. Public support correspondence is separate from plugin operation. Do not describe all workflows as read-only: writing, implementation, and artifact workflows can edit files when authorized.

## Review materials

`review-cases.json` contains five positive and three negative cases with self-contained synthetic fixtures under `tests/fixtures/`. Follow its setup instructions and evaluate the observed result against each rubric. Expected outcomes are not test results. Keep actual execution reports separate, record the package hash and runtime, and identify limitations such as a test that loaded a skill explicitly instead of proving automatic routing.

Suggested initial release notes:

> Initial submission of Cryptography Research Skills, a skills-only package with twelve focused workflows for research framing, literature evidence, proof review, technical writing, protocol implementation, benchmarking, evaluation prose, and reproducible artifacts. Includes skill-local references and three starter prompts. No MCP server, hooks, authentication, or publisher-operated endpoint is included. Review fixtures are synthetic and require no account credentials. Review conclusions are scoped assistance, not security certification.

## Submit through OpenAI Platform

1. Select the intended publishing organization and complete individual developer identity verification. The submitter needs Apps Management write access.
2. Open the [plugin submission portal](https://platform.openai.com/plugins), then choose **Create plugin → Skills only**.
3. Upload the versioned ZIP. Check the imported name, version, developer, logo, descriptions, and skills. Inspect any normalization warnings.
4. Supply the starter prompts, review cases, release notes, and availability wherever the skills-only form requests them. Do not enter MCP configuration.
5. Resolve all scan or validation findings. Review the exact policy attestations and their linked terms before accepting them.
6. Submit for review. Record the draft URL, submission identifier, uploaded ZIP hash, and actual status in a local execution report.
7. After approval, publish from the portal. Changes to published skills require a new version and review.

The general submission guide and detailed validator differ in how they describe some materials for skills-only plugins. The current validator explicitly makes website, support, privacy, and terms URLs optional for skills-only ZIPs; it lists five positive and three negative cases as an MCP requirement, while the general guide requests them more broadly. This repository prepares those cases for review regardless. Follow the live form and record what was actually supplied.

## Official references

Checked on 2026-09-21; these are living documents, not pinned specifications:

- [Package your plugin](https://developers.openai.com/plugins/build/plugins).
- [Submit plugins](https://developers.openai.com/plugins/deploy/submission).
- [Submission error reference](https://developers.openai.com/plugins/deploy/submission-errors).

Local validators and tests are preflight checks. Only the portal can establish that its current upload checks, safety scans, and review requirements have passed.
