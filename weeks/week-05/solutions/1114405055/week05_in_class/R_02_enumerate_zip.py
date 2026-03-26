"""R_02 enumerate / zip（一般版）。"""

from __future__ import annotations

from itertools import zip_longest


def enumerate_colors(colors: list[str], start: int = 0) -> list[tuple[int, str]]:
    """回傳 enumerate 結果。"""
    return list(enumerate(colors, start))


def zip_names_scores(names: list[str], scores: list[int]) -> list[tuple[str, int]]:
    """基本 zip 配對。"""
    return list(zip(names, scores))


def zip_with_padding(x: list[object], y: list[object], fill: object = 0) -> list[tuple[object, object]]:
    """長度不同時，用 zip_longest 補值。"""
    return list(zip_longest(x, y, fillvalue=fill))


def build_dict(keys: list[str], values: list[str]) -> dict[str, str]:
    """用 zip 建立字典。"""
    return dict(zip(keys, values))


if __name__ == "__main__":
    print(enumerate_colors(["red", "green", "blue"], start=1))
    print(zip_names_scores(["Alice", "Bob"], [90, 85]))
    print(zip_with_padding([1, 2], ["a", "b", "c"]))
    print(build_dict(["name", "age"], ["John", "30"]))
