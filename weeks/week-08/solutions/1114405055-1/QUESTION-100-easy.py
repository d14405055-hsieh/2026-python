import sys


cache = {1: 1}


def cycle_length(number: int) -> int:
    # 先把走過的路徑記起來，等找到已知答案再往回補
    path = []
    current = number

    while current not in cache:
        path.append(current)
        if current % 2 == 0:
            current //= 2
        else:
            current = current * 3 + 1

    length = cache[current]
    while path:
        value = path.pop()
        length += 1
        cache[value] = length

    return cache[number]


def main() -> None:
    output_lines = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        first, second = map(int, line.split())
        left = min(first, second)
        right = max(first, second)

        best = 0
        for value in range(left, right + 1):
            best = max(best, cycle_length(value))

        output_lines.append(f"{first} {second} {best}")

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()