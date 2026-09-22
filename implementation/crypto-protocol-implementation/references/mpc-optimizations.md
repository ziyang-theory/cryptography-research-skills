# MPC optimizations

Use this reference for MPC-specific candidates after fixing the objective and security contract. Apply the techniques justified by the backend and workload; these are not interchangeable implementations of the same protocol.

## Optimize the computation and its representation

Use backend costs rather than ordinary instruction count. For an appropriate garbling construction, non-XOR gates can dominate; for interactive sharing, multiplicative depth and conversion rounds can matter alongside multiplication count. Consider public-constant propagation, dead-output elimination, common subexpressions and size/depth tradeoffs while preserving the specified outputs and observable execution.

Treat integer width, signedness, overflow and fixed-point truncation as functionality. Narrowing is valid only under the original semantics or a justified range invariant. An approximation that changes numerical results needs an explicit changed specification and quality target. Replacing a field with a ring also changes the algebra used by authentication, preprocessing and security arguments; it is not just a faster modular-reduction implementation.

For mixed arithmetic, Boolean and garbled representations, optimize regions and their conversion boundaries together. Account for operation costs plus all conversions, including interaction, preprocessing and checks. Selecting the cheapest representation for each operation separately can lose to conversion overhead. Consistent arithmetic/bitwise sharings, such as those supplied by an applicable edaBit protocol, are cryptographic correlations rather than ordinary casts; use the exact generation and consumption contract.

Distinguish CPU vectorization, vectors of secret operations and packed secret sharing. Packed sharing needs the construction's capacity, reconstruction and corruption-threshold conditions. Adding threads does not provide its communication savings.

## Exploit structure without hiding preprocessing

Expose matrix/vector or polynomial structure when a matching protocol can exploit it. Structured preprocessing can reduce online openings relative to treating every scalar multiplication independently, but account for generation of the required correlations, authentication, local products, conversions and delivery. Independent scalar triples are not automatically an implementation of a specified matrix correlation; identify any construction and its cost.

For OT extension or PCG/silent-correlation replacements, match the consumer's exact output relation and party holdings, exposed seeds/keys, setup generation, output programmability and malicious checks. Reduced communication may shift the bottleneck to local expansion. Include adapters, discarded outputs and fresh consumables; a correlated-OT rate is not directly a chosen-message-OT or authenticated-triple rate. Use [specification and distributions](specification-and-distributions.md) for the joint distribution and setup argument.

For garbling, preserve the selected free-XOR/half-gate/fixed-key construction and its assumptions. Batch or vectorize its prescribed primitives where supported. An arbitrary hash substitution is not justified solely by collision resistance or ordinary secret-key block-cipher security. Gate-table payload alone excludes input transfer, output handling, framing, setup and malicious-security mechanisms; identify the applicable costs when comparing candidates.

## Preserve access and check semantics

Private indexing, sorting and secret-dependent selection may dominate surrounding arithmetic. Consider a public ordering, batched join, regular circuit or appropriate oblivious data structure if it reduces the measured cost while preserving functionality and leakage. A revealed sparsity pattern, loop count or intermediate comparison is additional leakage unless already permitted. Streaming must retain values for all live consumers and keep the schedule within the allowed observation model.

Distinguish batching messages from changing or deferring malicious-security checks. For a changed linear check, identify the domain, when errors are fixed, coefficient distribution and permitted reuse. Independent uniform field coefficients, powers of one challenge and ring coefficients require different arguments; do not transfer a field soundness bound without its hypotheses. Consult the exact corrected protocol version when reproducing a check or its communication count. Final checks must precede the output or action they are meant to authorize; use [security preservation](security-preservation.md) for affected proof obligations.
