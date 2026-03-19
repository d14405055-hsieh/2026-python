import sys


def is_jolly(seq):
    n = len(seq)
    if n <= 1:
        return True

    seen = set()
    for i in range(n - 1):
        d = abs(seq[i] - seq[i + 1])
        if 1 <= d <= n - 1:
            seen.add(d)

    return len(seen) == n - 1


def solve(text):
    data = text.split()
    idx = 0
    out = []

    while idx < len(data):
        n = int(data[idx])
        idx += 1
        seq = list(map(int, data[idx : idx + n]))
        idx += n
        out.append("Jolly" if is_jolly(seq) else "Not jolly")

    return "\n".join(out)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
