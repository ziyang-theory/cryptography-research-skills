# Claims and reviewer commands

## Claim map

For each selected claim, record only useful fields:

| Field | Purpose |
| --- | --- |
| Stable claim/experiment ID and paper label | Resolve the correct version without relying on printed numbering |
| Evidence type | Measurement, derivation, cited result, functional check, or open obligation |
| Component/configuration | Variant, parameters, workload and supplied setup |
| Command and prerequisites | Produce the evidence from the extracted package |
| Output and analysis | Identify raw results, parser/aggregation and displayed metric |
| Acceptance rule | Exact correctness or a justified performance interpretation |
| Exclusions/status | Omitted costs, ideal resources, platform limits and validation scope |

Use deterministic acceptance for correctness and logical counts where appropriate. Performance varies with hardware and noise; do not invent a universal percentage tolerance. A cited result may have a source/derivation route instead of a claimed local reproduction.

## Reviewer progression

Start a short README with purpose, requirements, quick build and the focused correctness example. Then give a few commands for the accompanying paper's central experiments, with expected output and meaningful time/memory guidance. Put full table coverage, optional comparisons, large batches and dependency-heavy baselines in the experiment guide. Split expensive profiles and external-dependency setup when that makes progress understandable.

A broad developer test suite can remain available without being the first command. Do not hide checks required to interpret the headline experiment. Keep researcher-facing provenance detailed enough to reproduce results while making terminal output concise.

Analysis should operate on newly generated evidence unless the release explicitly includes a historical reanalysis workflow. For multi-part commands, state whether outputs merge automatically and validate compatibility before combining them. A code path present in source, a completed correctness test, a timing run and a published result are different statuses.
