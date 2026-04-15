"""UVA 10189 - Minesweeper (AI 簡單版本，含中文註解)"""

import sys


def solve(data: str) -> str:
    lines = data.strip().splitlines()
    i = 0
    field_id = 1
    out = []

    # 8 個方向：上、下、左、右、四個斜角
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    while i < len(lines):
        n, m = map(int, lines[i].split())
        i += 1
        if n == 0 and m == 0:
            break

        grid = [list(lines[i + r].strip()) for r in range(n)]
        i += n

        # 先建立答案網格，預設都是 0
        ans = [["0"] * m for _ in range(n)]

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "*":
                    ans[r][c] = "*"
                    continue

                # 對空白格計算周圍 8 格地雷數
                count = 0
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "*":
                        count += 1
                ans[r][c] = str(count)

        if out:
            out.append("")
        out.append(f"Field #{field_id}:")
        out.extend("".join(row) for row in ans)
        field_id += 1

    return "\n".join(out)


def main() -> None:
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
