from __future__ import annotations

import sys


def build_sequence(n: int, m: int) -> str:
    # AI 教學版：只要不符合規則（包含中途不能整除），就輸出 Boring!。
    if n < 2 or m < 2:
        return "Boring!"

    seq = [n]
    while n != 1:
        if n % m != 0:
            return "Boring!"
        n //= m
        seq.append(n)

    return " ".join(map(str, seq))


def solve(data: str) -> str:
    out: list[str] = []
    for line in data.splitlines():
        text = line.strip()
        if not text:
            continue
        n, m = map(int, text.split())
        out.append(build_sequence(n, m))
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
