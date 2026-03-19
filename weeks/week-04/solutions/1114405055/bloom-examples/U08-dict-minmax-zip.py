# U8. 字典最值為何常用 zip(values, keys)（1.8）

prices = {"A": 2.0, "B": 1.0, "C": 4.5}

# 直接 min(prices) 是比 key。
print("min key:", min(prices))

# min(prices.values()) 雖拿到最小 value，但不知道是哪個 key。
print("min value only:", min(prices.values()))

# zip(value, key) 可同時帶出數值與對應 key。
min_pair = min(zip(prices.values(), prices.keys()))
max_pair = max(zip(prices.values(), prices.keys()))
print("min pair(value, key):", min_pair)
print("max pair(value, key):", max_pair)
