import sys


def main() -> None:
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    max_width = max(len(line) for line in lines)
    output = []

    for column in range(max_width):
        chars = []
        for row in range(len(lines) - 1, -1, -1):
            if column < len(lines[row]):
                chars.append(lines[row][column])
            else:
                chars.append(" ")
        output.append("".join(chars))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()