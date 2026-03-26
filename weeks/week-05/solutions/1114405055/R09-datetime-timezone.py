"""R09. 時區操作。"""

from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones

UTC = ZoneInfo("UTC")
CENTRAL = ZoneInfo("America/Chicago")
TAIPEI = ZoneInfo("Asia/Taipei")


def convert_example() -> dict[str, datetime]:
	"""建立 Chicago 時間並轉為其他時區。"""
	d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=CENTRAL)
	return {
		"central": d,
		"kolkata": d.astimezone(ZoneInfo("Asia/Kolkata")),
		"taipei": d.astimezone(TAIPEI),
	}


def utc_best_practice() -> datetime:
	"""示範內部使用 UTC，再轉出本地時區。"""
	utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=UTC)
	return utc_dt.astimezone(CENTRAL)


def find_taipei_zones() -> list[str]:
	"""找出所有含 Taipei 關鍵字的時區。"""
	return [z for z in available_timezones() if "Taipei" in z]


if __name__ == "__main__":
	print(convert_example())
	print(datetime.now(tz=UTC))
	print(utc_best_practice())
	print(find_taipei_zones())
