"""U_02 easy：itertools 重點版。"""

from __future__ import annotations

from itertools import combinations, islice


def itertools_easy() -> dict[str, object]:
    """只保留最常用：islice 與 combinations。"""
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    pairs = list(combinations(["a", "b", "c"], 2))
    return {"slice": list(islice(nums, 2, 6)), "pairs": pairs}


if __name__ == "__main__":
    print(itertools_easy())
