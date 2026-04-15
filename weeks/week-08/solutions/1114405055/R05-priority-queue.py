# R5: Implement a simple priority queue

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


pq = PriorityQueue()
pq.push("low", 1)
pq.push("high", 5)
pq.push("medium", 3)

print("pop #1 ->", pq.pop())
print("pop #2 ->", pq.pop())
print("pop #3 ->", pq.pop())
