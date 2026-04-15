import sys


def solve(data: str) -> str:
    a = int(data.strip())
    n = a * a + 1
    ans = 10**30

    d = 1
    while d * d <= n:
        if n % d == 0:
            e = n // d
            s = d + e + 2 * a
            if s < ans:
                ans = s
        d += 1

    return str(ans)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
