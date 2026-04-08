import sys


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, delta):
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def kth(self, k):
        # 找到前綴和 >= k 的最小索引，也就是第 k 小的值
        idx = 0
        step = 1
        while (step << 1) <= self.n:
            step <<= 1
        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            step >>= 1
        return idx + 1


def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    smaller = [0] * (n + 1)
    for i in range(2, n + 1):
        smaller[i] = int(data[i - 1])

    fw = Fenwick(n)
    for x in range(1, n + 1):
        fw.add(x, 1)

    ans = [0] * (n + 1)
    for i in range(n, 0, -1):
        pos = smaller[i] + 1
        val = fw.kth(pos)
        ans[i] = val
        fw.add(val, -1)

    print("\n".join(map(str, ans[1:])))


if __name__ == "__main__":
    solve()
