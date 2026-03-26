"""U02 easy：正則進階速記版。"""

from __future__ import annotations

import re
from calendar import month_abbr

DATE_PATTERN = re.compile(r"(\d+)/(\d+)/(\d+)")


def change_date(m: re.Match) -> str:
    """MM/DD/YYYY -> DD Mon YYYY。"""
    return f"{m.group(2)} {month_abbr[int(m.group(1))]} {m.group(3)}"


def regex_advanced(text: str) -> str:
    """最常見考法：sub + callback。"""
    return DATE_PATTERN.sub(change_date, text)


if __name__ == "__main__":
    print(regex_advanced("Today is 11/27/2012."))
