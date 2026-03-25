"""UVA 10056 - What is the Probability ?（手打版）"""

import sys


def solve(data: str) -> str:
    parts = data.split()
    if not parts:
        return ""

    t = int(parts[0])
    ptr = 1
    result = []

    for _ in range(t):
        player_count = int(parts[ptr])
        success_p = float(parts[ptr + 1])
        target = int(parts[ptr + 2])
        ptr += 3

        # 成功機率為 0 時永遠不會有人贏。
        if success_p == 0.0:
            result.append("0.0000")
            continue

        one_round_fail = (1.0 - success_p) ** player_count
        first_hit = (1.0 - success_p) ** (target - 1) * success_p
        ans = first_hit / (1.0 - one_round_fail)

        result.append(f"{ans:.4f}")

    return "\n".join(result)


def main() -> None:
    text = sys.stdin.read()
    output = solve(text)
    if output:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
