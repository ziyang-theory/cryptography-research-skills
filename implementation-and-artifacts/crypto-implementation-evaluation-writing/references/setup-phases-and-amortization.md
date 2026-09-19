# Setup, phases, and amortization

Read when the section concerns asynchronous roles, OT/OLE/VOLE, programmable correlations, PCG-backed computation, proof-system preprocessing, or reuse. Use the target construction's definition and actual implementation. This common guide does not prescribe a specific protocol, message order, backend, or numerical communication total.

## State the interface and initial state

Identify the setup after which the interaction claim applies: key or seed establishment, dealer, PKI/CRS, base transfers, channels, or other assumed functionality. State which parts are implemented, idealized, excluded, or separately estimated.

Describe speakers/recipients, prerequisite information, local work, transmitted data, and when the defined output condition holds. A two-message asynchronous protocol may have initial preparation/message, response, and final local processing; use this only when it matches the paper's interface. Keep protocol rounds, messages, transport handshakes, and packets distinct.

State the dependency of each operation on function, inputs, participants, and session. Separate circuit-independent setup, circuit-dependent preparation, and online work when the construction makes those distinctions. For comparisons that include preparation after seed setup, include the same post-setup work on both sides.

State the required output and cleanup condition at the timer stop. Final local verification and consumed-secret handling may occur after the last message. An excluded joint diagnostic audit is different from a verification step required by the implemented protocol; disclose either exclusion according to its role.

File-mediated execution and local cycle counts establish the measured local costs. They do not establish network-delivery latency. Distinguish local-party timers, a jointly measured completion interval, and a modeled network schedule.

## Account for correlations through consumption

Record the relevant stages and which ones each metric includes:

| Stage | What to establish |
| --- | --- |
| Setup | How correlated seeds/keys or base correlations are obtained; interaction, assumptions, and excluded cost |
| Expansion | Local work, party-specific costs, memory, materialization or streaming |
| Checks and conversion | Authentication, sacrifice, consistency checks, random-to-fixed or other conversion; any interaction |
| Preparation and consumption | Function/input dependencies, consumed correlations, unused outputs, output handling |

A short seed measures one object, not total setup traffic. Local expansion throughput does not establish distributed setup throughput. Ideal or dealer-provided correlations should remain explicit in the stated performance scope; a realistic setup estimate stays separate from measured work.

Specify the output relation and unit: random/chosen/correlated/general OT, scalar/vector OLE or VOLE, field/ring width, dimension, block grouping, and programmability as applicable. Confirm that the measured interface supplies what the consuming protocol needs. Do not equate one vector with one scalar item or an arithmetic multiplication with a Boolean AND without a defined conversion.

Report raw outputs, usable outputs after checks, padding or unused outputs, and the quantity consumed by the measured workload. Define the throughput denominator and party aggregation. First usable output, first complete batch, and steady-state throughput are different metrics. Count complete usable objects rather than just a convenient role's partial outputs when claiming complete-object throughput.

## Explain reuse and amortization

Input independence does not establish reusability. Distinguish reusable setup from correlations consumed once, and point to the construction's permitted reuse conditions. A cache is an implementation choice, not a reuse argument. State participant, function, session, and fresh-randomness restrictions where relevant.

For a batch, identify how setup is allocated and account for minimum-batch waste. Keep sequential amortization, simultaneous batching, and pipelining separate. Expansion-only timing with prepared seeds does not determine latency from fresh setup through protocol output.

## Account for proof-system setup

Classify setup as universal or relation-specific, and state updateability or trust only when established by the construction. Identify which proving/verifying keys and precomputed tables may be reused, by whom, and for which relations or sessions. Keep witness-dependent preparation separate from input-independent preprocessing.

Report setup, witness generation, proving, and verification separately when they answer different questions. For amortized proving or batch verification, state the batch shape, public-input treatment, reused work, accepted proof count, and soundness target. Proof bytes do not automatically include public statements, commitments supplied separately, setup material, or protocol transport.

## Reconcile logical and measured costs

For theoretical communication, retain fixed/input/output terms, domain assumptions, and the message direction or aggregation. State whether a per-gate value is an asymptotic coefficient, an exact normalized formula, or an amortized measured quantity.

When both logical counts and observed counters exist, explain differences from serialization, headers, commitments, seeds, input handling, output verification, authentication, padding, batching, and transport. Include only mechanisms actually used by the target protocol; do not add a primitive or conversion merely because another construction uses it. If wire measurements are unavailable, label the logical count and say what is unmeasured.

Keep computational security, statistical soundness, correctness error under honest generation, and engineering failures separate. Do not reuse historical parameters as a new security recommendation or infer concrete security from functional tests or throughput. Report any unresolved instantiation or composition assumption that materially qualifies the advertised configuration, without turning a writing task into an unsolicited proof audit.

For optional historical MPC examples, see [evidence-sources.md](evidence-sources.md): P07 illustrates asynchronous roles, P17 OT-interface distinctions, and P26 modeled construction costs. These notes are not a survey of all MPC or proof-system implementations.
