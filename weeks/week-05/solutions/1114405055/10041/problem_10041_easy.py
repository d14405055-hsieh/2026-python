"""UVA 10041 - Vito's Family（簡單版）"""

import sys


def solve(data: str) -> str:
    tokens = list(map(int, data.split()))
    if not tokens:
        return ""

    t = tokens[0]
    idx = 1
    answers = []

    for _ in range(t):
        r = tokens[idx]
        idx += 1
        relatives = tokens[idx:idx + r]
        idx += r

        # 距離總和最小的位置會在中位數。
        relatives.sort()
        median = relatives[r // 2]
        total = sum(abs(x - median) for x in relatives)
        answers.append(str(total))

    return "\n".join(answers)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
