from __future__ import annotations

import sys


def solve(text: str) -> str:
    # Keep leading/trailing spaces in each line; only strip final newlines.
    lines = text.splitlines()
    if not lines:
        return ""

    width = max(len(line) for line in lines)
    height = len(lines)

    padded = [line.ljust(width, " ") for line in lines]
    out_lines: list[str] = []

    for col in range(width):
        chars = []
        for row in range(height - 1, -1, -1):
            chars.append(padded[row][col])
        out_lines.append("".join(chars).rstrip())

    return "\n".join(out_lines)


if __name__ == "__main__":
    data = sys.stdin.read()
    print(solve(data))
