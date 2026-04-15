import sys


def main() -> None:
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    test_count = int(tokens[0])
    position = 1
    output_lines = []

    for _ in range(test_count):
        length = int(tokens[position])
        position += 1
        cars = list(map(int, tokens[position:position + length]))
        position += length

        swaps = 0
        for i in range(length):
            for j in range(i + 1, length):
                if cars[i] > cars[j]:
                    swaps += 1

        output_lines.append(f"Optimal train swapping takes {swaps} swaps.")

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()