# QUESTION-11332 — Mirrors Visible 主程式（整合 helper）
import sys
import math

def angle_between(x1,y1,x2,y2):
    a1 = math.atan2(y1,x1); a2 = math.atan2(y2,x2)
    return a2 - a1

def seg_ray_intersection(sx,sy,ex,ey, dx,dy):
    vx = ex - sx; vy = ey - sy
    denom = dx * vy - dy * vx
    if abs(denom) < 1e-9:
        return None
    t = (sx * vy - sy * vx) / denom
    u = None
    if abs(vx) > abs(vy):
        u = (t*dx - sx) / vx if abs(vx) > 1e-9 else None
    else:
        u = (t*dy - sy) / vy if abs(vy) > 1e-9 else None
    if t is not None and t > 1e-9 and u is not None and -1e-9 <= u <= 1+1e-9:
        return t
    return None

def visible_segments(segments, samples_per_seg=30):
    n = len(segments)
    vis = [0]*n
    for i,(sx,sy,ex,ey) in enumerate(segments):
        a1 = math.atan2(sy, sx)
        a2 = math.atan2(ey, ex)
        da = a2 - a1
        if da <= -math.pi:
            da += 2*math.pi
        elif da > math.pi:
            da -= 2*math.pi
        for k in range(samples_per_seg+1):
            theta = a1 + da * (k / samples_per_seg)
            dx = math.cos(theta); dy = math.sin(theta)
            tcur = seg_ray_intersection(sx,sy,ex,ey, dx,dy)
            if tcur is None:
                continue
            blocked = False
            for j,(ox,oy,px,qy) in enumerate(segments):
                if j == i: continue
                tj = seg_ray_intersection(ox,oy,px,qy, dx,dy)
                if tj is not None and tj < tcur - 1e-9:
                    blocked = True; break
            if not blocked:
                vis[i] = 1
                break
    return vis

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
