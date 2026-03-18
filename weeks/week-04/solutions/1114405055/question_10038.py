"""UVA 10038 - Jolly Jumpers."""

from __future__ import annotations

import sys
from typing import List


def is_jolly(seq: List[int]) -> bool:
    """判斷序列是否為 jolly jumper。"""
    n = len(seq)
    if n <= 1:
        return True

    diffs = set()
    for i in range(n - 1):
        d = abs(seq[i] - seq[i + 1])
        if 1 <= d <= n - 1:
            diffs.add(d)

    return len(diffs) == n - 1


def solve(data: str) -> str:
    tokens = data.split()
    idx = 0
    out: List[str] = []

    while idx < len(tokens):
        n = int(tokens[idx])
        idx += 1
        seq = [int(x) for x in tokens[idx : idx + n]]
        idx += n
        out.append("Jolly" if is_jolly(seq) else "Not jolly")

    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
