"""Synthetic 3-bit XOR round-trip check, not a security test."""


def encrypt(key, message):
    return key ^ message


def decrypt(key, ciphertext):
    return key ^ ciphertext


def main():
    checked = 0
    for key in range(8):
        for message in range(8):
            if decrypt(key, encrypt(key, message)) != message:
                raise SystemExit("FAIL: round trip")
            checked += 1
    print(f"PASS: {checked} synthetic 3-bit XOR round trips; security not tested")


if __name__ == "__main__":
    main()
