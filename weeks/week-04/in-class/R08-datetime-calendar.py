"""R08. 日期範圍與字串轉換。"""

from __future__ import annotations

from calendar import monthrange
from datetime import date, datetime, timedelta


def get_month_range(start: date | None = None) -> tuple[date, date]:
    """回傳該月起日與下個月起日（右開區間）。"""
    if start is None:
        start = date.today().replace(day=1)
    _, days = monthrange(start.year, start.month)
    return start, start + timedelta(days=days)


def date_range(start: datetime, stop: datetime, step: timedelta):
    """產生 [start, stop) 的日期時間序列。"""
    while start < stop:
        yield start
        start += step


def parse_ymd(s: str) -> datetime:
    """手動解析 YYYY-MM-DD，避免 strptime 較高成本。"""
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


def datetime_parse_and_format(text: str) -> tuple[datetime, str]:
    """示範字串轉 datetime 與格式化輸出。"""
    dt = datetime.strptime(text, "%Y-%m-%d")
    return dt, datetime.strftime(dt, "%A %B %d, %Y")


if __name__ == "__main__":
    first, last = get_month_range(date(2012, 8, 1))
    print(first, "~", last - timedelta(days=1))
    for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)):
        print(d)
    print(datetime_parse_and_format("2012-09-20"))
    print(parse_ymd("2012-09-20"))
