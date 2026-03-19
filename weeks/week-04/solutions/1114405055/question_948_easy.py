import sys


def possible_with_mode(coin, heavier, weighings):
    for left, right, result in weighings:
        in_left = coin in left
        in_right = coin in right

        if result == "=":
            if in_left or in_right:
                return False
        elif result == "<":
            if not in_left and not in_right:
                return False
            if heavier and in_left:
                return False
            if (not heavier) and in_right:
                return False
        elif result == ">":
            if not in_left and not in_right:
                return False
            if heavier and in_right:
                return False
            if (not heavier) and in_left:
                return False
        else:
            return False
    return True


def solve(text):
    data = text.split()
    if not data:
        return ""

    t = int(data[0])
    idx = 1
    answers = []

    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2

        weighings = []
        for _ in range(k):
            p = int(data[idx])
            idx += 1
            left = list(map(int, data[idx : idx + p]))
            idx += p
            right = list(map(int, data[idx : idx + p]))
            idx += p
            result = data[idx]
            idx += 1
            weighings.append((left, right, result))

        candidates = []
        for coin in range(1, n + 1):
            if possible_with_mode(coin, True, weighings) or possible_with_mode(
                coin, False, weighings
            ):
                candidates.append(coin)

        answers.append(str(candidates[0] if len(candidates) == 1 else 0))

    return "\n\n".join(answers)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
