import math
import sys


def solve(data: str) -> str:
    ans = []
    for ln in data.strip().splitlines():
        if not ln.strip():
            continue
        s, a, u = ln.split()
        s = float(s)
        a = float(a)

        if u == "min":
            a /= 60.0

        if a > 180.0:
            a = 360.0 - a

        r = 6440.0 + s
        x = a * math.pi / 180.0
        arc = r * x
        chord = 2.0 * r * math.sin(x / 2.0)
        ans.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(ans)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
