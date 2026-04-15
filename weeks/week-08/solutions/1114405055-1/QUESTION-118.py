import sys


def main() -> None:
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if not lines:
        return

    upper_x, upper_y = map(int, lines[0].split())
    directions = ["N", "E", "S", "W"]
    deltas = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0),
    }

    scents = set()
    output = []
    index = 1

    while index < len(lines):
        x, y, direction = lines[index].split()
        commands = lines[index + 1]
        index += 2

        x = int(x)
        y = int(y)
        facing = directions.index(direction)
        lost = False

        for command in commands:
            if command == "L":
                facing = (facing - 1) % 4
                continue
            if command == "R":
                facing = (facing + 1) % 4
                continue

            dx, dy = deltas[directions[facing]]
            next_x = x + dx
            next_y = y + dy

            if not (0 <= next_x <= upper_x and 0 <= next_y <= upper_y):
                if (x, y) not in scents:
                    scents.add((x, y))
                    lost = True
                    break
                continue

            x = next_x
            y = next_y

        result = f"{x} {y} {directions[facing]}"
        if lost:
            result += " LOST"
        output.append(result)

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()