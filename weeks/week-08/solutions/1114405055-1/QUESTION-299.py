import sys


def main() -> None:
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    cases = int(tokens[0])
    index = 1
    results = []

    for _ in range(cases):
        length = int(tokens[index])
        index += 1
        cars = list(map(int, tokens[index:index + length]))
        index += length

        swaps = 0
        for left in range(length):
            for right in range(left + 1, length):
                if cars[left] > cars[right]:
                    swaps += 1

        results.append(f"Optimal train swapping takes {swaps} swaps.")

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()