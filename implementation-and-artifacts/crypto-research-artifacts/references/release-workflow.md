# Release workflow

## Scope and policy

Resolve project instructions, dirty state, accompanying paper, enabled protocol variants and intended audience. When assessing compliance or preparing for a specific submission stage, check current official venue/stage instructions for anonymity, format, limits, external links, evaluation criteria and distribution obligations as applicable. Record the URL, access date and whether the rule is current, historical or unverified. An inaccessible page does not prove rules are absent. A generic planning request can proceed with unverified rules clearly marked; it does not justify a compliance claim.

Use the project's existing release layout; do not create a large documentation hierarchy just to follow a template. Map empirical claims to included components and explicitly mark ideal setup, partial reconstructions, unsupported platforms and uncalibrated parameter regimes. A package that builds does not thereby instantiate a theorem.

For anonymous distribution, inspect content, paths, remote URLs, metadata, filenames, archive ownership/timestamps, symlinks and machine identifiers. Preserve required third-party attribution/licenses. Keep necessary private provenance outside the export when allowed. A pattern scan is evidence about tested patterns, not proof that public source is unrecognizable.

## Package construction

Choose the minimum complete reviewer route. Exclude unrelated development outputs, caches, secrets, stale binaries and obsolete variants unless the requested release requires them. Required input fixtures and expected correctness vectors differ from historical benchmark observations; omitting historical timings must not remove inputs needed to rerun experiments.

Make paper-derived inputs self-contained where needed, with version/content identity and clear measured-versus-derived status. Use stable labels/experiment IDs, not hard-coded table numbers from a different manuscript build. Do not relabel old observations after changing a default or variant.

Pin dependencies and document fetch/offline requirements. Check links and file references in the actual export. Absolute author paths, sibling checkouts, untracked files and developer build caches must not be silent dependencies. Inspect symlink targets, executable bits, archive traversal hazards and platform-specific metadata. Prefer the established packaging script with a manifest over ad hoc recursive copies.

## Detached validation

Create a fresh extraction outside Git, sibling projects and old build outputs. Follow the reviewer commands from that directory. Validate the smallest correctness example, representative experiment and analysis path, expected output/schema, and all documented required inputs; choose larger runs only when needed and feasible.

Record exact commands, host/toolchain/configuration, selected variant, outcomes, time scope and limitations. Separate functional, smoke, full-performance, anonymity and offline checks. Record NOT RUN for unsupported or unexecuted checks; do not convert script syntax checks into a native benchmark pass.

If package contents change after validation, revalidate the affected commands and bind the report to the final archive checksum. Keep a manifest to identify the exact shipped files. Do not claim bitwise reproducibility unless checked under a defined build/environment contract.

When paper/configuration/evidence mismatch remains, state it separately; packaging cannot repair a theorem gap or retroactively recreate an old binary. Apply paper edits only within their authorized scope.
