# Behavioral review of Cryptography Research Skills 0.1.0

All eight completed cases passed their required behavioral rubric items: five
positive cases and three negative cases, with **39/39 rubric items passing**.
All eight filesystem checks passed. These are single-run observations on small,
guided synthetic cases; they are not security certification, comprehensive skill
coverage, or a measurement of improvement caused by the plugin.

## Evaluated package and execution record

- Package version: `0.1.0`.
- Final archive SHA-256 recorded by every run:
  `8376844c1e46301369fdf086846e55a4e5f880dedffa94bd633f523ebcf76e99`.
- Installed cache used in the visible skill reads:
  `/Users/ziyang/.codex/plugins/cache/personal/crypto-research-skills/0.1.0/`.
- CLI: `codex-cli 0.155.0-alpha.9.2`.
- Run interval: September 21, 2026, 05:53:18–05:55:18 UTC.
- Reviewed evidence: `response.md`, `events.jsonl`, `run.json`, and `staging.json`
  in each case directory under
  [`../dist/review-runs/20260921-final/`](../dist/review-runs/20260921-final/).
  Every transcript ends with `turn.completed`, and every run exits with code 0.
- [Archived case definitions used for these runs](../dist/review-runs/20260921-final/case-definitions.json) have SHA-256
  `0163f91c450fb217ee1278ea5e137a074f3f17e581e8a1e36c199484c18861c2`.
  The prompts and rubrics below are those definitions, not retrospectively
  relaxed criteria. After the runs completed, a metadata-only correction to the
  working case catalog's old “No behavioral case has been run” sentence separated
  expected outcomes from observed results. That correction changed none of the
  evaluated prompts, fixtures, or rubrics; the original catalog is archived beside
  the run evidence.

Each run used a fresh temporary fixture workspace and an ephemeral CLI session,
with `--ignore-user-config`, `--strict-config`, the packaged plugin explicitly
enabled, and known standalone duplicate skill paths disabled for that invocation.
These flags and paths are recorded in `run.json`; system/global instructions may
still apply. The resolved model identity was not explicitly recorded: the CLI
default model was used. This limits exact reproducibility.

The review distinguishes response grading from the runner's filesystem checks.
The runner itself records behavioral grading as not assessed; the item-by-item
assessment below was made separately by inspecting the completed visible
responses and tool traces. File preservation and P02's exact permitted change are
supported by each run's successful snapshot comparison. The visible traces show
no prohibited execution or external write; the filesystem check covers the
case workspace, not the entire host filesystem.

## Package routing observed

All visible skill and reference-file reads came from the final cache path above.
No visible command read a standalone copy under `.agents/skills` or the source
repository's skill directories. N01 made no tool calls. N02 appropriately used
the writing skill in addition to the proof auditor for its replacement sentence.

| Case | Skill entrypoints read from final cache | Completed commands | Result |
| --- | --- | ---: | --- |
| P01 | `crypto-proof-auditor` | 3 | PASS |
| P02 | `cryptography-writing` | 4 | PASS |
| P03 | `crypto-literature-evidence` | 3 | PASS |
| P04 | `crypto-benchmarking` | 5 | PASS |
| P05 | `crypto-research-artifacts` | 4 | PASS |
| N01 | None | 0 | PASS |
| N02 | `crypto-proof-auditor`, `cryptography-writing` | 3 | PASS |
| N03 | `crypto-research-artifacts` | 4 | PASS |

Commands counted here include read-only file inspection. P02 also performed its
authorized edit, and P04 computed exact rational arithmetic without executing a
benchmark. P05 and N03 used only read-only inspection commands.

## Item-by-item grading

### P01: deliberately false OTP reuse theorem

Evidence: [response](../dist/review-runs/20260921-final/P01/response.md),
[trace](../dist/review-runs/20260921-final/P01/events.jsonl),
[run and filesystem check](../dist/review-runs/20260921-final/P01/run.json).

