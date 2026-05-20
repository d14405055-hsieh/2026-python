# UVA 11150 — Frog on the Log（簡易版）
# 簡單做法：把 L 限制到 max(stones)+T，之後用 BFS 或 DP 計算踩到石子的最少數量

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
    print(min_stones(10, 2, 3, [2,6]))
