from __future__ import annotations

import sys


def cycle_length(n: int, memo: dict[int, int]) -> int:
    """Return Collatz cycle length for n (including n and 1)."""
    original = n
    sequence: list[int] = []

    while n not in memo:
        sequence.append(n)
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2

    length = memo[n]
    for value in reversed(sequence):
        length += 1
        memo[value] = length

    return memo[original]


def solve(text: str) -> str:
    memo = {1: 1}
    out_lines: list[str] = []

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        i, j = map(int, line.split())
        lo, hi = (i, j) if i <= j else (j, i)

        max_cycle = 0
        for n in range(lo, hi + 1):
            c = cycle_length(n, memo)
            if c > max_cycle:
                max_cycle = c

        out_lines.append(f"{i} {j} {max_cycle}")

    return "\n".join(out_lines)


if __name__ == "__main__":
    data = sys.stdin.read()
    print(solve(data))