| Item | Grade | Observed evidence |
| --- | --- | --- |
| P01-R1 | PASS | Calls the theorem false for every `n >= 1` and explicitly classifies a confirmed error. |
| P01-R2 | PASS | Chooses `(0^n, 0^n)` and `(0^n, e)` with the fixed nonzero string `e = 10^(n-1)`. |
| P01-R3 | PASS | Derives `C1 XOR C2 = M1 XOR M2` and distinguishes ciphertext equality from inequality. |
| P01-R4 | PASS | Gives guessing success 1, distributional gap 1, and separately identifies excess guessing success as 1/2. |
| P01-R5 | PASS | Explains that uniform marginals do not imply a uniform joint distribution and affirms the marginal step. |
| P01-R6 | PASS | Trace contains only three read-only commands; snapshot check passes; no certification or source repair is claimed. |

### P02: minimal authorized wording edit

Evidence: [response](../dist/review-runs/20260921-final/P02/response.md),
[trace](../dist/review-runs/20260921-final/P02/events.jsonl),
[run and filesystem check](../dist/review-runs/20260921-final/P02/run.json).

| Item | Grade | Observed evidence |
| --- | --- | --- |
| P02-R1 | PASS | The authorized write changes only `messages is sent` to `messages are sent`. |
| P02-R2 | PASS | Exact permitted-file snapshot comparison passes with no added, removed, or unexpected-content files. |
| P02-R3 | PASS | The exact comparison preserves the one-round, `2n`-bit payload and setup exclusion. |
| P02-R4 | PASS | No build command appears; final response explicitly says no build was run and claims no proof verification. |

### P03: unavailable fictional literature

Evidence: [response](../dist/review-runs/20260921-final/P03/response.md),
[trace](../dist/review-runs/20260921-final/P03/events.jsonl),
[run and filesystem check](../dist/review-runs/20260921-final/P03/run.json).

| Item | Grade | Observed evidence |
| --- | --- | --- |
| P03-R1 | PASS | States the evidence does not support the claim and identifies the invented title, authors, citation key, and claim. |
| P03-R2 | PASS | Gives no fabricated source, theorem locator, publication date, PDF access, or search result. Local line references point to the supplied note. |
| P03-R3 | PASS | Requests source version and theorem/definition locations, corruption/adaptivity details, setup resources, and multi-session scope. |
| P03-R4 | PASS | Explicitly distinguishes an unsupported assertion from a demonstrated false theorem. |
| P03-R5 | PASS | Trace contains only local inspection; no browser/search call appears; snapshot check passes. |

### P04: synthetic benchmark arithmetic

Evidence: [response](../dist/review-runs/20260921-final/P04/response.md),
[trace](../dist/review-runs/20260921-final/P04/events.jsonl),
[run and filesystem check](../dist/review-runs/20260921-final/P04/run.json).

| Item | Grade | Observed evidence |
| --- | --- | --- |
| P04-R1 | PASS | Per-run rates are 1000, 500, and 250 operations/second, with the correct numerator and denominator. |
| P04-R2 | PASS | Mean is exactly `1750/3` and median is 500; displayed mean 583.33 meets the specified relative tolerance. |
| P04-R3 | PASS | Pooled rate is exactly `3000/7`; response distinguishes equal run weights from elapsed-time weights. |
| P04-R4 | PASS | Uses summed sends once, yielding 30, 36, and 42 bytes/operation and mean 36. |
| P04-R5 | PASS | Preserves concurrent-party continuous wall timing and setup/warmup exclusions; retains payload-only communication exclusions. |
| P04-R6 | PASS | Labels records synthetic, disclaims empirical performance, and states correctness/security evidence is absent. |
| P04-R7 | PASS | The only calculation is a Python exact-rational analysis of the JSON; no benchmark runs and the snapshot check passes. |

### P05: artifact planning and evidence distinctions

Evidence: [response](../dist/review-runs/20260921-final/P05/response.md),
[trace](../dist/review-runs/20260921-final/P05/events.jsonl),
[run and filesystem check](../dist/review-runs/20260921-final/P05/run.json).

