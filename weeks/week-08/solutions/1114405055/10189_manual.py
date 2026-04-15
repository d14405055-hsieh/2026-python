import sys


def solve(data: str) -> str:
    lines = data.strip().splitlines()
    i = 0
    k = 1
    out = []
    d8 = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    while i < len(lines):
        n, m = map(int, lines[i].split())
        i += 1
        if n == 0 and m == 0:
            break

        g = [list(lines[i + r].strip()) for r in range(n)]
        i += n
        a = [["0"] * m for _ in range(n)]

        for r in range(n):
            for c in range(m):
                if g[r][c] == "*":
                    a[r][c] = "*"
                else:
                    cnt = 0
                    for dr, dc in d8:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < n and 0 <= nc < m and g[nr][nc] == "*":
                            cnt += 1
                    a[r][c] = str(cnt)

        if out:
            out.append("")
        out.append(f"Field #{k}:")
        out.extend("".join(row) for row in a)
        k += 1

    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
