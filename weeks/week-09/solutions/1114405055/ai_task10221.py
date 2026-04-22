from __future__ import annotations

import math
import sys


PI = math.pi
EARTH_RADIUS = 6440.0


def compute_arc_and_chord(s: float, a: float, unit: str) -> tuple[float, float]:
    # AI 教學版：先把角度正規化到 <= 180，再依單位換算成弧度。
    if unit == "min":
        angle_deg = a / 60.0
    else:
        angle_deg = a

    if angle_deg > 180.0:
        angle_deg = 360.0 - angle_deg

    theta = angle_deg * PI / 180.0
    radius = EARTH_RADIUS + s

    arc = radius * theta
    chord = 2.0 * radius * math.sin(theta / 2.0)
    return arc, chord


def solve(data: str) -> str:
    out: list[str] = []
    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue
        s_str, a_str, unit = line.split()
        arc, chord = compute_arc_and_chord(float(s_str), float(a_str), unit)
        out.append(f"{arc:.6f} {chord:.6f}")
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
