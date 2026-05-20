# UVA 11150 — 手打版本，處理多組輸入
import sys
from collections import deque

def min_stones(L, S, T, stones):
    if L == 0:
        return 0
    max_stone = max(stones) if stones else 0
    limit = min(L, max_stone + T)
    blocked = [0] * (limit + 1)
    for p in stones:
        if p <= limit:
            blocked[p] = 1
    INF = 10**9
    dist = [INF] * (limit + 1)
    dq = deque()
    dist[0] = 0
    dq.append(0)
    while dq:
        u = dq.popleft()
        if u + S > L:
            return dist[u]
        for step in range(S, T+1):
            v = u + step
            if v > limit:
                return dist[u]
            cost = dist[u] + (1 if blocked[v] else 0)
            if cost < dist[v]:
                dist[v] = cost
                dq.append(v)
    return 0

if __name__ == '__main__':
    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit(0)
    it = iter(data)
    while True:
        try:
            L = int(next(it))
        except StopIteration:
            break
        S = int(next(it)); T = int(next(it)); M = int(next(it))
        stones = [int(next(it)) for _ in range(M)]
        print(min_stones(L, S, T, stones))
