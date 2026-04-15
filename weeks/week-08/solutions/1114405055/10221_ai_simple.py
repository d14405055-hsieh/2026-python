"""UVA 10221 - Satellites（AI 簡單版，含中文註解）"""

import math
import sys


def solve(data: str) -> str:
    out = []
    for line in data.strip().splitlines():
        if not line.strip():
            continue
        s_str, a_str, unit = line.split()
        s = float(s_str)
        a = float(a_str)

        # 單位轉換：min -> deg
        if unit == "min":
            a /= 60.0

        # 取較小圓心角（弧長要走短弧）
        if a > 180.0:
            a = 360.0 - a

        r = 6440.0 + s
        rad = math.radians(a)

        arc = r * rad
        chord = 2.0 * r * math.sin(rad / 2.0)

        out.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
