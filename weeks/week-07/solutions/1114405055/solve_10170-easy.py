import sys


def days_sum(s, n):
    # 計算從 s 到 n 的總天數: s + (s+1) + ... + n
    cnt = n - s + 1
    return (s + n) * cnt // 2


def solve_one(s, d):
    lo, hi = s, s
    while days_sum(s, hi) < d:
        hi *= 2

    while lo < hi:
        mid = (lo + hi) // 2
        if days_sum(s, mid) >= d:
            hi = mid
        else:
            lo = mid + 1
    return lo


def solve():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        s, d = map(int, line.split())
        out.append(str(solve_one(s, d)))
    print("\n".join(out))


if __name__ == "__main__":
    solve()
