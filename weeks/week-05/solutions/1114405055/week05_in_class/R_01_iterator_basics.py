"""R_01 迭代器基礎（一般版）。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Iterator, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class CountDown:
    """可迭代倒數物件：for 迴圈可直接使用。"""

    start: int

    def __iter__(self) -> Iterator[int]:
        current = self.start
        while current > 0:
            yield current
            current -= 1


def manual_iter(items: Iterable[T]) -> list[T]:
    """手動使用 next() 走訪可迭代物件。"""
    out: list[T] = []
    it = iter(items)
    while True:
        try:
            out.append(next(it))
        except StopIteration:
            break
    return out


def manual_iter_default(items: Iterable[T]) -> list[T]:
    """使用 next(it, default) 的寫法，避免 try/except。"""
    out: list[T] = []
    it = iter(items)
    while True:
        item = next(it, None)
        if item is None:
            break
        out.append(item)
    return out


def iterator_demo() -> dict[str, object]:
    """整理迭代器重點結果。"""
    data = [1, 2, 3]
    it = iter(data)
    first_three = [next(it), next(it), next(it)]
    countdown_values = list(CountDown(3))
    return {
        "first_three": first_three,
        "countdown": countdown_values,
        "manual": manual_iter(["a", "b", "c"]),
        "manual_default": manual_iter_default(["a", "b", "c"]),
    }


if __name__ == "__main__":
    print(iterator_demo())
