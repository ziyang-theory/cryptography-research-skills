"""Synthetic correspondence-review fixture; not deployed cryptographic code."""


class OneUseMask:
    def __init__(self, mask):
        self.mask = mask
        self.used = False

    def apply(self, encoded):
        if self.used:
            raise ValueError("already consumed")
        if (
            not isinstance(encoded, str)
            or not encoded
            or not encoded.isascii()
            or not encoded.isdigit()
            or (len(encoded) > 1 and encoded.startswith("0"))
        ):
            raise ValueError("invalid encoding")
        x = int(encoded) % 17
        self.used = True
        return (x + self.mask) % 17
