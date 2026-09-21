# Synthetic release-planning fixture

All files are toy review inputs. No real benchmark or historical experiment is
represented. The requested output is a plan; no package has been built or tested.

## Selected claims

- C1: The XOR encrypt/decrypt functions recover the original 3-bit message for
  every 3-bit key/message pair. `smoke.py` is a proposed deterministic check.
- C2: The supplied synthetic observation records 1,000 operations in 0.020 seconds.
  `summarize.py` derives its rate. It does not run the toy protocol or measure time.
- C3: The implementation offers 128-bit cryptographic security. No security
  experiment, proof, reduction, implementation correspondence, or leakage analysis
  is supplied for this claim. Treat it as unsupported.

## Scope and requirements

Python 3 standard library is sufficient for the two supplied scripts. There are
no dependencies to download. No source revision, real hardware record, or real
measurement provenance is supplied. A future package should carry these synthetic
qualifications. No venue compliance or anonymous-release claim is requested.
