"""UVA 10041 - Vito's Family（手打版）"""

import sys


def solve(data: str) -> str:
    nums = [int(x) for x in data.split()]
    if not nums:
        return ""

    case_count = nums[0]
    ptr = 1
    out = []

    for _ in range(case_count):
        count = nums[ptr]
        ptr += 1
        houses = nums[ptr:ptr + count]
        ptr += count

        houses.sort()

        # 用中位數當作新家門牌，可讓絕對距離總和最小。
        choose = houses[count // 2]

        distance_sum = 0
        for h in houses:
            distance_sum += abs(h - choose)

        out.append(str(distance_sum))

    return "\n".join(out)


def main() -> None:
    data = sys.stdin.read()
    ans = solve(data)
    if ans:
        sys.stdout.write(ans)


if __name__ == "__main__":
    main()
