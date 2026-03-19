# U4. heap 為何能高效拿 Top-N（1.4）

import heapq

nums = [5, 1, 9, 2, 7]
h = nums[:]
heapq.heapify(h)

# 核心性質：h[0] 永遠是最小值。
print("heap internal:", h)
print("smallest now:", h[0])

# 持續 pop，會依小到大取出。
ordered = []
while h:
    ordered.append(heapq.heappop(h))
print("pop order:", ordered)

# 直接拿 Top-N：nsmallest / nlargest。
print("2 smallest:", heapq.nsmallest(2, nums))
print("2 largest:", heapq.nlargest(2, nums))
