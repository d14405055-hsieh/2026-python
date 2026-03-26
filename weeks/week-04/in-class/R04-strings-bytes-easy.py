"""R04 easy：位元組字串重點速記版。"""

from __future__ import annotations

import re


def bytes_basics() -> dict[str, object]:
    """最常考的 bytes 操作，集中放一起方便記憶。

    1) 切片與 split 跟字串很像。
    2) bytes 索引回傳 int，不是字元。
    3) 正則處理 bytes 時，pattern 也要用 bytes（rb"..."）。
    """
    data = b"Hello World"
    return {
        "slice": data[:5],
        "split": data.split(),
        "first_int": data[0],
        "regex_split": re.split(rb"[:,]", b"FOO:BAR,SPAM"),
        "formatted": "{:10s} {:10d}".format("ACME", 100).encode("ascii"),
    }


if __name__ == "__main__":
    print(bytes_basics())
