"""題號 10193：最小化 b+c（AI 簡單版，含中文註解）"""

import math
import sys


def solve(data: str) -> str:
    a = int(data.strip())
    target = a * a + 1

    best = None

    # 由 (b-a)(c-a)=a^2+1，可轉為找 target 的因數對
    d = 1
    while d * d <= target:
        if target % d == 0:
            e = target // d
            cur = d + e + 2 * a
            if best is None or cur < best:
                best = cur
        d += 1

    return str(best)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
