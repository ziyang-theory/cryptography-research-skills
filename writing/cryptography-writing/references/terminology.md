# Cryptography terminology

Use this reference for preferred wording when drafting or revising cryptographic prose, and when an unfamiliar term or generic metaphor obscures an object. Follow the current manuscript's definitions and notation first, then the cited construction's usage, then established literature. The wording defaults below are editorial preferences, not claims that other terms are absent from the literature. Do not normalize a source-defined term into a different guarantee.

## Name the object and role

Honor recorded author corrections before suggesting fresh wording. If the
author rejects a term as uncommon or asks for a replacement, identify the
object and use the accepted wording in the same scope. Prefer an existing
defined term over adding a definition solely to justify a redundant label.
Preserve mathematical qualifiers and distinguish view from transcript,
correlations from messages, and masked values from unmasked values.

When asked to refresh project guidance or memory, record the original term,
accepted alternative or meaning, scope, and conversation provenance. Resolve
later corrections and reverts before retaining an earlier choice. Keep
manuscript-specific choices in project guidance unless the author explicitly
asks to generalize them. Extract reusable wording defaults by meaning;
do not carry over particular variable names, theorem organization, or
protocol parameters. A section-local preference does not become a universal
word ban. An author's objection is a writing
preference, not evidence that no cryptography paper uses the term.

An algorithm, scheme, protocol, functionality, construction, compiler, instantiation, and executable implementation have different roles. In particular, a functionality's input/output, leakage, scheduling, and abort interface may be split between the functionality and its surrounding execution model. An implementation realizing specified behavior is not automatically a protocol securely realizing that functionality.

Keep party, adversary, simulator, distinguisher, reduction, extractor, prover, and verifier interfaces distinct. A transcript records interaction; a party's view generally also contains its input, coins, and retained local state.

Use claim verbs according to the supported result:

- A protocol **realizes**, **securely implements**, **securely computes**, or **emulates** the object named by its governing definition.
- A construction **satisfies** a definition or **achieves** a property under stated premises; a concrete choice **instantiates** an abstraction.
- A reduction **establishes** an implication by turning a successful adversary into an algorithm for the specified underlying problem.
- An incomplete argument **sketches**, **proposes**, **assumes**, or **conjectures** its unresolved part rather than proving it.

## Preferred wording in cryptographic prose

Apply these defaults to the object actually meant. Choose a replacement
only when it preserves the definition and claim; do not perform a global
synonym substitution.

