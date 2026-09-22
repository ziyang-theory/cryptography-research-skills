# Batching and release order

Use the implicated example to test an algebraic or scheduling inference. These are self-contained toy experiments, not analyses or attacks on SPDZ, SPDZ2k, or another named protocol. A failed inference need not refute the surrounding theorem.

Provenance: adapted from the user-supplied *Learning from Ivan Damgård: A Cryptography Research Distillate* (`ivan_damgard_research_distillate.md`, research cutoff 2026-09-22), §3, Move 6, and §§4.1–4.3. The conditional formulations and release criterion below state their own premises.

## Local products need an actual multiplication interface

For additive shares over a field, `x=x_0+x_1` and `y=y_0+y_1`, the locally available sum `x_0 y_0+x_1 y_1` omits `x_0 y_1+x_1 y_0`. For example, `(x_0,x_1)=(1,0)` and `(y_0,y_1)=(0,1)` give local sum `0` and product `1`. Privacy and linear reconstruction do not supply missing cross terms. Multiplying degree-at-most-`t` sharing polynomials yields degree at most `2t`; this does not by itself yield a fresh degree-`t` sharing. Identify the locally available term vector and consumer's required sharing distribution before claiming local multiplication.

## Positive case: independent field coefficients

Let `H` denote the state on which the argument conditions, including the fixed residual vector `delta in F_q^B`. Suppose, for every supported `H=h`, the challenge vector `R=(R_1,...,R_B)` is conditionally uniform on `F_q^B`. Accept exactly when `sum_j R_j delta_j=0`.

For every `h` with `delta(h) != 0`, choose a nonzero coordinate `delta_k`. After additionally fixing all `R_j` for `j != k`, exactly one value of the still-uniform `R_k` accepts. Thus

`Pr[accept | H=h] = 1/q`.

For zero residuals acceptance is certain. Prove the conditional law from the actual challenge-generation interface, including prior checks and reused state; marginal uniformity alone does not imply this premise. Including residuals in the conditioning must preserve the claimed law even when residuals depend on hidden state.

## Powers of one challenge are a different experiment

If instead `R_j=r^j`, with `r` conditionally uniform on `F_q` after residuals are fixed, acceptance tests the nonzero formal polynomial `P(X)=sum_{j=1}^B delta_j X^j`. For degree `d`, the root bound gives at most `min(1,d/q)`, not generally `1/q`. Over `F_5`, `P(X)=X+X^2` accepts at `0` and `4`, with probability `2/5`. For degree at least `q` the bound can be vacuous: `X^q-X` vanishes everywhere on `F_q`. Preserve the actual exponent range and sampling domain, including whether zero is excluded.

## Residuals chosen after the challenge

For revealed `(r_1,r_2) != (0,0)`, choosing `(delta_1,delta_2)=(r_2,-r_1)` gives a nonzero residual that always passes. At `(0,0)`, choose `(1,0)`. This defeats the toy check with probability one. The failed obligation is fixation of residuals with the required conditional challenge distribution. An actual attack additionally requires the protocol to permit these residuals; algebra alone does not grant that control.

## Ring annihilators change the bound

For `k >= 2`, in `Z/(2^k)`, take `delta=2^(k-1) != 0` and uniform `r`. Then `r delta=0` exactly when `r` is even, with probability `1/2`, not `2^(-k)`. More generally, a single fixed nonzero residual in a finite commutative ring `A` accepts with probability `|Ann(delta)|/|A|`, where `Ann(delta)={a in A: a delta=0}`. A field proof's inversion step does not transfer to a nonunit. This calculation says nothing about a specialized ring authentication construction.

## Delayed checking needs a release argument

Separate internal use of unchecked values from externally visible messages, outputs, or state transitions. To derive a release bound from the toy checks, establish both:

- Every forbidden release implies an **earlier** acceptance of a nonzero residual in some check.
- At each of at most `m` checks, conditional on every supported state reaching that check with its residual fixed, the false-acceptance probability is at most `epsilon_i`.

The union bound then gives `Pr[forbidden release] <= sum_i epsilon_i`, without independence between checks. The first premise is a protocol invariant, not a consequence of the cancellation calculation. Define which release is forbidden by the target experiment; an adversary receiving its prescribed output before honest parties may be allowed.

A later rejection cannot retract an earlier disclosure. For a toy functionality revealing nothing about secret bit `s`, a protocol that first sends `s` and then always rejects leaks completely, despite zero false acceptances. Even when integrity is captured by residuals, privacy needs a separate joint-view argument for every pre-check disclosure. Reusing a key or challenge requires the conditional bound after earlier observations; multiplying single-check bounds without such an argument is unjustified.
