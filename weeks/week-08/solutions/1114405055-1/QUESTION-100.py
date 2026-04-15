import sys


cache = {1: 1}


def cycle_length(number: int) -> int:
    if number in cache:
        return cache[number]

    if number % 2 == 0:
        length = 1 + cycle_length(number // 2)
    else:
        length = 1 + cycle_length(number * 3 + 1)

    cache[number] = length
    return length


def main() -> None:
    lines = [line.strip() for line in sys.stdin if line.strip()]
    result = []

    for line in lines:
        i, j = map(int, line.split())
        left, right = sorted((i, j))
        longest = 0

        for value in range(left, right + 1):
            longest = max(longest, cycle_length(value))

        result.append(f"{i} {j} {longest}")

    sys.stdout.write("\n".join(result))


if __name__ == "__main__":
    main()