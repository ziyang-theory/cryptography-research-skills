# Plugin review cases

This directory supplies local, synthetic fixtures for exactly five positive and
three negative cases in [`../review-cases.json`](../review-cases.json). It is a
representative behavioral review set, not complete coverage of all twelve skills.
This corpus defines expected outcomes. Its `execution_status: not_run` values are
template defaults, not a summary of execution reports. See the separate
[2026-09-21 behavioral report](../behavioral-review-20260921.md) for observed runs.

All cryptographic examples and numerical observations here were created for this
review set. They are not reproductions of a paper, measurements of real software,
or evidence of cryptographic security. The false statement in P01 is intentional.

## Reproduce a case

1. Install the final packaged plugin in a fresh Codex test session. Record its
   version and ZIP SHA-256, the Codex/model version, date, and any tool restrictions.
   Disable duplicate copies of these skills so the tested package is identifiable.
2. Validate the review materials and stage an isolated input workspace:

   ```sh
   python3 submission/tests/review_cases.py validate
   python3 submission/tests/review_cases.py prepare P01
   ```

   `prepare` prints a new temporary workspace, the exact prompt, and a snapshot
   file. It copies only that case's input fixtures; the expected-answer rubric
   stays outside the test workspace. The preparation script does not run Codex.
3. Start the test session in the printed workspace, submit the exact prompt, and
   save the visible response, tool trace, and workspace diff outside that workspace.
   Use a separate fresh workspace/session for each case. None requires credentials
   or external services. P03 explicitly restricts evidence to the supplied files.
4. Compare the response with every required rubric item in the JSON. A case passes
   only if all required items pass. Accept equivalent mathematically correct
   wording; require exact byte preservation only where stated. Inspect visible
   skill-loading/tool activity if available, without requesting hidden reasoning.
5. Check workspace side effects against the initial snapshot:

   ```sh
   python3 submission/tests/review_cases.py check P01 /printed/workspace /printed/snapshot.json
   ```

   This check verifies file preservation or P02's exact permitted edit. It does
   **not** grade the assistant's response, verify skill selection, or establish
   cryptographic correctness. Record `PASS`, `FAIL`, or `NOT RUN` separately for
   the manual behavioral rubric and the filesystem check. Save actual outcomes in
   a separate run report; do not substitute fixture validation for behavioral runs.

## Negative-case interpretation

- N01 is an out-of-scope routing case: an ordinary grammar edit needs no crypto skill.
- N02 is an unsupported-claim case: supplied functional tests cannot justify a
  claimed 128-bit security theorem.
- N03 is an authorization-boundary case: a planning request must not create an
  archive, run experiments, or publish anything.

N02 and N03 may correctly activate the relevant skill to explain the limitation.
“Negative” means that the specified unwanted behavior must not occur; it does
not mean the assistant should refuse to help with the supported part of the task.

## Optional Codex CLI runner

After installing `crypto-research-skills@personal`, run the synthetic cases with:

```sh
python3 submission/tests/run_codex_review.py --codex /path/to/codex
```

Use repeated `--case P01` arguments to select cases and `--output-dir PATH` to
choose the output location. The runner uses fresh workspaces, records visible
responses and tool traces, and checks file effects. It ignores the saved user
configuration and disables duplicate standalone copies of these twelve skills
for each invocation only; it does not change saved skill settings. System/global
instructions may still apply. The CLI's default model is used, and its resolved
model identifier is not recorded by this runner. Authentication still comes from
the existing Codex account. Inspect every response and tool trace manually;
successful command exit codes are not behavioral grades.
