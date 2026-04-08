import sys


def bitcount(x):
    return x.bit_count()


def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    rows = data[2:2 + n]

    valid_states = []
    for s in range(1 << m):
        # 同一列不可左右相鄰或隔一格互打
        if (s & (s << 1)) == 0 and (s & (s << 2)) == 0:
            valid_states.append(s)

    plains = []
    for r in rows:
        mask = 0
        for i, ch in enumerate(r):
            if ch == "P":
                mask |= (1 << i)
        plains.append(mask)

    row_states = []
    for i in range(n):
        ok = []
        for s in valid_states:
            if (s & ~plains[i]) == 0:
                ok.append(s)
        row_states.append(ok)

    dp = {}
    for s in row_states[0]:
        dp[(s, 0)] = bitcount(s)

    for i in range(1, n):
        ndp = {}
        for cur in row_states[i]:
            c = bitcount(cur)
            for (pre, prepre), val in dp.items():
                # 不可與前一列、前兩列同欄互打
                if (cur & pre) == 0 and (cur & prepre) == 0:
                    key = (cur, pre)
                    best = val + c
                    if key not in ndp or best > ndp[key]:
                        ndp[key] = best
        dp = ndp

    print(max(dp.values()) if dp else 0)


if __name__ == "__main__":
    solve()
