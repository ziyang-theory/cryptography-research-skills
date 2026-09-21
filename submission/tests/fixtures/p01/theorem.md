# Synthetic OTP reuse example

This example was written for plugin review. It is not a claim from a published paper.

## Construction and experiment

Let n be any integer at least 1. Sample K uniformly from {0,1}^n once. To encrypt
a pair (M1, M2), use the same K for both ciphertexts:
C1 = K XOR M1 and C2 = K XOR M2. Messages are fixed independently of K.
The adversary sees the complete ordered pair (C1, C2); K is not revealed.
There are no oracles, corruption operations, aborts, or other setup resources.

Before a uniformly random challenge bit b is sampled, an adversary chooses two
message pairs X0 and X1 in ({0,1}^n)^2. The challenger encrypts Xb using the
construction above and returns both ciphertexts. The adversary outputs b'.
Perfect pair privacy means Pr[b' = b] = 1/2 for every adversary in this experiment.
For a fixed distinguisher D, the distributional distinguishing gap is
|Pr[D(EncPair(K, X0)) = 1] - Pr[D(EncPair(K, X1)) = 1]|.

## Theorem T (deliberately false)

The construction has perfect pair privacy for every n >= 1.

## Supplied proof

For each fixed message Mi, Ci = K XOR Mi is uniform on {0,1}^n. Therefore the
joint pair (C1, C2) is uniform on ({0,1}^n)^2 and is independent of (M1, M2).
Consequently every adversary guesses b with probability exactly 1/2.
