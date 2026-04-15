import sys


def main() -> None:
    text = sys.stdin.read()
    toggle = True
    output = []

    for char in text:
        if char == '"':
            output.append("``" if toggle else "''")
            toggle = not toggle
        else:
            output.append(char)

    sys.stdout.write("".join(output))


if __name__ == "__main__":
    main()