import sys


def main() -> None:
    data = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if not data:
        return

    upper_x, upper_y = map(int, data[0].split())
    directions = ["N", "E", "S", "W"]
    moves = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0),
    }

    scents = set()
    output_lines = []
    index = 1

    while index < len(data):
        x, y, direction = data[index].split()
        commands = data[index + 1]
        index += 2

        x = int(x)
        y = int(y)
        direction_index = directions.index(direction)
        lost = False

        for command in commands:
            if command == "L":
                direction_index = (direction_index - 1) % 4
            elif command == "R":
                direction_index = (direction_index + 1) % 4
            else:
                dx, dy = moves[directions[direction_index]]
                next_x = x + dx
                next_y = y + dy

                if not (0 <= next_x <= upper_x and 0 <= next_y <= upper_y):
                    if (x, y) in scents:
                        continue
                    scents.add((x, y))
                    lost = True
                    break

                x = next_x
                y = next_y

        result = f"{x} {y} {directions[direction_index]}"
        if lost:
            result += " LOST"
        output_lines.append(result)

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()