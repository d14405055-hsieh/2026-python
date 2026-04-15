"""UVA 10222 - Decode the Mad man（AI 簡單版，含中文註解）"""

import sys


KEYS = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
POS = {ch: i for i, ch in enumerate(KEYS)}


def decode_char(ch: str) -> str:
    if ch == " ":
        return " "

    low = ch.lower()
    if low not in POS:
        return ch

    idx = POS[low]
    if idx == 0:
        out = low
    else:
        out = KEYS[idx - 1]

    return out.upper() if ch.isupper() else out


def solve(data: str) -> str:
    return "".join(decode_char(c) for c in data)


def main() -> None:
    print(solve(sys.stdin.read()), end="")


if __name__ == "__main__":
    main()
