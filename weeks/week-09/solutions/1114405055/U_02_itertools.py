# Understand（理解）- itertools 工具函數

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")


def count(n):
    i = n
    while True:
        yield i
        i += 1


c = count(0)
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
nums = [1, 3, 5, 2, 4, 6]
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
a = [1, 2]
b = [3, 4]
c = [5]
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")
items = ["a", "b", "c"]
print(f"permutations(items):")
for p in permutations(items):
    print(f"  {p}")

print(f"permutations(items, 2):")
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
print(f"combinations(items, 2):")
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
chars = ["A", "B", "1"]
print("2位數密碼:")
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
from itertools import combinations_with_replacement

for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")


# =========================
# 手打版（詳細中文註解）
# 位置：本檔案最下方
# =========================

# 從 itertools 匯入常見工具：
# - islice: 針對「可迭代物件」做切片（特別適合生成器）
# - dropwhile: 前段符合條件就持續丟棄，直到第一次不符合才開始保留
# - takewhile: 前段符合條件就持續保留，遇到第一次不符合就立刻停止
# - chain: 把多個可迭代物件串接成單一序列
# - permutations: 產生排列（順序不同視為不同結果）
# - combinations: 產生組合（順序不同視為相同結果）
from itertools import (
    islice,
    dropwhile,
    takewhile,
    chain,
    permutations,
    combinations,
    combinations_with_replacement,
)

print("\n\n=== 手打版：itertools 詳解 ===")
print("--- islice() 切片 ---")


def count_handwrite(n):
    # 這是一個「無限生成器」：
    # 從 n 開始，每次 yield 當前值，然後加 1，永遠不會自己結束。
    # 這類生成器不能直接轉成 list，否則會無限執行。
    i = n
    while True:
        yield i
        i += 1


# 建立從 0 開始的無限序列：0, 1, 2, 3, ...
counter = count_handwrite(0)
# islice(counter, 5, 10) 表示：
# 1. 跳過前 5 個元素（索引 0~4）
# 2. 取索引 5~9（共 5 個）
# 所以結果會是 [5, 6, 7, 8, 9]
result = list(islice(counter, 5, 10))
print(f"islice(counter, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
nums_handwrite = [1, 3, 5, 2, 4, 6]
# dropwhile(lambda x: x < 5, nums_handwrite) 的規則：
# 1. 從頭開始檢查，每個元素只要 < 5 就繼續丟棄
# 2. 一旦遇到第一個不滿足條件的元素（這裡是 5），就停止丟棄
# 3. 後面所有元素都原樣保留，不再套用條件
# 所以結果是 [5, 2, 4, 6]
result = list(dropwhile(lambda x: x < 5, nums_handwrite))
print(f"dropwhile(x<5, {nums_handwrite}): {result}")

print("\n--- takewhile() 條件取用 ---")
# takewhile(lambda x: x < 5, nums_handwrite) 的規則：
# 1. 從頭開始取值，只要元素 < 5 就持續保留
# 2. 一旦遇到第一個不符合條件的元素（這裡是 5），立即停止
# 3. 後面的元素完全不看
# 所以結果只會是前綴 [1, 3]
result = list(takewhile(lambda x: x < 5, nums_handwrite))
print(f"takewhile(x<5, {nums_handwrite}): {result}")

print("\n--- chain() 串聯 ---")
a_handwrite = [1, 2]
b_handwrite = [3, 4]
c_handwrite = [5]
# chain(a_handwrite, b_handwrite, c_handwrite) 會依序把三個序列接起來
# 可以把多個資料來源視為同一條序列來走訪
print(f"chain(a, b, c): {list(chain(a_handwrite, b_handwrite, c_handwrite))}")

print("\n--- permutations() 排列 ---")
items_handwrite = ["a", "b", "c"]
print("permutations(items_handwrite):")
# permutations(items_handwrite) 預設長度 r = len(items_handwrite)
# 會列出所有全排列，總數是 3! = 6
for p in permutations(items_handwrite):
    print(f"  {p}")

print("permutations(items_handwrite, 2):")
# permutations(items_handwrite, 2) 代表從 3 個元素中排出長度 2 的有序結果
# 計算數量為 P(3,2) = 3 * 2 = 6
for p in permutations(items_handwrite, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
print("combinations(items_handwrite, 2):")
# combinations(items_handwrite, 2) 與排列差異在於「不看順序」
# 所以 ('a','b') 和 ('b','a') 視為同一組，總數 C(3,2)=3
for combo in combinations(items_handwrite, 2):
    print(f"  {combo}")

print("\n--- 組合應用：密碼窮舉 ---")
chars_handwrite = ["A", "B", "1"]
print("2位數密碼（不重複）:")
# permutations(chars_handwrite, 2) 產生不重複字元的 2 位密碼
# 例如：AB、A1、BA、B1、1A、1B
for p in permutations(chars_handwrite, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
# combinations_with_replacement(chars_handwrite, 2) 允許重複取值
# 例如：AA、BB、11 會出現；但因為是組合概念，不看順序
# 所以 AB 和 BA 只會保留一種表示方式
for p in combinations_with_replacement(chars_handwrite, 2):
    print(f"  {''.join(p)}")
