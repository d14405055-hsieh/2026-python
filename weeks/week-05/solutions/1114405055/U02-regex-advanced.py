"""U02. 正則表達式進階技巧。"""

from __future__ import annotations

import re
import timeit
from calendar import month_abbr

TEXT = "Today is 11/27/2012. PyCon starts 3/13/2013."
DATE_PATTERN = re.compile(r"(\d+)/(\d+)/(\d+)")


def using_module(text: str = TEXT):
    """每次都由 re 模組解析 pattern。"""
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)


def using_compiled(text: str = TEXT):
    """使用預編譯 pattern。"""
    return DATE_PATTERN.findall(text)


def benchmark_regex(number: int = 20_000) -> tuple[float, float]:
    """回傳模組呼叫與預編譯的耗時。"""
    t1 = timeit.timeit(lambda: using_module(TEXT), number=number)
    t2 = timeit.timeit(lambda: using_compiled(TEXT), number=number)
    return t1, t2


def change_date(m: re.Match) -> str:
    """將 MM/DD/YYYY 改為 DD Mon YYYY。"""
    mon_name = month_abbr[int(m.group(1))]
    return f"{m.group(2)} {mon_name} {m.group(3)}"


def rewrite_dates(text: str = TEXT) -> str:
    """套用回呼函式替換日期。"""
    return DATE_PATTERN.sub(change_date, text)


def matchcase(word: str):
    """產生一個替換函式，保留原字大小寫風格。"""

    def replace(m: re.Match) -> str:
        t = m.group()
        if t.isupper():
            return word.upper()
        if t.islower():
            return word.lower()
        if t[0].isupper():
            return word.capitalize()
        return word

    return replace


def replace_keep_case(s: str, target: str = "python", word: str = "snake") -> str:
    """忽略大小寫替換，並保留原 token 大小寫型態。"""
    return re.sub(target, matchcase(word), s, flags=re.IGNORECASE)


if __name__ == "__main__":
    print(benchmark_regex())
    print(rewrite_dates())
    print(replace_keep_case("UPPER PYTHON, lower python, Mixed Python"))
