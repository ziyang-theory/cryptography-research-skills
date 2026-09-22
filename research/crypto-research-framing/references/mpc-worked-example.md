# MPC interface exercises

The first exercise is adapted from §6 of the user-supplied *Learning from Amit Sahai: A Cryptography Research Distillate* (research cutoff September 20, 2026). It is not an attributed construction or a solved protocol. Use the relevant exercise to isolate a preprocessing interface; their targets and corruption models are separate.

## Target and unknowns

Suppose the researcher seeks lower communication for a two-round maliciously secure two-party protocol with circuit-independent preprocessing. Before choosing a construction, resolve the allowed corruption and composition, abort or delivery, output recipients, speaking order, when the circuit and inputs are known, and the exact preprocessing distribution. An ideal source of correlations is distinct from a maliciously secure distributed protocol generating them.

Let `kappa` and `sigma` denote the computational and statistical security parameters for this exercise. Define disjoint phases and, if the task concerns total communication, use an accounting convention such as

`C_total = C_setup + C_circuit-dependent preprocessing + C_online`.

Count transmitted bits with an explicit aggregation convention, including all traffic in exactly one phase. For amortization over `B` executions, separate one-time setup from per-execution material; the setup cost per execution is `C_setup/B` only when that reuse and batch size are justified. No preprocessing is free because it is circuit-independent, and fresh correlations are not reusable merely because their distribution has not changed.

## Isolate what the expensive step supplies

Describe the component by party holdings and a joint law, not just by naming a primitive. Which values can a malicious participant choose? Which are public or later revealed? What does the simulator know when it must produce each message? Which consistency relation must hold for the next stage, and what happens on malformed input?

Then consider an applicable change: express a relation directly over its natural field; use internal executions as checkable objects; or expose a value to simplify a computation. Each is a candidate. The last changes the target unless the extra disclosure can be simulated under the original permitted leakage. Reduced bit encoding costs can also be offset by conversion or consistency checks.

## A small calculation can rule out a candidate

Suppose a component generates two field elements `(X,Y)` over a finite field `F`. The original joint law is `(R,R)` for uniform `R` in `F`; a candidate samples independent uniform `(R,S)` instead. Each coordinate has the same marginal distribution. Nevertheless, a party observing both coordinates can test equality:

`Pr[X=Y | original] = 1`, while `Pr[X=Y | candidate] = 1/|F|`.

The difference in acceptance probabilities is `1 - 1/|F|`. This refutes preservation of the joint law and any justification based solely on matching marginals. If no permitted observer ever sees both coordinates, this calculation is not itself an attack on the whole protocol; identify the actual observer and any later check consuming the relation.

## State the next lemma and its missing premise

A useful candidate statement might be: for every adversary allowed by the fixed model, replacing component A by component B preserves the specified joint view and state within a declared statistical-distance or computational-distinguishing bound, while producing the interface required by each later consistency check. Name the view, conditioning, simulator interface, and bound before attempting its proof. This sentence is a statement template, not a proved lemma.

For `m` replacements, define the consecutive experiments and justify every transition with its retained state and adaptive choices. Only then accumulate the applicable bounds; a fresh-copy calculation alone does not cover correlated reuse. End with the exact missing claim or the concrete counterexample, and connect it to the communication term it would improve. Passing a one-gate check is not a proof of the full compiler.

## Double sharing: a complete-view masking argument

This separate, restricted exercise adapts §5 of *Learning from Ivan Damgård: A Cryptography Research Distillate* (research cutoff September 22, 2026). It proves a one-use equality of local views with ideal preprocessing, not a two-round MPC construction or a full simulation theorem.

