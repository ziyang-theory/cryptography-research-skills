# Plugin review cases

This directory supplies local, synthetic fixtures for exactly five positive and
three negative cases in [`../review-cases.json`](../review-cases.json). It is a
representative behavioral review set, not complete coverage of all twelve skills.
This corpus defines expected outcomes. Its `execution_status: not_run` values are
template defaults, not a summary of execution reports. See the separate
[2026-09-21 behavioral report](../behavioral-review-20260921.md) for observed runs.

The separate [`../development-cases.json`](../development-cases.json) adds eight
development cases for adjacent workflows, valid and invalid proof arguments, and
response versus source completion. It leaves the submission cases unchanged.
Both suites use the same staging, side-effect checker, and optional CLI runner.
The default suite is always `submission`; select `--suite development` explicitly.

All cryptographic examples and numerical observations here were created for this
review set. They are not reproductions of a paper, measurements of real software,
or evidence of cryptographic security. The false statement in P01 is intentional.

## Reproduce a case

1. Install the intended plugin in a fresh Codex test session. Record the candidate
   version and ZIP SHA-256 separately from any observed loaded-package identity,
   plus the Codex/model version, date, and tool restrictions. Mark unknown loading
   origin or content explicitly unverified. Review duplicate skill installations;
   a candidate ZIP hash alone does not identify the instructions actually loaded.
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

## Development cases

| Case | Requested result |
| --- | --- |
| D01 | Symbolic correlation counts and communication accounting |
| D02 | A short evaluation and comparison using supplied synthetic observations |
| D03 | Read-only implementation/specification correspondence review |
| D04 | A short AI-use disclosure from a bounded contribution account |
| D05 | Audit of a complete valid direct joint-distribution proof |
| D06 | Audit of the minimally altered invalid counterpart |
| D07 | Completion of an elementary argument in the response |
| D08 | Insertion of that argument into the named source file |

These prompts do not name skills. Grade the deliverable, side effects, and visible
skill selection separately; selection is unknown when the trace does not expose
it. Equivalent correct workflows are acceptable. A correct direct proof need not
use named hybrids. Research framing and manuscript QA remain outside this set;
the cases do not establish complete coverage or an improvement over a baseline.

```sh
python3 submission/tests/review_cases.py --suite development validate
python3 submission/tests/review_cases.py --suite development prepare D08
python3 submission/tests/review_cases.py --suite development check D08 /printed/workspace /printed/snapshot.json
```

D01–D07 require unchanged files. D08 permits content changes only to the existing
`lemma.md`; additions, deletions, and changes to other files fail the mechanical
check. An unchanged or incorrect `lemma.md` can pass that narrow check: manually
grade the completed proof and diff against the rubric. No exact-byte proof oracle
is imposed. The rubric stays outside every staged workspace.

The unit tests include finite supporting checks of the synthetic mathematical
oracles. They do not replace the general arguments or grade a model response.

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
choose the output location. Use `--suite development` with optional `--case D01`
selections for the supplemental suite. The runner uses fresh workspaces, records
visible responses and tool traces, and checks file effects. It retains `run.json`
and stops with nonzero status if Codex or the checker fails, including a launch
error. Successful mechanical checks leave the behavioral grade `NOT ASSESSED`.

The runner ignores saved user configuration. It disables only the discovered
`~/.agents/skills/<name>/SKILL.md` paths for these twelve skills and their resolved
targets, for that invocation; it does not change saved skill settings. Other
discovery locations and system/global instructions may still apply. Authentication
comes from the existing Codex account.

The repository manifest version and local ZIP SHA-256 are recorded as
`candidate_plugin_version` and `candidate_archive_sha256`. The runner enables the
installed plugin by name without establishing its loading origin or contents:
`loaded_package_binding` remains `UNVERIFIED` and its content identity is null.
It records `model_selection: cli_default`, with no requested override and an
unknown resolved model. These runs show behavior in the recorded environment;
they do not substantiate a regression claim about the candidate archive's exact
bytes. Inspect every response and tool trace manually; successful command exit
codes are not behavioral grades.
