from __future__ import annotations

import sys


def inversion_count(nums: list[int]) -> int:
    swaps = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                swaps += 1
    return swaps


def solve(text: str) -> str:
    tokens = text.split()
    if not tokens:
        return ""

    t = int(tokens[0])
    idx = 1
    out_lines: list[str] = []

    for _ in range(t):
        l = int(tokens[idx])
        idx += 1
        train = list(map(int, tokens[idx : idx + l]))
        idx += l

        swaps = inversion_count(train)
        out_lines.append(f"Optimal train swapping takes {swaps} swaps.")

    return "\n".join(out_lines)


if __name__ == "__main__":
    data = sys.stdin.read()
    print(solve(data))
