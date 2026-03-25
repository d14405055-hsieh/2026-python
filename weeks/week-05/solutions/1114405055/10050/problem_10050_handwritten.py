"""UVA 10050 - Hartals（手打版）"""

import sys


def solve(data: str) -> str:
    values = [int(x) for x in data.split()]
    if not values:
        return ""

    tc = values[0]
    pos = 1
    out = []

    for _ in range(tc):
        total_days = values[pos]
        pos += 1
        party_count = values[pos]
        pos += 1
        hartals = values[pos:pos + party_count]
        pos += party_count

        lost = [False] * (total_days + 1)

        for h in hartals:
            d = h
            while d <= total_days:
                weekday = d % 7
                # 逢星期五(6)與星期六(0)休假，罷會不算損失工作日。
                if weekday != 6 and weekday != 0:
                    lost[d] = True
                d += h

        out.append(str(sum(lost)))

    return "\n".join(out)


def main() -> None:
    data = sys.stdin.read()
    answer = solve(data)
    if answer:
        sys.stdout.write(answer)


if __name__ == "__main__":
    main()
