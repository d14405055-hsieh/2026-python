"""R04. 位元組字串操作。

本檔將原本教學示範改為可測試函式，方便搭配 unit test 使用。
"""

from __future__ import annotations

import re


def slice_head(data: bytes) -> bytes:
	"""回傳前五個位元組。"""
	return data[0:5]


def split_bytes_pattern(raw: bytes) -> list[bytes]:
	"""使用 bytes 正則分割。"""
	return re.split(rb"[:,]", raw)


def first_items() -> tuple[str, int]:
	"""回傳字串與 bytes 的第一個元素，展示型別差異。"""
	a = "Hello"
	b = b"Hello"
	return a[0], b[0]


def format_then_encode(name: str, amount: int) -> bytes:
	"""先做字串格式化，再用 ASCII 編碼成 bytes。"""
	return "{:10s} {:10d}".format(name, amount).encode("ascii")


def demo() -> dict[str, object]:
	"""集中回傳示範結果，方便測試與 CLI 顯示。"""
	data = b"Hello World"
	return {
		"slice": slice_head(data),
		"startswith": data.startswith(b"Hello"),
		"split": data.split(),
		"replace": data.replace(b"Hello", b"Hello Cruel"),
		"regex_split": split_bytes_pattern(b"FOO:BAR,SPAM"),
		"first_items": first_items(),
		"formatted": format_then_encode("ACME", 100),
	}


if __name__ == "__main__":
	for key, value in demo().items():
		print(f"{key}: {value}")