**Source context.** Ivan Damgård and Jesper Buus Nielsen, *Scalable and Unconditionally Secure Multiparty Computation*, CRYPTO 2007: [§3.1/Fig. 2](https://link.springer.com/content/pdf/10.1007/978-3-540-74143-5_32.pdf#page=6) generates double sharings, §3.3/Fig. 4 uses them in triple generation, and §3.4/Figs. 5–6 uses triples for circuit evaluation (printed pp. 577–580). Those passages of the 19-page proceedings PDF were checked on September 22, 2026; its full security proof was not audited. The following fixed-input coupling is a separate pedagogical argument, not a quotation or reconstruction of the paper's full theorem.

### Resource and operation

Work over `F_q` with `n >= 2` distinct nonzero evaluation points `zeta_i`, `t >= 0`, and `n > 2t`. Fix a passive corruption set `T` with `|T| <= t`. Channels are private; even a corrupted collector follows the protocol. Fix degree-at-most-`t` input polynomials `f,g`, with secrets `f(0),g(0)`. Party `i` holds their evaluations at `zeta_i`.

An ideal resource, independent of the inputs, samples a uniform pair `(p,P)` from

`Omega = {(p,P): deg p <= t, deg P <= 2t, p(0)=P(0)}`.

Equivalently, sample the common constant `r` uniformly and all nonconstant coefficients independently uniformly. Party `i` receives `p(zeta_i),P(zeta_i)`. No generator seeds, coefficients, or correlated auxiliary state are exposed beyond these shares.

Each party sends `u_i = f(zeta_i)g(zeta_i)+P(zeta_i)` to the collector. The collector reconstructs `h=fg+P`, of degree at most `2t`, and sends `D=h(0)` to all parties. Each computes `z_i=D-p(zeta_i)`. These are degree-at-most-`t` shares of `f(0)g(0)`, since `z(X)=D-p(X)`. This proves passive correctness. A corrupted collector sees all of `h`; uniformity of `D` alone does not prove privacy.

### Exact local comparison

For any fixed alternative `f',g'` of degree at most `t` agreeing with `f,g` at all points in `T`, compare the joint views consisting of:

- corrupted input and preprocessing shares;
- the entire polynomial `h` and announcement `D`;
- corrupted output shares `z_i`.

The actual collection messages are evaluations of `h`, so this view covers a corrupted collector as well as the other corrupted parties. It excludes honest output shares and later reconstruction of the product. The probability space is precisely the independent ideal preprocessing above.

Set `Delta=fg-f'g'` and

`L_T(X) = product_{i in T}(X-zeta_i) / product_{i in T}(-zeta_i)`.

The empty product is one. Nonzero evaluation points make the denominator invertible. Thus `deg L_T <= t`, `L_T(0)=1`, and `L_T(zeta_i)=0` for `i in T`. Couple the second execution to the first by

`p' = p + Delta(0)L_T`, and `P' = P + Delta`.

Both degree bounds hold, and the two constants still coincide. Since `Delta(zeta_i)=0` on `T`, every corrupted preprocessing share is unchanged. Moreover `f'g'+P'=fg+P=h`; hence `D` and every corrupted output share are unchanged too. Translation by these fixed polynomials is a bijection of `Omega`, whose inverse subtracts them. It preserves the uniform preprocessing law exactly. Consequently the stated joint views have identical distributions, with zero statistical distance and no computational assumption or reduction loss.

This is a distributional coupling, not an online simulator that is granted the honest polynomials. It establishes only the quantified local comparison. A full real/ideal proof must supply its simulator and match the required outputs, auxiliary state, scheduling, and composition definition.

### What changes would invalidate reuse?

A concrete generator must justify the same joint resource interface, including exposed state. Reusing the mask pair across two products exposes their difference through the two announcements. Adaptive corruption or a malicious collector needs additional arguments. Merely preserving the sharing equations establishes none of those extensions.

For this operation, collection and private redistribution transmit `2(n-1)` field elements. If redistribution uses an ideal broadcast whose payload is counted once, the count is `(n-1)+1=n` elements. These are alternative channel/accounting conventions, excluding preprocessing. Both have two causally sequential message steps and linear collector traffic; repeated dependent operations do not give a two-round circuit evaluation.
