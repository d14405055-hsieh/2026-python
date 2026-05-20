# UVA 11321 — 手打版本，逐筆處理陷阱放置要求
import sys
from collections import deque


def can_reach(N, M, blocked):
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
    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit(0)
    it = iter(data)
    N = int(next(it)); M = int(next(it)); T = int(next(it))
    blocked = set()
    for _ in range(T):
        x = int(next(it)); y = int(next(it))
        if (x,y) in blocked:
            print('>_<')
            continue
        blocked.add((x,y))
        if can_reach(N, M, blocked):
            print('<(_ _)>')
        else:
            blocked.remove((x,y))
            print('>_<')
