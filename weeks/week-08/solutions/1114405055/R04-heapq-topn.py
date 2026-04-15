# R4: heapq Top-N

import heapq


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print("largest 3 ->", heapq.nlargest(3, nums))
print("smallest 3 ->", heapq.nsmallest(3, nums))

portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "AAPL", "shares": 50, "price": 543.22},
    {"name": "FB", "shares": 200, "price": 21.09},
]
print("cheapest ->", heapq.nsmallest(1, portfolio, key=lambda s: s["price"]))

heap = list(nums)
heapq.heapify(heap)
print("heapified ->", heap)
print("heappop ->", heapq.heappop(heap))
