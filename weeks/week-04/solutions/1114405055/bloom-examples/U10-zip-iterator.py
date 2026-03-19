# U10. zip 為何只能用一次（1.8）

prices = {"A": 2.0, "B": 1.0, "C": 4.5}
zipped = zip(prices.values(), prices.keys())

# 第一次消耗 zipped。
print("min pair:", min(zipped))

# 這時 zipped 已經空了，不能再拿 max。
try:
    print("max pair:", max(zipped))
except ValueError as exc:
    print("second use failed:", exc)

# 若要多次使用，應該先 materialize。
pairs = list(zip(prices.values(), prices.keys()))
print("reuse min/max:", min(pairs), max(pairs))
