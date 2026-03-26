"""U06. 時區操作最佳實踐：UTC 優先。"""

from __future__ import annotations

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

UTC = ZoneInfo("UTC")
CENTRAL = ZoneInfo("America/Chicago")
TAIPEI = ZoneInfo("Asia/Taipei")


def dst_boundary_demo() -> tuple[datetime, datetime]:
	"""示範夏令時邊界：直接本地加減 vs 轉 UTC 後計算。"""
	local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=CENTRAL)
	wrong = local_dt + timedelta(minutes=30)
	correct = (local_dt.astimezone(UTC) + timedelta(minutes=30)).astimezone(CENTRAL)
	return wrong, correct


def parse_store_utc_and_display(user_input: str) -> tuple[datetime, datetime]:
	"""輸入本地時間，儲存成 UTC，最後轉台北顯示。"""
	naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
	utc_value = naive.replace(tzinfo=CENTRAL).astimezone(UTC)
	taipei_value = utc_value.astimezone(TAIPEI)
	return utc_value, taipei_value


if __name__ == "__main__":
	print(dst_boundary_demo())
	print(parse_store_utc_and_display("2012-12-21 09:30:00"))
