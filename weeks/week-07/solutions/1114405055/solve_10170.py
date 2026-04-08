import sys


def segsum(s, n):
    c = n - s + 1
    return (s + n) * c // 2


def find_n(s, d):
    l = s
    r = s
    while segsum(s, r) < d:
        r <<= 1
    while l < r:
        m = (l + r) // 2
        if segsum(s, m) >= d:
            r = m
        else:
            l = m + 1
    return l


def main():
    ans = []
    for ln in sys.stdin:
        ln = ln.strip()
        if not ln:
            continue
        s, d = map(int, ln.split())
        ans.append(str(find_n(s, d)))
    print("\n".join(ans))


if __name__ == "__main__":
    main()
