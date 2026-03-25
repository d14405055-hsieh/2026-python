"""10055（依題目敘述：函數增減性查詢）簡單版"""

import sys


class Fenwick:
    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def prefix_sum(self, idx: int) -> int:
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

    def range_sum(self, left: int, right: int) -> int:
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


def solve(data: str) -> str:
    vals = [int(x) for x in data.split()]
    if not vals:
        return ""

    n, q = vals[0], vals[1]
    ptr = 2
    fw = Fenwick(n)
    flipped = [0] * (n + 1)
    out = []

    for _ in range(q):
        v = vals[ptr]
        ptr += 1
        if v == 1:
            i = vals[ptr]
            ptr += 1
            # 反轉一次代表奇偶性改變，1 表示目前是減函數。
            if flipped[i] == 0:
                flipped[i] = 1
                fw.add(i, 1)
            else:
                flipped[i] = 0
                fw.add(i, -1)
        else:
            l, r = vals[ptr], vals[ptr + 1]
            ptr += 2
            dec_count = fw.range_sum(l, r)
            out.append("1" if dec_count % 2 else "0")

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
