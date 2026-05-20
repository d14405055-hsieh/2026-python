# UVA 11332 — Mirrors Visible（簡易版，採角度取樣判定）
# 注意：此為取樣近似法，對某些邊界情況可能不完全精準，但易於理解與實作
import math


def seg_ray_intersection(sx,sy,ex,ey, dx,dy):
    # ray: (0,0)+t*(dx,dy), t>0
    # segment: (sx,sy)+u*(ex-sx,ey-sy), u in [0,1]
    vx = ex - sx; vy = ey - sy
    denom = dx * vy - dy * vx
    if abs(denom) < 1e-9:
        return None
    # solve for t and u
    # t*dx = sx + u*vx
    # t*dy = sy + u*vy
    # => t = (sx*vy - sy*vx) / denom
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
        # normalize to range [a1,a2] taking shortest arc
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
    segs = [(1,1,2,1), (2,2,3,2), (1,2,2,3)]
    print(visible_segments(segs))
