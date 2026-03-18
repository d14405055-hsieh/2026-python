"""UVA 10008 - What's Cryptanalysis?"""

from __future__ import annotations

from collections import Counter
import sys
from typing import List, Tuple


def count_letters(lines: List[str]) -> List[Tuple[str, int]]:
    """統計 A~Z（不分大小寫）的出現次數並排序。"""
    counter: Counter[str] = Counter()
    for line in lines:
        for ch in line.upper():
            if "A" <= ch <= "Z":
                counter[ch] += 1

    return sorted(counter.items(), key=lambda item: (-item[1], item[0]))


def solve(data: str) -> str:
    raw_lines = data.splitlines()
    if not raw_lines:
        return ""

    n = int(raw_lines[0].strip() or "0")
    lines = raw_lines[1 : 1 + n]
    result = count_letters(lines)
    return "\n".join(f"{ch} {cnt}" for ch, cnt in result)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
