# R04. 位元組字串操作（2.20）
# 主題：bytes / bytearray 的常見操作與和 str 的差異

import re


def demo_bytes_basics():
	"""bytes 基本切片、搜尋、替換。"""
	data = b"Hello World"
	print("=== bytes 基本操作 ===")
	print("slice [0:5] ->", data[0:5])
	print("startswith(b'Hello') ->", data.startswith(b"Hello"))
	print("split() ->", data.split())
	print("replace() ->", data.replace(b"Hello", b"Hello Cruel"))


def demo_regex_on_bytes():
	"""bytes 與正則：pattern 必須也用 bytes。"""
	raw = b"FOO:BAR,SPAM"
	print("\n=== bytes + regex ===")
	# 字串用 r"..."，位元組字串用 rb"..."。
	print("re.split(rb'[:,]', raw) ->", re.split(rb"[:,]", raw))


def demo_str_vs_bytes_index():
	"""str 與 bytes 在索引結果上的關鍵差異。"""
	text = "Hello"
	byte_text = b"Hello"
	print("\n=== str 與 bytes 索引差異 ===")
	print("text[0] ->", repr(text[0]))
	print("byte_text[0] ->", byte_text[0], "(整數，等於 ord('H'))")


def demo_encoding_boundary():
	"""字串格式化後轉 bytes 的典型流程。"""
	print("\n=== format 與 encode ===")
	# str.format 的輸出型態仍是 str，若要網路傳輸/寫二進位檔再 encode。
	formatted_str = "{:10s} {:10d}".format("ACME", 100)
	formatted_bytes = formatted_str.encode("ascii")
	print("formatted str ->", formatted_str)
	print("encoded bytes ->", formatted_bytes)


def demo_bytearray_mutable():
	"""bytearray 可就地修改，適合需要原地更新資料的情境。"""
	print("\n=== bytearray 可變操作 ===")
	ba = bytearray(b"hello")
	ba[0] = ord("H")
	print("after index assignment ->", ba)
	ba.append(ord("!"))
	print("after append ->", ba)


if __name__ == "__main__":
	demo_bytes_basics()
	demo_regex_on_bytes()
	demo_str_vs_bytes_index()
	demo_encoding_boundary()
	demo_bytearray_mutable()
