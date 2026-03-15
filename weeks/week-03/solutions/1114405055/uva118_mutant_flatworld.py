from __future__ import annotations

import sys


DIRECTIONS = "NESW"
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def turn(direction: str, cmd: str) -> str:
    idx = DIRECTIONS.index(direction)
    if cmd == "L":
        return DIRECTIONS[(idx - 1) % 4]
    return DIRECTIONS[(idx + 1) % 4]


def solve(text: str) -> str:
    lines = [line.rstrip("\n") for line in text.splitlines() if line.strip() != ""]
    if not lines:
        return ""

    max_x, max_y = map(int, lines[0].split())
    scents: set[tuple[int, int]] = set()
    out_lines: list[str] = []

    i = 1
    while i + 1 < len(lines):
        x, y, direction = lines[i].split()
        x = int(x)
        y = int(y)
        commands = lines[i + 1].strip()

        lost = False
        for cmd in commands:
            if cmd in ("L", "R"):
                direction = turn(direction, cmd)
                continue

            dx, dy = MOVE[direction]
            nx, ny = x + dx, y + dy

            if 0 <= nx <= max_x and 0 <= ny <= max_y:
                x, y = nx, ny
                continue

            # Ignore dangerous move if current cell already has scent.
            if (x, y) in scents:
                continue

            scents.add((x, y))
            lost = True
            break

        if lost:
            out_lines.append(f"{x} {y} {direction} LOST")
        else:
            out_lines.append(f"{x} {y} {direction}")

        i += 2

    return "\n".join(out_lines)


if __name__ == "__main__":
    data = sys.stdin.read()
    print(solve(data))
