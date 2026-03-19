# U1. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）

p = (4, 5)

# 正確：左邊兩個變數，右邊兩個元素。
x, y = p
print("x, y:", x, y)

# 錯誤示範：元素只有 2 個，但左邊要 3 個。
try:
    x, y, z = p
except ValueError as exc:
    print("unpack error:", exc)
