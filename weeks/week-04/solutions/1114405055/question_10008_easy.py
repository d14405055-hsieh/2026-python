"""UVA 10008 簡單版：用陣列直接計數。"""

import sys


def solve(text):
    lines = text.splitlines()
    if not lines:
        return ""

    n = int(lines[0].strip() or "0")
    cnt = [0] * 26

    for i in range(1, min(n + 1, len(lines))):
        for ch in lines[i].upper():
            if "A" <= ch <= "Z":
                cnt[ord(ch) - ord("A")] += 1

    items = []
    for i in range(26):
        if cnt[i] > 0:
            items.append((chr(ord("A") + i), cnt[i]))

    items.sort(key=lambda x: (-x[1], x[0]))
    return "\n".join(f"{ch} {num}" for ch, num in items)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
