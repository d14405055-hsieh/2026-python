import sys


def carry_count(a, b):
    c = 0
    carry = 0
    while a > 0 or b > 0:
        s = (a % 10) + (b % 10) + carry
        if s >= 10:
            c += 1
            carry = 1
        else:
            carry = 0
        a //= 10
        b //= 10
    return c


def to_msg(c):
    if c == 0:
        return "No carry operation."
    if c == 1:
        return "1 carry operation."
    return f"{c} carry operations."


def solve(text):
    data = text.split()
    out = []

    for i in range(0, len(data), 2):
        a = int(data[i])
        b = int(data[i + 1])
        if a == 0 and b == 0:
            break
        out.append(to_msg(carry_count(a, b)))

    return "\n".join(out)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
