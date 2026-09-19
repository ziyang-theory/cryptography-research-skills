# Cryptography terminology and claim discipline

Choose terminology in this order:

1. definitions, notation, macros, and role names in the current manuscript;
2. terminology in the cited paper for the construction or proof technique;
3. established usage in authoritative cryptography papers and textbooks.

Prefer a term of art only when it denotes the formal notion actually used. Do not introduce an undefined synonym, modernize construction-specific language without evidence, or silently import a stronger security notion. If usage is uncertain, preserve the source and flag the choice rather than guessing.

## Prefer precise cryptographic language

When drafting or revising prose, try to avoid “loss,” “resource,” “ledger,” “boundary,” and “bridge” as generic labels or metaphors. Use standard cryptographic terminology when its formal meaning fits; otherwise describe the object, quantity, or relationship in plain language. Apply this preference to headings, tables, captions, proof explanations, and reports as well as manuscript paragraphs.

Choose the wording from the actual meaning, not by mechanical substitution:

| Vague wording | More precise wording, when applicable |
| --- | --- |
| loss | distinguishing-advantage bound, statistical distance, soundness error, failure probability, or reduction loss; identify the quantity being bounded |
| resource | ideal functionality, primitive, setup assumption, oracle access, correlated randomness, or the specific time, memory, communication, or query bound |
| ledger | table of claims and supporting sources, results table, communication calculation, or summary of hybrid transitions |
| boundary | scope of the theorem, corruption threshold, start or end of a protocol phase, included and excluded costs, or the precise condition under discussion |
| bridge | reduction, implication, composition theorem, transformation, or a sentence explaining how one construction yields another |

These alternatives are not interchangeable. For example, an ideal functionality is not a computational assumption, statistical distance is not an adversary's success probability, and an explanatory connection is not necessarily a reduction. Do not invent a theorem or alter a security claim to justify a preferred word.

Keep a word when it is technically necessary or formally defined in the governing source, such as “reduction loss,” “entropy loss,” or a resource in a framework that defines resources. Preserve exact quotations, titles, identifiers, notation, and source-defined names. In new prose, prefer the specific meaning even when a broader word would be defensible. This is a writing preference, not a blanket word ban or permission to change the construction, assumptions, guarantees, or unrelated text.

## Name the mathematical object precisely

Preserve local definitions, but use these conventional roles when they fit:

- an **algorithm** is a computational procedure;
- a **scheme** is usually a specified collection of algorithms with common syntax and correctness or security requirements;
- a **protocol** specifies an interaction among parties;
- a **functionality** specifies a task, commonly through input/output behavior; a richer ideal-resource functionality may also specify leakage, abort, delivery, state, and scheduling interfaces, while some formalisms place those interfaces in the surrounding ideal execution;
- a **construction** builds an object from stated primitives or resources;
- a **compiler** transforms objects or protocols while preserving or changing properties according to a stated theorem;
- an **instantiation** replaces an abstraction with a concrete primitive or parameter choice;
- an **implementation** is an executable realization of specified behavior.

Do not conflate the interfaces of a party, adversary, simulator, distinguisher, reduction, extractor, prover, or verifier. One algorithm may occupy multiple roles only when the governing definition identifies them. A transcript records exchanged messages; a party's view generally includes additional local state such as its input, random tape, and received messages.

## State only the supported claim

A security claim may need to identify the security parameter, execution or experiment, adversary class and resources, corruption pattern, setup or hybrid model, computational assumptions, guarantee, comparison relation or success bound, leakage profile, and abort or output-delivery qualification. State only components established by the surrounding definition or proof.

Use conventional formulations only under the stated guardrails:

| Informal wording | Conventional wording, when justified | Guardrail |
| --- | --- | --- |
| efficient attacker | probabilistic polynomial-time (PPT) adversary | Use QPT for a quantum adversary; for concrete security, state the actual resource bound. |
| very unlikely | except with negligible probability in the security parameter | A fixed numerical error is not itself a negligible function. |
| the two cases look the same | the indexed distributions are identically distributed, statistically close, or computationally indistinguishable | Match the exact relation proved. |
| the attacker succeeds with probability | the adversary wins the named experiment with the stated probability or advantage | State the success event and baseline when advantage is used. |
| change the game one step at a time | proceed via a sequence of hybrids | Identify every transition and the resulting bound on distinguishing advantage. Do not confuse this with a hybrid model. |
| use an attacker to break the assumption | construct a reduction that uses the adversary to solve the underlying problem or distinguish the underlying distributions | State direction, running time, access, and reduction loss. |
| the protocol is secure | the protocol realizes or securely computes the stated functionality under the named definition and model | Do not hide corruption, setup, composition, leakage, or output qualifications. |
| learns nothing | the named random variables satisfy the definition's exact privacy or leakage condition | This may use simulation, independence, conditional distributions, statistical distance, a semantic-security experiment, or another formal condition; do not assume one. |
| trusted preprocessing | setup assumption, ideal functionality, preprocessing functionality, or correlated preprocessing | These are not synonyms; use the resource actually defined. |
| a party stops | abort under the governing execution or functionality | Reserve selective abort and other qualified abort terms for a definition or cited usage that explicitly supports them. |
| uses `X` as a black box | the construction invokes the stated interface of `X`, or the reduction uses the adversary or primitive as a black box | Construction black-boxness and reduction black-boxness are different axes; “fully black-box” needs the source's definition. |
| unconditionally secure | the named property holds information-theoretically—perfectly or statistically, as defined—against the stated adversary class, relative to the named network, setup, oracle, or hybrid resources | Do not hide query or resource bounds, ideal-resource assumptions, or statistical error. |
| two-round protocol | an `r = 2` protocol with the stated speakers, recipients, topology, and preprocessing boundary | NISC, two-sided NISC, simultaneous exchange, broadcast, and client/server flows differ. |
| linear or constant-rate communication | the stated total or amortized cost in the named unit as a function of the named parameters | Include the aggregation rule, denominator, and additive or depth-dependent terms. |

Use claim verbs precisely:

- A protocol **realizes** or **securely implements** an ideal functionality, **securely computes** a functionality, or **emulates** an ideal process or system according to the governing definition.
- A construction **satisfies** a definition or **achieves** a property under stated assumptions.
- An executable artifact **implements** specified behavior or a protocol path; this is distinct from a definition's formal use of “securely implements.”
- A concrete primitive or parameter choice **instantiates** an abstraction.
- A reduction **establishes** a claim by transforming a successful adversary into an algorithm for the stated problem.
- Complete reasoning may **prove** or **establish** a claim; incomplete material should **sketch**, **propose**, **assume**, or **conjecture** it.

Do not silently conflate a hash function with a random oracle; semi-honest, covert, and malicious corruption; corruption, leakage, knowledge, learning, and output; or a hybrid-model theorem with a concrete instantiation. Preserve exact quantifiers, advantage bounds, reduction loss, oracle access, composability scope, and classical-versus-quantum assumptions.

Do not infer a missing assumption, definition, citation, theorem, or proof step. Treat prior-art and theorem attributions as unverified until checked against the cited primary source or an authoritative reference.
