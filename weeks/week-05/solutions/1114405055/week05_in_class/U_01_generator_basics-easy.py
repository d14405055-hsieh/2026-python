"""U_01 easy：生成器重點版。"""

from __future__ import annotations


def countdown(n: int):
    """每次 yield 一個值，直到 1。"""
    while n > 0:
        yield n
        n -= 1


def generator_easy() -> list[int]:
    """直接把生成器轉 list 觀察結果。"""
    return list(countdown(3))


if __name__ == "__main__":
    print(generator_easy())
