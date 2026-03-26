"""U_01 生成器基礎（一般版）。"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Iterator


def frange(start: float, stop: float, step: float) -> Iterator[float]:
    """浮點版 range，逐步 yield。"""
    x = start
    while x < stop:
        yield x
        x += step


def fibonacci() -> Iterator[int]:
    """無窮 Fibonacci 生成器。"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def chain_iter(*iterables: Iterable[int]) -> Iterator[int]:
    """用 yield from 串接多個 iterable。"""
    for it in iterables:
        yield from it


@dataclass
class Node:
    """用於示範樹狀 depth-first 走訪。"""

    value: int
    children: list["Node"] = field(default_factory=list)

    def add_child(self, node: "Node") -> None:
        self.children.append(node)

    def depth_first(self) -> Iterator["Node"]:
        yield self
        for child in self.children:
            yield from child.depth_first()


def flatten(items: Iterable[object]) -> Iterator[object]:
    """遞迴攤平巢狀可迭代結構，字串視為原子值。"""
    for x in items:
        if hasattr(x, "__iter__") and not isinstance(x, (str, bytes)):
            yield from flatten(x)  # type: ignore[arg-type]
        else:
            yield x


if __name__ == "__main__":
    print(list(frange(0, 2, 0.5)))
    fib = fibonacci()
    print([next(fib) for _ in range(10)])
    print(list(chain_iter([1, 2], [3, 4], [5, 6])))
    root = Node(0)
    root.add_child(Node(1))
    root.add_child(Node(2))
    root.children[0].add_child(Node(3))
    print([node.value for node in root.depth_first()])
    print(list(flatten([1, [2, [3, 4]], 5])))
