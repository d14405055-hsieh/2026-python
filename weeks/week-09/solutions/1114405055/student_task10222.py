from __future__ import annotations

import sys


KEYBOARD_ROWS = [
    "`1234567890-=",
    "qwertyuiop[]\\",
    "asdfghjkl;'",
    "zxcvbnm,./",
]


def make_table() -> dict[str, str]:
    table: dict[str, str] = {}
    for row in KEYBOARD_ROWS:
        for i in range(1, len(row)):
            table[row[i]] = row[i - 1]
            if row[i].isalpha():
                table[row[i].upper()] = row[i - 1].upper()
    return table


TRANS = make_table()


def solve(data: str) -> str:
    result_chars = [TRANS.get(ch, ch) for ch in data]
    return "".join(result_chars)


if __name__ == "__main__":
    print(solve(sys.stdin.read()), end="")
