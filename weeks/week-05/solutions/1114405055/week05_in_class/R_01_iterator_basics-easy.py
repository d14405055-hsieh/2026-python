"""R_01 easy：迭代器重點版。"""

from __future__ import annotations


def iterator_easy(items: list[int]) -> dict[str, object]:
    """記憶重點：iter 產生迭代器、next 逐個取值。"""
    it = iter(items)
    taken: list[int] = []
    while True:
        value = next(it, None)
        if value is None:
            break
        taken.append(value)
    return {"taken": taken, "count": len(taken)}


if __name__ == "__main__":
    print(iterator_easy([1, 2, 3]))
