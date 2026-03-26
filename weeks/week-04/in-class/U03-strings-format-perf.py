"""U03. 字串格式化效能與陷阱。"""

from __future__ import annotations

import timeit

PARTS = [f"item{i}" for i in range(1000)]


def bad_concat(parts: list[str] = PARTS) -> str:
    """低效示範：迴圈中反覆使用 + 串接字串。"""
    s = ""
    for p in parts:
        s += p
    return s


def good_join(parts: list[str] = PARTS) -> str:
    """高效示範：一次使用 join 完成串接。"""
    return "".join(parts)


def benchmark_concat(number: int = 500) -> tuple[float, float]:
    """回傳 bad/good 串接方式的耗時。"""
    t1 = timeit.timeit(lambda: bad_concat(PARTS), number=number)
    t2 = timeit.timeit(lambda: good_join(PARTS), number=number)
    return t1, t2


class SafeSub(dict):
    """format_map 使用：缺失鍵保留原佔位符。"""

    def __missing__(self, key: str) -> str:
        return "{" + key + "}"


def safe_format(template: str, data: dict[str, object]) -> str:
    """用 SafeSub 避免缺鍵時噴錯。"""
    return template.format_map(SafeSub(data))


def bytes_index_diff() -> tuple[str, int]:
    """示範 str 與 bytes 索引回傳差異。"""
    return "Hello"[0], b"Hello"[0]


def format_bytes(name: str, count: int) -> bytes:
    """bytes 無 format，先 format 成 str 再 encode。"""
    return "{:10s} {:5d}".format(name, count).encode("ascii")


if __name__ == "__main__":
    print(benchmark_concat())
    print(safe_format("{name} has {n} messages.", {"name": "Guido"}))
    print(bytes_index_diff())
    print(format_bytes("ACME", 100))
