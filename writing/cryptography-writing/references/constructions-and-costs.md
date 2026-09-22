# Cryptographic constructions, resources, and cost accounting

Use this reference for construction interfaces, correlated resources, PCGs, garbling, FSS, NISC, protocol compilers, phase boundaries, rounds, communication, amortization, and performance comparisons.

## Name the abstraction and exposed interface

Keep a primitive or scheme, an ideal functionality, a protocol, a compiler, a concrete instantiation, and an implementation distinct. A construction may use:

- ideal calls to a functionality;
- the input/output interface of primitive algorithms or next-message functions;
- oracle access in a reduction;
- a primitive's description or implementation code.

These are different black-box or non-black-box interfaces. Use **fully black-box** only under the source's exact definition. Black-box access does not by itself imply practical or concrete efficiency.

State whether a resource is one-shot, bounded-use, reusable, or reactive; whether it shares state across sessions; and whether it depends on the circuit, relation, parties, identities, inputs, session, or previous transcript. Preserve whether the construction is generic, special-purpose, or mixed; these are design choices, not quality rankings.

## Name a correlation algebraically

When introducing or comparing OLE, VOLE, ROT, COT, a multiplication triple, or an authenticated correlation whose convention is not already fixed locally, state the defining equation, domain or field, scalar or vector dimensions, randomness, and the values held by each party. Sender/receiver and additive-share conventions vary across sources.

Distinguish a chosen-input functionality from a randomized correlation and identify the conversion protocol, if any. Preserve base-field, subfield, extension-field, block, batched, and vector qualifications. Do not treat ideal calls, correlated seeds, expanded correlations, and concrete transfers as the same resource or cost unit.

## Pseudorandom correlation generators

Follow the governing PCG syntax and security definition. Identify:

- how correlated seeds are sampled, generated, or distributed;
- what each local expansion algorithm outputs;
- the exact correctness or target-distribution requirement;
- the seed-and-output security experiment, assumptions, and parameter regime.

The short seed is part of a party's view. Correct expansion and pseudorandom stretch do not by themselves show that a PCG realizes an ideal correlation functionality.

Treat programmability, reverse sampleability, distributed setup, malicious setup security, leakage resilience, reuse, streaming expansion, and polynomial stretch as separate properties. “Silent,” “local,” or “non-interactive” expansion normally means no interaction after seed distribution; it does not mean no setup, no seed communication, no trusted resource, or zero total cost.

## Phase boundaries and end-to-end scope

Define phases by what they may depend on: the function or circuit, input lengths, actual inputs, party identities, session identifiers, or prior transcripts. Phase names are manuscript-local. Separate when applicable:

- setup or seed generation;
- circuit-independent or function-independent preprocessing;
- circuit-dependent or function-dependent preprocessing;
- local expansion;
- input processing;
- online evaluation.

State the security and assumptions of each phase and the composition used for the end-to-end claim. Perfect, statistical, or information-theoretic security in an ideal-resource hybrid does not imply the same end-to-end guarantee after a computational concrete instantiation. Online-only cost or security is not a total deployment claim.

State whether preprocessing is trusted, ideal, distributed, semi-honest-secure, or malicious-secure; whether it is single-use or reusable; and what accept/reject or abort feedback it exposes. One-time material such as a Beaver triple must not be silently reused.

An additive communication decomposition such as `C_total = C_setup + C_pre + C_online` requires disjoint charged traffic covering the claimed total. If setup is already included in preprocessing, split it out or identify the inclusion rather than adding it twice. Distinct phase names do not establish disjoint costs.

## Garbling, FSS, and NISC

Preserve construction-local role and object names: garbler or generator, evaluator, wire value, wire label, active label, garbled gate or table, and decoding information are not universal synonyms. For authenticated garbling, name what is authenticated and the mechanism. Keep garbling correctness, privacy, obliviousness, authenticity, and the final malicious-2PC theorem separate.

An FSS scheme shares a function description into keys whose local evaluations form additive, subtractive, or otherwise defined shares of `f(x)`. Distinguish the function description, FSS keys, local output shares, point evaluation, full-domain evaluation, and permitted leakage. A DPF is FSS for point functions; use DCF only with the source's comparison-function convention.

Separate an FSS scheme from a dealer or distributed protocol that generates FSS keys or correlations, and from verifiable FSS for malformed keys. Tree seeds, control bits, correction words, special paths, punctured evaluation, and named tree optimizations are construction-specific unless locally defined.

For NISC or another “non-interactive” construction, state setup or preprocessing, online message count and speaking order, output recipients, and whether receiver messages, setup, or encodings are single-use or reusable. “Non-interactive preprocessing” may still contain a simultaneous message exchange.

## Communication and round accounting

For communication, state:

- the unit: bits, bytes, symbols, field elements, ciphertexts, or concrete messages;
- the direction and aggregation convention: designated-direction traffic, bytes sent by a named party, the maximum sent by any party, or the sum of all send counters;
- honest-party-only versus all-party, per-party versus aggregate, and point-to-point versus broadcast;
- logical payload versus observed transport bytes.

Report hashes, correlation instances, primitive calls, oracle queries, and ideal-functionality calls as separate resource counts unless a concrete instantiation maps them to communication. Do not sum endpoint sent-and-received counters without checking whether this counts each transmission twice. Do not form rankings or ratios until units, aggregation rules, phase boundaries, and excluded resources are aligned.

A directional byte metric is not itself a latency bound. State full- or half-duplex operation, directional bandwidth, overlap, and the causal critical path before translating directional communication into wall-clock time.

For rounds, state the speaking and delivery pattern, topology, and whether messages are simultaneous. Separate messages, simultaneous-message layers, back-and-forth exchanges, causal protocol steps, ideal-resource calls, and concrete network rounds. Say which calls execute in parallel and whether setup generation, preprocessing, expected-round subprotocols, broadcast realization, or hybrid-resource instantiation is excluded.

## Asymptotic and amortized costs

State the denominator and scaling regime for every per-unit or amortized claim: gates, non-free gates, multiplications, correlations, statements, sessions, executions, or another unit. Distinguish amortization within one circuit, across batched preprocessing, and across repeated executions; parallel and sequential amortization are not interchangeable.

Preserve additive, circuit-independent, input/output, depth-dependent, party-dependent, and security-parameter-dependent terms that affect the regime. “Constant rate,” “linear communication,” “scalable,” “free,” and `O(1)` per gate are incomplete without what is held fixed, what is excluded, and where lower-order terms vanish. A garbled-circuit-equivalent ratio must name its reference scheme, parameter values, and included phases.

Keep circuit size, circuit depth, non-free gate count, primitive calls, proof size, total communication, local computation, memory, and latency separate. Pipelining may change overlap and storage without changing logical communication.

## Concrete evidence

Classify each number as measured, independently rerun, inherited, analytically derived, estimated, extrapolated, or projected. Distinguish a component benchmark from end-to-end performance. State excluded costs, parameter choices, hardware, network, concurrency, and whether the value is per party, per pair, or wall-clock time.
