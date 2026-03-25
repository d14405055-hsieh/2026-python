"""UVA 10057 - A mid-summer night's dream（手打版）"""

import sys
from bisect import bisect_left, bisect_right


def solve(data: str) -> str:
    values = [int(x) for x in data.split()]
    p = 0
    ans = []

    while p < len(values):
        n = values[p]
        p += 1

        arr = values[p:p + n]
        p += n
        arr.sort()

        # 最小絕對距離和會落在中位數區間 [a, b]。
        a = arr[(n - 1) // 2]
        b = arr[n // 2]

        # 統計所有位於 [a, b] 的元素個數。
        left_pos = bisect_left(arr, a)
        right_pos = bisect_right(arr, b)
        amount = right_pos - left_pos

        # 可行 A 的整數個數。
        count_a = b - a + 1

        ans.append(f"{a} {amount} {count_a}")

    return "\n".join(ans)


def main() -> None:
    data = sys.stdin.read()
    output = solve(data)
    if output:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
