from __future__ import annotations

import sys


def sequence_or_boring(n: int, m: int) -> str:
    if n < 2 or m < 2:
        return "Boring!"

    seq = [n]
    current = n
    while current != 1:
        if current % m != 0:
            return "Boring!"
        current //= m
        seq.append(current)

    return " ".join(str(x) for x in seq)


def solve(data: str) -> str:
    result: list[str] = []
    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue
        n, m = map(int, line.split())
        result.append(sequence_or_boring(n, m))
    return "\n".join(result)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
