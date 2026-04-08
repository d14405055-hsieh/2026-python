import re
import sys


SEG = {
    0: 0b1111110,
    1: 0b0110000,
    2: 0b1101101,
    3: 0b1111001,
    4: 0b0110011,
    5: 0b1011011,
    6: 0b1011111,
    7: 0b1110000,
    8: 0b1111111,
    9: 0b1111011,
}


def parse_side(side):
    nums = re.findall(r"[+-]?\d+", side)
    total = 0
    for x in nums:
        total += int(x)
    return total


def is_ok(eq):
    left, right = eq.split("=")
    return parse_side(left) == parse_side(right)


def solve():
    line = sys.stdin.read()
    if "#" not in line:
        return
    expr = line.split("#", 1)[0]
    chars = list(expr)

    digits_pos = [i for i, ch in enumerate(chars) if ch.isdigit()]

    add = {d: [] for d in range(10)}
    rem = {d: [] for d in range(10)}
    same_move = {d: [] for d in range(10)}

    for a in range(10):
        ma = SEG[a]
        ca = ma.bit_count()
        for b in range(10):
            mb = SEG[b]
            cb = mb.bit_count()
            x = ma ^ mb
            if cb == ca + 1 and (mb & ma) == ma and x.bit_count() == 1:
                add[a].append(b)
            if cb == ca - 1 and (mb | ma) == ma and x.bit_count() == 1:
                rem[a].append(b)
            if cb == ca and x.bit_count() == 2:
                same_move[a].append(b)

    # 情況一：同一個數字內移動一根木棒
    for i in digits_pos:
        d = ord(chars[i]) - ord("0")
        for nd in same_move[d]:
            old = chars[i]
            chars[i] = str(nd)
            cand = "".join(chars)
            if is_ok(cand):
                print(cand + "#")
                return
            chars[i] = old

    # 情況二：從一個數字拆一根，補到另一個數字
    for i in digits_pos:
        di = ord(chars[i]) - ord("0")
        for ndi in rem[di]:
            old_i = chars[i]
            chars[i] = str(ndi)
            for j in digits_pos:
                if j == i:
                    continue
                dj = ord(chars[j]) - ord("0")
                for ndj in add[dj]:
                    old_j = chars[j]
                    chars[j] = str(ndj)
                    cand = "".join(chars)
                    if is_ok(cand):
                        print(cand + "#")
                        return
                    chars[j] = old_j
            chars[i] = old_i

    print("No")


if __name__ == "__main__":
    solve()
