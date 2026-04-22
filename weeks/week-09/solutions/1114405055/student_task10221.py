from __future__ import annotations

import math
import sys


EARTH_RADIUS = 6440.0


def one_case(s: float, a: float, unit: str) -> tuple[float, float]:
    angle_deg = a / 60.0 if unit == "min" else a
    if angle_deg > 180.0:
        angle_deg = 360.0 - angle_deg

    rad = math.radians(angle_deg)
    r = EARTH_RADIUS + s
    arc = r * rad
    chord = 2.0 * r * math.sin(rad / 2.0)
    return arc, chord


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    ans: list[str] = []

    for line in lines:
        s_str, a_str, unit = line.split()
        arc, chord = one_case(float(s_str), float(a_str), unit)
        ans.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
