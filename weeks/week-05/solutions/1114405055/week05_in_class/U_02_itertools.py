"""U_02 itertools 工具（一般版）。"""

from __future__ import annotations

from itertools import chain, combinations, combinations_with_replacement, dropwhile, islice, permutations, takewhile
from typing import Iterator


def count_from(n: int) -> Iterator[int]:
    """無窮計數器。"""
    i = n
    while True:
        yield i
        i += 1


def itertools_demo() -> dict[str, object]:
    """集中回傳常見 itertools 範例結果。"""
    nums = [1, 3, 5, 2, 4, 6]
    items = ["a", "b", "c"]
    return {
        "islice": list(islice(count_from(0), 5, 10)),
        "dropwhile": list(dropwhile(lambda x: x < 5, nums)),
        "takewhile": list(takewhile(lambda x: x < 5, nums)),
        "chain": list(chain([1, 2], [3, 4], [5])),
        "permutations_2": list(permutations(items, 2)),
        "combinations_2": list(combinations(items, 2)),
        "combinations_with_replacement_2": list(combinations_with_replacement(items, 2)),
    }


if __name__ == "__main__":
    print(itertools_demo())
