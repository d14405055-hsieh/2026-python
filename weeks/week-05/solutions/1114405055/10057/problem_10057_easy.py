"""UVA 10057 - A mid-summer night's dream（簡單版）"""

import sys
from bisect import bisect_left, bisect_right


def solve(data: str) -> str:
    nums = [int(x) for x in data.split()]
    idx = 0
    out = []

    while idx < len(nums):
        n = nums[idx]
        idx += 1
        arr = nums[idx:idx + n]
        idx += n
        arr.sort()

        low = arr[(n - 1) // 2]
        high = arr[n // 2]

        cnt = bisect_right(arr, high) - bisect_left(arr, low)
        ways = high - low + 1

        out.append(f"{low} {cnt} {ways}")

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
