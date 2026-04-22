from __future__ import annotations

import sys


def solve(data: str) -> str:
    lines = data.splitlines()
    idx = 0
    field_index = 1
    out: list[str] = []

    while idx < len(lines):
        head = lines[idx].strip()
        idx += 1
        if not head:
            continue

        n, m = map(int, head.split())
        if n == 0 and m == 0:
            break

        board = [list(lines[idx + r].rstrip("\n")) for r in range(n)]
        idx += n

        answer: list[str] = []
        for r in range(n):
            row: list[str] = []
            for c in range(m):
                if board[r][c] == "*":
                    row.append("*")
                else:
                    count = 0
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == "*":
                                count += 1
                    row.append(str(count))
            answer.append("".join(row))

        if out:
            out.append("")
        out.append(f"Field #{field_index}:")
        out.extend(answer)
        field_index += 1

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
