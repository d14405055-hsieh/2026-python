# UVA 11332 — 手寫版本（取樣判定）
import sys
from QUESTION_11332_easy import visible_segments

if __name__ == '__main__':
    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit(0)
    it = iter(data)
    n = int(next(it))
    segs = []
    for _ in range(n):
        sx = int(next(it)); sy = int(next(it)); ex = int(next(it)); ey = int(next(it))
        segs.append((sx,sy,ex,ey))
    vis = visible_segments(segs, samples_per_seg=40)
    print(' '.join(map(str, vis)))
