# R8: Dict min/max/sorted with zip

prices = {"ACME": 45.23, "AAPL": 612.78, "FB": 10.75}

print("min by value (zip) ->", min(zip(prices.values(), prices.keys())))
print("max by value (zip) ->", max(zip(prices.values(), prices.keys())))
print("sorted by value (zip) ->", sorted(zip(prices.values(), prices.keys())))

min_key = min(prices, key=lambda k: prices[k])
max_key = max(prices, key=lambda k: prices[k])
print("min key ->", min_key, prices[min_key])
print("max key ->", max_key, prices[max_key])
