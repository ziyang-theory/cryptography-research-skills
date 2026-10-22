# Synthetic one-use field operation

This is an invented code/specification correspondence exercise, not a deployed protocol or a security theorem.

The caller constructs `OneUseMask(mask)` with an integer `mask` in `{0,...,16}`. A fresh object has `used == False`. This constructor precondition is assumed; constructor validation is outside the exercise.

`apply(encoded)` receives a Python string. Its legal values are exactly `str(x)` for integers `0 <= x < 17`: canonical ASCII decimal encodings without signs, whitespace, or leading zeroes (except the string `"0"`).

- If the object is already used, raise `ValueError` and return no value.
- If `encoded` is not legal, raise `ValueError`, return no value, and leave `used` unchanged. In particular, an invalid first message does not consume the pending operation.
- Otherwise set `used = True` and return `(x + mask) % 17` as an integer.

The state and rejection behavior are part of the specification. Agreement on legal inputs alone does not establish correspondence. This document makes no confidentiality, authentication, or malicious-security claim.
