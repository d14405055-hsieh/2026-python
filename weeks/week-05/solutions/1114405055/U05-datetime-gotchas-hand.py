"""U05 easy：日期時間陷阱速記版。"""

from __future__ import annotations

import calendar
from datetime import datetime


def add_one_month(dt: datetime) -> datetime:
    """加一個月，月底自動向下夾住。"""
    year = dt.year + (1 if dt.month == 12 else 0)
    month = 1 if dt.month == 12 else dt.month + 1
    last_day = calendar.monthrange(year, month)[1]
    return dt.replace(year=year, month=month, day=min(dt.day, last_day))


def datetime_gotchas_easy() -> dict[str, object]:
    """最常考：1/31 +1 月會落在 2/29 或 2/28。"""
    return {
        "jan31_plus1": add_one_month(datetime(2012, 1, 31)),
        "sep23_plus1": add_one_month(datetime(2012, 9, 23)),
    }


if __name__ == "__main__":
    print(datetime_gotchas_easy())
