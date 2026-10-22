# Synthetic one-use observation lemma

This is an invented finite-distribution exercise. It is not a theorem about a deployed protocol, multiple sessions, adaptive corruption, or an implementation.

## Experiment

Let `q >= 2` be prime and work in `F_q`. Let `(X,Z)` have any joint distribution on `F_q` and a finite auxiliary-information space. Sample `R` and `S` independently and uniformly from `F_q`, independently of `(X,Z)`.

The passive observer receives the auxiliary information `Z` and the triple

`V_X = (R, X + S, R + X + S)`.

The observer receives no other state or coins. Define `Sim(q)` to sample independent uniform `U,V` in `F_q`, independently of `(X,Z)`, and return `(U,V,U+V)`. The simulator receives `q` but neither `X` nor `Z`. All additions are field additions. There is no abort, oracle, or computational assumption in this experiment.

## Claim

For every such `q` and distribution of `(X,Z)`, the joint distributions `(Z,V_X)` and `(Z,Sim(q))` are identical. Consequently their statistical distance and every observer's absolute difference of acceptance probabilities are zero, even for an unbounded observer.

## Supplied proof

Fix `x,z` with `Pr[X=x,Z=z] > 0` and any `a,b,c` in `F_q`. If `c != a+b`, the triple `(a,b,c)` has probability zero in both experiments. If `c = a+b`, then `V_x=(a,b,c)` exactly when `R=a` and `S=b-x`. These are two independent uniform choices even after conditioning on `X=x,Z=z`, so this event has probability `q^(-2)`. The simulator returns that triple exactly when `U=a,V=b`, also with probability `q^(-2)`. Thus the conditional laws agree for every supported `x,z`. Multiplying by `Pr[X=x,Z=z]` and summing over `x` gives equality jointly with `Z`. No efficiency restriction or computational assumption is used.
