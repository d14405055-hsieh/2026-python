"""UVA 10035 - Primary Arithmetic."""

from __future__ import annotations

import sys
from typing import List


def count_carries(a: int, b: int) -> int:
    """計算 a + b 在直式加法中發生幾次進位。"""
    carries = 0
    carry = 0

    while a > 0 or b > 0:
        digit_sum = (a % 10) + (b % 10) + carry
        if digit_sum >= 10:
            carries += 1
            carry = 1
        else:
            carry = 0
        a //= 10
        b //= 10

    return carries


def _format_carry_message(carries: int) -> str:
    if carries == 0:
        return "No carry operation."
    if carries == 1:
        return "1 carry operation."
    return f"{carries} carry operations."


def solve(data: str) -> str:
    tokens = data.split()
    out: List[str] = []

    for i in range(0, len(tokens), 2):
        a = int(tokens[i])
        b = int(tokens[i + 1])
        if a == 0 and b == 0:
            break
        out.append(_format_carry_message(count_carries(a, b)))

    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
