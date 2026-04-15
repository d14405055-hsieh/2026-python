import sys


K = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
MP = {c: i for i, c in enumerate(K)}


def dec(c: str) -> str:
    if c == " ":
        return " "
    lc = c.lower()
    if lc not in MP:
        return c
    i = MP[lc]
    d = K[i - 1] if i > 0 else lc
    return d.upper() if c.isupper() else d


def solve(data: str) -> str:
    return "".join(dec(c) for c in data)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
