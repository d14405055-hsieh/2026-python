# R20. ChainMap 合併映射（1.20）

from collections import ChainMap

a = {"x": 1, "z": 3}
b = {"y": 2, "z": 4}
combined = ChainMap(a, b)

print("x:", combined["x"])
print("y:", combined["y"])

# key 重複時，會先讀取前面的 mapping。
print("z from first mapping:", combined["z"])

# 寫入會寫到第一個 mapping。
combined["w"] = 100
print("a after write:", a)
print("b unchanged:", b)