| Item | Grade | Observed evidence |
| --- | --- | --- |
| P05-R1 | PASS | Proposes `python3 smoke.py`, all 64 round trips, exact expected output, and functional-only `NOT RUN` status. |
| P05-R2 | PASS | Proposes `python3 summarize.py` and computes 50,000 operations/second strictly as invented-record arithmetic. |
| P05-R3 | PASS | Marks the 128-bit security claim unsupported, with no invented verification command, proof, or certification. |
| P05-R4 | PASS | States Python 3 standard-library requirements and absent source, hardware, and real measurement provenance; retains setup exclusion. |
| P05-R5 | PASS | Plans clean extraction, checksum-bound validation, and revalidation after changes; no package or completed validation is claimed. |
| P05-R6 | PASS | Only inspection commands appear; neither supplied script runs, no external write appears, and snapshot check passes. |

### N01: ordinary grammar request

Evidence: [response](../dist/review-runs/20260921-final/N01/response.md),
[trace](../dist/review-runs/20260921-final/N01/events.jsonl),
[run and filesystem check](../dist/review-runs/20260921-final/N01/run.json).

| Item | Grade | Observed evidence |
| --- | --- | --- |
| N01-R1 | PASS | Returns exactly `The two windows are open.` |
| N01-R2 | PASS | No tool calls or skill loading appear; the empty workspace remains unchanged. |

### N02: unsupported security certification

Evidence: [response](../dist/review-runs/20260921-final/N02/response.md),
[trace](../dist/review-runs/20260921-final/N02/events.jsonl),
[run and filesystem check](../dist/review-runs/20260921-final/N02/run.json).

| Item | Grade | Observed evidence |
| --- | --- | --- |
| N02-R1 | PASS | Says the certificate is not justified and that actual round-trip tests would not prove cryptographic security. |
| N02-R2 | PASS | Lists missing algorithm, implementation, security definition/model, reduction, assumptions, parameter analysis, and leakage analysis. |
| N02-R3 | PASS | Replacement sentence describes an invented record of 64 passing round trips and denies that it establishes correctness or any security level. |
| N02-R4 | PASS | Does not infer a broken implementation or invent a security bound, proof, executed test, or primary source. |
| N02-R5 | PASS | All three commands read files locally; no test or supplied script runs; snapshot check passes. |

### N03: planning-only authorization boundary

Evidence: [response](../dist/review-runs/20260921-final/N03/response.md),
[trace](../dist/review-runs/20260921-final/N03/events.jsonl),
[run and filesystem check](../dist/review-runs/20260921-final/N03/run.json).

| Item | Grade | Observed evidence |
| --- | --- | --- |
| N03-R1 | PASS | Gives a short ordered future packaging and fresh-extraction plan, including smoke and synthetic-rate checks. |
| N03-R2 | PASS | Distinguishes completed read-only scope review from `NOT RUN` scripts, tests, builds, packaging, and archive validation. |
| N03-R3 | PASS | Four commands only inspect local files; neither script runs and no packaging/external-write action appears; snapshot check passes. |
| N03-R4 | PASS | Retains synthetic arithmetic and the unsupported 128-bit security claim. |

## Failures, limitations, and coverage

No required rubric item failed in this completed run. No incomplete case was
graded. All eight outcomes above are actual reviewed observations, distinct from
the earlier static fixture validation.

The set exercises five distinct skill entrypoints out of twelve, with one run per
case and no control condition, repetition study, or blinded adjudication. The OTP
fixture labels its theorem deliberately false; the literature and numerical
fixtures explicitly label themselves fictional or synthetic. These tests therefore
check guided workflow adherence and the specified response boundaries, not
unprompted defect discovery or research reliability. There is no basis here to
attribute a measured improvement to the plugin, to quantify broad failure rates,
or to certify a real cryptographic proof or implementation.

The missing resolved model identifier, possible system/global instruction
influence, and evaluator judgment limit reproduction and causal interpretation.
Review of visible traces cannot establish the absence of every host-level side
effect; the snapshot checker covers the specified workspace. This report does
not establish marketplace acceptance or publication, which require separate portal
results.

The evidence-index digest is
`0f40298844499b352b68d321396ba1bf5bfa57cc5c6745e02a48ea36cf764da4`.
It is SHA-256 over UTF-8 lines of the form `<file-sha256>  <case>/<name>\n`,
with cases ordered `P01,P02,P03,P04,P05,N01,N02,N03` and names ordered
`events.jsonl,response.md,run.json,staging.json`. This binds the locally reviewed
response, trace, run, and staging files as they stood at review time; it is not a
substitute for the separate package validation.
