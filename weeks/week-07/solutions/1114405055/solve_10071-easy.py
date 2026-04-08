import sys
from collections import defaultdict


def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    nums = list(map(int, data[1:1 + n]))

    # 先統計所有 a+b+c 的和出現次數
    cnt3 = defaultdict(int)
    for a in nums:
        for b in nums:
            for c in nums:
                cnt3[a + b + c] += 1

    # 再枚舉 d,e,f，查詢 a+b+c = f-d-e
    ans = 0
    for d in nums:
        for e in nums:
            for f in nums:
                ans += cnt3[f - d - e]

    print(ans)


if __name__ == "__main__":
    solve()
