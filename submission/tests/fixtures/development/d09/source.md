# Fixed source claims for a synthetic editing exercise

The claims below are invented manuscript facts for this editing exercise. Treat them as the author's fixed source claims; the task is to edit prose, not to prove a protocol secure.

The result concerns one execution of a protocol among n parties against a static semi-honest adversary corrupting at most t parties, with t < n/2. It assumes ideal preprocessing from F_corr. The simulator receives the corrupted parties' inputs and outputs. The statistical distance between the real and simulated joint views is at most 2^(-kappa).

The online phase uses two broadcast rounds. This round count excludes preprocessing. The manuscript makes no claim about malicious adversaries, adaptive corruption, reuse of preprocessing, or a concrete implementation of F_corr.
