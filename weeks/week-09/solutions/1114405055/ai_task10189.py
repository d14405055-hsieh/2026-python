from __future__ import annotations

import sys


def solve(data: str) -> str:
    lines = data.splitlines()
    i = 0
    field_no = 1
    outputs: list[str] = []

    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line:
            continue

        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break

        grid = [list(lines[i + r].rstrip("\n")) for r in range(n)]
        i += n

        # AI 教學版：逐格計算周圍 8 個方向的地雷數量。
        result: list[str] = []
        for r in range(n):
            row_chars: list[str] = []
            for c in range(m):
                if grid[r][c] == "*":
                    row_chars.append("*")
                    continue

                mines = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "*":
                            mines += 1
                row_chars.append(str(mines))
            result.append("".join(row_chars))

        if outputs:
            outputs.append("")
        outputs.append(f"Field #{field_no}:")
        outputs.extend(result)
        field_no += 1

    return "\n".join(outputs)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
