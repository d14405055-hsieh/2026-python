"""UVA 10050 - Hartals（簡單版）"""

import sys


def solve(data: str) -> str:
    nums = [int(x) for x in data.split()]
    if not nums:
        return ""

    t = nums[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = nums[idx]
        idx += 1
        p = nums[idx]
        idx += 1
        hs = nums[idx:idx + p]
        idx += p

        lost_days = set()
        for h in hs:
            day = h
            while day <= n:
                # 第 6 天是星期五、第 7 天是星期六，都不算工作天。
                mod = day % 7
                if mod != 6 and mod != 0:
                    lost_days.add(day)
                day += h

        ans.append(str(len(lost_days)))

    return "\n".join(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
