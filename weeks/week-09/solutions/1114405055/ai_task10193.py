from __future__ import annotations

import math
import sys


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    t = int(lines[0])
    out: list[str] = []

    # AI 教學版：把二進位字串轉成整數，利用 gcd 判斷是否有共同因數 > 1。
    for i in range(1, t + 1):
        a = int(lines[2 * i - 1], 2)
        b = int(lines[2 * i], 2)
        if math.gcd(a, b) > 1:
            out.append(f"Pair #{i}: All you need is love!")
        else:
            out.append(f"Pair #{i}: Love is not all you need!")

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