| Avoid or reconsider | Prefer, with the relevant qualification |
| --- | --- |
| loss | Statistical distance, soundness error, failure probability, or reduction loss |
| resource | Ideal functionality, primitive, setup, oracle, correlation, or computational bound |
| ledger | Claims and supporting sources, cost calculation, or hybrid-transition summary |
| boundary | Theorem scope, threshold, protocol phase, or included and excluded costs |
| bridge | Reduction, implication, composition theorem, transformation, or explanatory connection |
| endpoint(s) | Named parties or roles, such as sender/receiver or prover/verifier; in a hybrid argument, the initial and final experiments or distributions |
| layer | The particular protocol phase, subprotocol, primitive, or assumption; for exposition or comparisons, name the section, claim, or comparison being discussed |
| generic interface | The actual inputs, outputs, leakage, party roles, or scheduling rule. Retain “interface” for a specified functionality or primitive interface. |
| generic publish | Send, broadcast, reveal, or reconstruct, according to the protocol's actual operation and recipients. Public availability alone does not imply a broadcast. |
| pad, garbling pad | The PRF output, OT message, mask, or rerandomization string actually used. Preserve “one-time pad” and formally defined uses. |
| coalition, when it means the corrupted set | Corrupted parties or set of corrupted parties. A coalition in a game-theoretic or other model need not consist of corrupted parties. |
| scalar correlations | The actual correlation and domain: for example, random bit-OT correlations when that is the supplied relation. Other scalar-valued correlations do not become OT by renaming. |
| vague scalar modifiers, such as scalar primitive calls | The bit, field element, message, product, or named functionality and its calls. Retain meaningful scalar/vector distinctions. |
| OT state, when only supplied correlations are meant | OT correlations, a party's shares of the correlations, or the sender's and receiver's named values. Retain “state” for complete retained state, including messages, coins, and derived values. |
| vague contribution | Define the component or summand, then use its name or symbol. An XOR of PRF outputs is not a single PRF output; a garbled-row share is not a complete garbled row. |
| advantage bound without naming the advantage | Distinguishing advantage, forging advantage, or the quantity defined by the experiment. When bounding it, say “bound on the distinguishing advantage,” for example. Preserve the quantitative claim. |
| primary input, when no contrast requires primary | Input or input wire. Keep a defined distinction from intermediate inputs or values. |
| normalization for representational conventions | Circuit representation or the actual conventions adopted. Retain “normalization” for a genuine mathematical transformation and account for its effects. |
| operands in explanatory prose | The named quantities or inputs being multiplied, when clearer. Keep “operands” where it precisely distinguishes argument roles. |
| first-round prefix or unexplained prefix | First-round view when it includes that view's state and messages; transcript prefix when only the indicated messages are meant. Specify the actual contents. |
| cutoff for a bounded sampler | The number of trials and the event that causes abort or failure, together with the failure output and probability when relevant. |
| reconstructed object | The reconstructed secret, value, or garbled circuit. Name the object. |
| aggregate row or unexplained required aggregate | The garbled row or other reconstructed value, and the equation relating it to the shares. Preserve meaningful uses such as aggregate shares or sums. |
| sample the marginal without explaining the sampling | Name the sampled variables, their law, the conditioning, and which variables are retained. State independence only when justified; retain “marginal distribution” when the mathematical distinction matters. |
| experiment used only to label a step in a hybrid sequence | Hybrid or hybrid distribution. Retain “experiment” for the actual security experiment, game, or executable procedure. |
| wrapper, stack, pipeline | The particular construction, composition, sequence of subprotocols, or implementation procedure |

Choose the term from the object's role in the construction or proof, not by mechanical substitution. In a hybrid argument, name the experiments or distributions being compared rather than “endpoints”; describe the advantage in distinguishing the initial and final distributions rather than an “endpoint gap.” If the intended object is unclear, resolve it from the definitions before choosing a more formal-sounding term.

These are alternatives by meaning, not interchangeable synonyms or banned words. Retain exact titles, quotations, identifiers, and formally defined usage, including reduction loss or entropy loss. Precise uses such as a circuit layer, a network or API endpoint, and implementation pipelining can remain when they refer to those actual objects. Do not infer a round, a security property, or a composition theorem from a replacement label.

Prefer an existing mathematical description, such as “linear combination,”
to a new label for the same expression. Preserve when each value becomes
available, who knows it, and how it is computed: “locally computable” alone
does not mean “available before the first round.” A public coefficient does
not make its product with a secret value public.

State the security model positively and precisely. Mention other models
when needed to delimit the claim or answer a comparison, rather than adding
stock disclaimers about guarantees outside the paper's subject. Name the
specific overhead or parameter dependence that improves; wording alone
must not strengthen a priority or efficiency claim.

## Resolve a technical ambiguity

Do not silently turn success probability into advantage, fixed error into asymptotic negligibility, a uniform marginal into a private joint view, correctness into security, or an ideal-model theorem into concrete security. Inspect the governing definition before changing proof/argument, setup/preprocessing, selective abort, adaptive, unconditional, fully black-box, or succinct.

Use [security claims](security-claims.md), [secure computation](secure-computation.md), [proof systems and oracles](proof-systems-and-oracles.md), or [constructions and costs](constructions-and-costs.md) for the particular ambiguity. An informal phrase can remain useful when tied to the exact definition; making it sound more formal is not a reason to strengthen it.
