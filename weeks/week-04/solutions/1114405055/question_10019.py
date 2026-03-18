"""UVA 10019 - Funny Encryption Method."""

from __future__ import annotations

import sys
from typing import List, Tuple


def bit_count_in_decimal_and_hex(n: int) -> Tuple[int, int]:
    """回傳 (十進位數值的 1-bit 數, 十進位字串當十六進位解讀後的 1-bit 數)。"""
    b1 = bin(n).count("1")
    hex_interpret = int(str(n), 16)
    b2 = bin(hex_interpret).count("1")
    return b1, b2


def solve(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    t = int(tokens[0])
    nums = [int(x) for x in tokens[1 : 1 + t]]
    out: List[str] = []
    for num in nums:
        b1, b2 = bit_count_in_decimal_and_hex(num)
        out.append(f"{b1} {b2}")
    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
