# Cryptography Research Skills

Twelve focused workflows for cryptography research by Ziyang Jin.

Choose a skill for the requested deliverable. The source collection has four research skills, five writing skills, and three implementation skills; the plugin bundles all twelve. Instructions and references are loaded as needed; no account, credential, MCP server, or external service is bundled.

## Included workflows

### Research

Formulate thoughts clearly by making questions, definitions, assumptions, evidence, and proof obligations explicit.

- `crypto-research-framing`: formulate and refine a research question.
- `crypto-literature-evidence`: trace claims to primary sources.
- `crypto-proof-auditor`: examine proofs under their stated model.
- `crypto-correlation-accounting`: define and normalize correlation units.

### Writing

Communicate supported claims and prepare clear, consistent manuscripts.

- `cryptography-writing`: draft or minimally edit technical prose.
- `crypto-prior-work-comparison`: compare results using compatible claims and costs.
- `crypto-implementation-evaluation-writing`: write claims supported by experimental evidence.
- `crypto-manuscript-qa`: check manuscript sources, builds, and references.
- `crypto-ai-acknowledgements`: describe AI assistance and human checking.

### Implementation

Implement protocols, measure their behavior, and package reproducible artifacts.

- `crypto-protocol-implementation`: relate protocol interfaces and code.
- `crypto-benchmarking`: design and audit reproducible measurements.
- `crypto-research-artifacts`: prepare and validate reproducible artifact packages.

## Example requests

"Audit this cryptographic proof under its stated model. Report gaps without editing the source."

"Improve this cryptography paragraph with the smallest edit that preserves its claim and notation."

"Check whether these benchmark measurements support the comparison and its stated cost boundaries."

## Scope and tools

These are research-assistance workflows, not security certification or machine-checked proofs. Audit conclusions apply only to the examined material and its stated assumptions. A successful build or test does not establish a security theorem.

The host agent supplies file access, browsing, code execution, and any other tools. A workflow can require a local compiler, typesetter, or benchmark environment; the package does not install these dependencies. The agent should report missing tools or evidence and respect the user's scope and permissions.

The package contains instructions, reference notes, and presentation assets. It includes no MCP server, hooks, telemetry, authentication, or publisher-operated data endpoint. The host service handles prompts and files according to its own settings and policies. A requested literature search, external tool, or support email may disclose information through that service; confidential manuscripts should be handled under the user's applicable policies.

## Source, support, and license

- Source and documentation: https://github.com/ziyang-theory/cryptography-research-skills
- Support: ziyang@cs.toronto.edu
- Original materials: MIT License; see `LICENSE`.
- Optional academic citation: see `CITATION.cff`. Citation is appreciated, not required by the MIT License.
- Third-party sources retain their own rights and terms.
