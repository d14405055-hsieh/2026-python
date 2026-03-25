"""UVA 10056 - What is the Probability ?（簡單版）"""

import sys


def solve(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    t = int(tokens[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(tokens[idx])
        p = float(tokens[idx + 1])
        i = int(tokens[idx + 2])
        idx += 3

        if p == 0.0:
            out.append("0.0000")
            continue

        q = (1.0 - p) ** n
        # 等比級數：第 i 位玩家第一次勝利機率 / (1 - q)
        prob = ((1.0 - p) ** (i - 1) * p) / (1.0 - q)
        out.append(f"{prob:.4f}")

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
