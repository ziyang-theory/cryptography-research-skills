# Worked implication: compatible inputs and one-party view simulation

This teaching argument adapts §6 of the user-supplied *Learning from Mihir Bellare: A Cryptography Research Distillate* (September 21, 2026). It is a sufficient-condition exercise, not a reconstruction of a cited 2PC theorem or a claim of novelty. Use it to see what a simpler privacy experiment must supply to a simulator.

## Fix the limited setting

Fix a classical, standalone two-party protocol with a fixed public schedule, perfect correctness, polynomial-time honest algorithms, independently sampled honest coins, and no external correlated setup or state. Alice is passively corrupted and follows the protocol. Her deterministic prescribed output is `f_A(x,y)`; permitted public leakage is `ell(x,y)`. Both functions are efficiently computable. All algorithms receive the security parameter `lambda` and the public parameters and length information needed to run in polynomial time.

Let `V_A(x,y)` contain Alice's input, coins, received messages, and output under fresh honest execution. Input samplers may efficiently generate auxiliary information `z` correlated with the inputs, but not with the subsequently sampled honest coins. The conclusion below concerns Alice's view with that auxiliary information. It does not assert malicious security, adaptive corruption security, or a composition theorem.

## Two sufficient premises

**Compatible-input indistinguishability.** For every permitted efficient sampler of valid `(x,y_0,y_1,z)` satisfying

```text
f_A(x,y_0) = f_A(x,y_1),
ell(x,y_0) = ell(x,y_1),
```

the ensembles `(x,z,V_A(x,y_0))` and `(x,z,V_A(x,y_1))` are computationally indistinguishable. Protocol coins are fresh and independent of the sampler. The sampler class must include the augmented sampler below; `z` may retain the original inputs. Merely quantifying over independent fixed inputs is not this premise. For a concrete version, specify a bound `epsilon` at the sampler and distinguisher resources actually used.

**Efficient compatible-input construction.** On each feasible `(x,o,l)`, an algorithm `I` always returns a legal `y_hat` with `f_A(x,y_hat)=o` and `ell(x,y_hat)=l`, in polynomial time in the public lengths and `lambda`. It receives neither the actual `y` nor extra secret information. Legal inputs must respect any domain restrictions of the exercise. If a proposed constructor sometimes fails, its failure probability and resulting output behavior require a separate bound; the argument below assumes no failure.

## Simulator and comparison

**Simulator.** Given only `(x,o,l)` and the public inputs, compute `y_hat <- I(x,o,l)`, run both honest parties locally on `(x,y_hat)` with fresh independent coins, and return Alice's view.

For any permitted real-input sampler of `(x,y,z)` and any permitted efficient distinguisher:

**Hyb_0:** Sample `(x,y,z)` and return `(x,z,V_A(x,y))`. This is the real-view distribution.

**Hyb_1:** Sample the same `(x,y,z)`, compute `o=f_A(x,y)`, `l=ell(x,y)`, and `y_hat <- I(x,o,l)`, then return `(x,z,V_A(x,y_hat))` with fresh honest coins. The augmented sampler that outputs `(x,y,y_hat,z)` satisfies the compatibility premise. That premise bounds this transition by its declared distinguishing bound. The endpoint is exactly the simulator's distribution given the real prescribed output and leakage, with the original `(x,z)` retained.

There is one application of the indistinguishability premise, with no hybrid-count multiplier. The augmented sampler pays for output/leakage evaluation and `I`; the simulator pays for `I` and local protocol execution. Their actual costs must fit the premise's resource bounds. This does not turn a polynomial-time statement into a concrete bound unless those bounds are supplied.

The compatible input need not be drawn from Bob's true conditional input distribution: the stated view-indistinguishability premise, including its auxiliary information and sampler coverage, is what justifies substitution. Compatibility alone does not imply privacy.

## PSI as an input-construction example

Suppose the input domain is all subsets of a specified finite universe, Alice has `A`, her prescribed output is `S=A intersect B`, and the only additional relevant leakage is Bob's size `m`. Construct `B_hat=S union D`, where `D` contains exactly `m-|S|` distinct elements outside `A`.

For feasible inputs there are enough such elements; an efficient method to find them must still be supplied. Then `A intersect B_hat=S` and `|B_hat|=m`. An authenticated database restriction, additional leakage, or another enforced validity condition may make this constructor inadmissible. No PSI protocol's view-indistinguishability premise is established by this set calculation: sending all of `B` gives a counterexample to that missing premise whenever distinct compatible sets are allowed.

For malicious participants, extracting an effective input, enforcing consistency, simulating abort, and interacting with an ideal functionality are separate obligations. Correlated setup, reuse, or later corruption can require further joint state. Keep the scoped implication and those missing extensions distinct.
