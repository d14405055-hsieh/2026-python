"""U01. 字串分割與匹配陷阱。"""

from __future__ import annotations

import re


def split_with_delimiters(line: str) -> tuple[list[str], list[str], str]:
    """保留分隔符並可重建字串。"""
    fields = re.split(r"(;|,|\s)\s*", line)
    values = fields[::2]
    delimiters = fields[1::2] + [""]
    rebuilt = "".join(v + d for v, d in zip(values, delimiters))
    return values, delimiters, rebuilt


def startswith_tuple_only(url: str, choices: list[str]) -> tuple[str, bool]:
    """示範 startswith 傳 list 會失敗、tuple 才正確。"""
    try:
        url.startswith(choices)  # type: ignore[arg-type]
    except TypeError as e:
        return str(e), url.startswith(tuple(choices))
    return "", url.startswith(tuple(choices))


def normalize_spaces(s: str) -> tuple[str, str, str]:
    """回傳 strip、暴力 replace、正規化空白三種結果。"""
    stripped = s.strip()
    replaced = s.replace(" ", "")
    normalized = re.sub(r"\s+", " ", s.strip())
    return stripped, replaced, normalized


def clean_lines(lines: list[str]) -> list[str]:
    """用生成器逐行去除頭尾空白。"""
    return [line for line in (l.strip() for l in lines)]


if __name__ == "__main__":
    print(split_with_delimiters("asdf fjdk; afed, fjek,asdf, foo"))
    print(startswith_tuple_only("http://www.python.org", ["http:", "ftp:"]))
    print(normalize_spaces("  hello     world  "))
    print(clean_lines(["  apple  \n", "  banana  \n"]))
