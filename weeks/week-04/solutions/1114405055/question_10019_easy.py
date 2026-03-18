"""UVA 10019 簡單版：用 while 迴圈計算 bit 數。"""

import sys


def count_ones(x):
    ans = 0
    while x > 0:
        ans += x % 2
        x //= 2
    return ans


def solve(text):
    data = text.split()
    if not data:
        return ""

    t = int(data[0])
    out = []

    for i in range(1, t + 1):
        n = int(data[i])
        b1 = count_ones(n)
        b2 = count_ones(int(str(n), 16))
        out.append(f"{b1} {b2}")

    return "\n".join(out)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
