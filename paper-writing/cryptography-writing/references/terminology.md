# Cryptography terminology

Use this reference when a word changes the mathematical meaning or an unfamiliar term needs checking. Follow the current manuscript's definitions and notation first, then the cited construction's usage, then established literature. Do not normalize a source-defined term into a different guarantee.

## Name the object and role

An algorithm, scheme, protocol, functionality, construction, compiler, instantiation, and executable implementation have different roles. In particular, a functionality's input/output, leakage, scheduling, and abort interface may be split between the functionality and its surrounding execution model. An implementation realizing specified behavior is not automatically a protocol securely realizing that functionality.

Keep party, adversary, simulator, distinguisher, reduction, extractor, prover, and verifier interfaces distinct. A transcript records interaction; a party's view generally also contains its input, coins, and retained local state.

Use claim verbs according to the supported result:

- A protocol **realizes**, **securely implements**, **securely computes**, or **emulates** the object named by its governing definition.
- A construction **satisfies** a definition or **achieves** a property under stated premises; a concrete choice **instantiates** an abstraction.
- A reduction **establishes** an implication by turning a successful adversary into an algorithm for the specified underlying problem.
- An incomplete argument **sketches**, **proposes**, **assumes**, or **conjectures** its unresolved part rather than proving it.

## Prefer the actual quantity

Avoid generic metaphors when a precise description is available:

| Generic label | Name the intended meaning |
| --- | --- |
| loss | Statistical distance, soundness error, failure probability, or reduction loss |
| resource | Ideal functionality, primitive, setup, oracle, correlation, or computational bound |
| ledger | Claims and supporting sources, cost calculation, or hybrid-transition summary |
| boundary | Theorem scope, threshold, protocol phase, or included and excluded costs |
| bridge | Reduction, implication, composition theorem, transformation, or explanatory connection |

These are alternatives by meaning, not interchangeable synonyms or banned words. Retain exact titles, quotations, identifiers, and formally defined usage, including reduction loss or entropy loss.

## Resolve a technical ambiguity

Do not silently turn success probability into advantage, fixed error into asymptotic negligibility, a uniform marginal into a private joint view, correctness into security, or an ideal-model theorem into concrete security. Inspect the governing definition before changing proof/argument, setup/preprocessing, selective abort, adaptive, unconditional, fully black-box, or succinct.

Use [security claims](security-claims.md), [secure computation](secure-computation.md), [proof systems and oracles](proof-systems-and-oracles.md), or [constructions and costs](constructions-and-costs.md) for the particular ambiguity. An informal phrase can remain useful when tied to the exact definition; making it sound more formal is not a reason to strengthen it.
