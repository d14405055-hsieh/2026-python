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


def side_sum(s):
    return sum(int(x) for x in re.findall(r"[+-]?\d+", s))


def valid(eq):
    l, r = eq.split("=")
    return side_sum(l) == side_sum(r)


def main():
    src = sys.stdin.read()
    if "#" not in src:
        return
    expr = src.split("#", 1)[0]
    ch = list(expr)
    pos = [i for i, c in enumerate(ch) if c.isdigit()]

    add = {d: [] for d in range(10)}
    rem = {d: [] for d in range(10)}
    mov = {d: [] for d in range(10)}

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
                mov[a].append(b)

    for i in pos:
        d = ord(ch[i]) - 48
        for nd in mov[d]:
            oi = ch[i]
            ch[i] = str(nd)
            s = "".join(ch)
            if valid(s):
                print(s + "#")
                return
            ch[i] = oi

    for i in pos:
        d1 = ord(ch[i]) - 48
        for nd1 in rem[d1]:
            oi = ch[i]
            ch[i] = str(nd1)
            for j in pos:
                if j == i:
                    continue
                d2 = ord(ch[j]) - 48
                for nd2 in add[d2]:
                    oj = ch[j]
                    ch[j] = str(nd2)
                    s = "".join(ch)
                    if valid(s):
                        print(s + "#")
                        return
                    ch[j] = oj
            ch[i] = oi

    print("No")


if __name__ == "__main__":
    main()
