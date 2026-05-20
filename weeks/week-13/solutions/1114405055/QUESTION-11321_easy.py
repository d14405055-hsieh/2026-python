# UVA 11321 — 放陷阱檢查（簡易版）
# 中文註解：對於每個要放的陷阱，暫時放上去後檢查從左邊到右邊是否仍有路徑

from collections import deque


def can_reach(N, M, blocked):
    # blocked: set of (x,y)
    dq = deque()
    seen = set()
    for x in range(N):
        if (x, 0) not in blocked:
            dq.append((x,0)); seen.add((x,0))
    while dq:
        x,y = dq.popleft()
        if y == M-1:
            return True
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and (nx,ny) not in blocked and (nx,ny) not in seen:
                seen.add((nx,ny)); dq.append((nx,ny))
    return False

if __name__ == '__main__':
    N, M = 3, 10
    blocked = set()
    queries = [(1,1), (0,5), (2,9)]
    for q in queries:
        if q in blocked:
            print('>_<')
            continue
        blocked.add(q)
        if can_reach(N, M, blocked):
            print('<(_ _)>')
        else:
            blocked.remove(q)
            print('>_<')
