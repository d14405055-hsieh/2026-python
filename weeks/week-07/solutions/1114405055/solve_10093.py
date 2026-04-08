import sys


def solve():
    a = sys.stdin.read().strip().split()
    if not a:
        return
    n = int(a[0])
    m = int(a[1])
    g = a[2:2 + n]

    st = []
    for s in range(1 << m):
        if (s & (s << 1)) == 0 and (s & (s << 2)) == 0:
            st.append(s)

    land = []
    for r in g:
        ms = 0
        for i, ch in enumerate(r):
            if ch == "P":
                ms |= (1 << i)
        land.append(ms)

    rs = []
    for i in range(n):
        cur = []
        for s in st:
            if (s & ~land[i]) == 0:
                cur.append(s)
        rs.append(cur)

    dp = {}
    for s in rs[0]:
        dp[(s, 0)] = s.bit_count()

    for i in range(1, n):
        ndp = {}
        for c in rs[i]:
            cc = c.bit_count()
            for (p1, p2), v in dp.items():
                if (c & p1) == 0 and (c & p2) == 0:
                    k = (c, p1)
                    nv = v + cc
                    ov = ndp.get(k)
                    if ov is None or nv > ov:
                        ndp[k] = nv
        dp = ndp

    print(max(dp.values()) if dp else 0)


if __name__ == "__main__":
    solve()
