# R01. 字串分割與匹配（2.1-2.3）
# 主題：re.split() / startswith() / endswith() / fnmatch()

import re
from fnmatch import fnmatch, fnmatchcase


def demo_split_with_multi_delimiters():
	"""示範如何用多種分隔符切字串。"""
	line = "asdf fjdk; afed, fjek,asdf, foo"

	print("=== 2.1 多界定符分割 ===")
	# [;,\s] 代表「分號、逗號、空白」任一種皆可當分隔符。
	# 後面的 \s* 可吸收分隔符後多餘空白，避免產生前後空格。
	tokens_1 = re.split(r"[;,\s]\s*", line)
	print("split pattern [;,\\s]\\s* ->", tokens_1)

	# (?:...) 是非捕獲分組：只做分組，不保留分隔符到結果內。
	# 若改成 (...)，re.split 會把分隔符也塞回結果陣列。
	tokens_2 = re.split(r"(?:,|;|\s)\s*", line)
	print("split non-capturing group ->", tokens_2)


def demo_startswith_endswith():
	"""示範前綴/後綴判斷與多副檔名篩選。"""
	print("\n=== 2.2 開頭/結尾匹配 ===")
	filename = "spam.txt"
	print("endswith('.txt') ->", filename.endswith(".txt"))
	print("startswith('file:') ->", filename.startswith("file:"))

	filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
	# endswith/startswith 支援 tuple 一次比對多個條件。
	c_or_h_files = [name for name in filenames if name.endswith((".c", ".h"))]
	print("C/H files ->", c_or_h_files)


def demo_fnmatch():
	"""示範 shell 風格萬用字元匹配。"""
	print("\n=== 2.3 Shell 通配符匹配 ===")
	print("fnmatch('foo.txt', '*.txt') ->", fnmatch("foo.txt", "*.txt"))
	print("fnmatch('Dat45.csv', 'Dat[0-9]*') ->", fnmatch("Dat45.csv", "Dat[0-9]*"))

	# fnmatch() 會受作業系統大小寫規則影響；fnmatchcase() 永遠區分大小寫。
	print("fnmatchcase('foo.txt', '*.TXT') ->", fnmatchcase("foo.txt", "*.TXT"))

	addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
	st_addresses = [addr for addr in addresses if fnmatchcase(addr, "* ST")]
	print("addresses end with ' ST' ->", st_addresses)


if __name__ == "__main__":
	demo_split_with_multi_delimiters()
	demo_startswith_endswith()
	demo_fnmatch()
