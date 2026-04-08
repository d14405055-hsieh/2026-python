import sys


class BIT:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (n + 1)

    def add(self, i, v):
        while i <= self.n:
            self.t[i] += v
            i += i & -i

    def kth(self, k):
        i = 0
        p = 1
        while (p << 1) <= self.n:
            p <<= 1
        while p:
            ni = i + p
            if ni <= self.n and self.t[ni] < k:
                k -= self.t[ni]
                i = ni
            p >>= 1
        return i + 1


def main():
    s = sys.stdin.read().strip().split()
    if not s:
        return
    n = int(s[0])
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        a[i] = int(s[i - 1])

    bit = BIT(n)
    for x in range(1, n + 1):
        bit.add(x, 1)

    out = [0] * (n + 1)
    for i in range(n, 0, -1):
        x = bit.kth(a[i] + 1)
        out[i] = x
        bit.add(x, -1)
    print("\n".join(map(str, out[1:])))


if __name__ == "__main__":
    main()
