import sys


def main() -> None:
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    width = max(len(line) for line in lines)
    rotated = []

    for column in range(width):
        chars = []
        for row in range(len(lines) - 1, -1, -1):
            line = lines[row]
            if column < len(line):
                chars.append(line[column])
            else:
                chars.append(" ")
        rotated.append("".join(chars))

    sys.stdout.write("\n".join(rotated))


if __name__ == "__main__":
    main()