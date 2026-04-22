from __future__ import annotations

import sys


ROWS = [
    "`1234567890-=",
    "qwertyuiop[]\\",
    "asdfghjkl;'",
    "zxcvbnm,./",
]


def build_mapping() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for row in ROWS:
        for i in range(1, len(row)):
            right = row[i]
            left = row[i - 1]
            mapping[right] = left
            if right.isalpha():
                mapping[right.upper()] = left.upper()
    return mapping


MAP = build_mapping()


def solve(data: str) -> str:
    # AI 教學版：每個字元若在鍵盤映射中，就替換成左邊那顆鍵。
    decoded: list[str] = []
    for ch in data:
        decoded.append(MAP.get(ch, ch))
    return "".join(decoded)


if __name__ == "__main__":
    print(solve(sys.stdin.read()), end="")
