# U5. 優先佇列為何要加 index（1.5）

import heapq


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Item({self.name})"


pq = []

# 若只放 (priority, item)，同 priority 時會嘗試比較 item，可能 TypeError。
# 正解：放 (priority, index, item)，確保 tuple 可比較。
index = 0
for priority, name in [(2, "low"), (5, "high"), (5, "urgent"), (3, "normal")]:
    heapq.heappush(pq, (-priority, index, Item(name)))
    index += 1

while pq:
    priority, _, item = heapq.heappop(pq)
    print("pop:", -priority, item)
