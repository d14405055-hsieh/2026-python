import sys


EPS = 1e-12


def union_len(segs):
    if not segs:
        return 0.0
    segs.sort()
    s = 0.0
    l, r = segs[0]
    for nl, nr in segs[1:]:
        if nl <= r:
            if nr > r:
                r = nr
        else:
            s += r - l
            l, r = nl, nr
    s += r - l
    return s


def cover_at(x0, vv, ll, t):
    segs = []
    for i in range(len(x0)):
        l = x0[i] + vv[i] * t
        segs.append((l, l + ll[i]))
    return union_len(segs)


def integral_piece(x0, vv, ll, dt):
    pts = [0.0, dt]
    ep = []
    for i in range(len(x0)):
        ep.append((x0[i], vv[i]))
        ep.append((x0[i] + ll[i], vv[i]))

    m = len(ep)
    for i in range(m):
        a1, s1 = ep[i]
        for j in range(i + 1, m):
            a2, s2 = ep[j]
            d = s1 - s2
            if abs(d) < EPS:
                continue
            t = (a2 - a1) / d
            if EPS < t < dt - EPS:
                pts.append(t)

    pts = sorted(set(round(x, 12) for x in pts))
    area = 0.0
    for i in range(len(pts) - 1):
        a = pts[i]
        b = pts[i + 1]
        fa = cover_at(x0, vv, ll, a)
        fb = cover_at(x0, vv, ll, b)
        area += (fa + fb) * (b - a) * 0.5
    return area


def solve(data: str) -> str:
    arr = list(map(int, data.split()))
    n, w, tlim, rain = arr[:4]
    x = []
    ll = []
    vv = []
    p = 4
    for _ in range(n):
        x.append(float(arr[p]))
        ll.append(float(arr[p + 1]))
        vv.append(float(arr[p + 2]))
        p += 3

    t = 0.0
    covered = 0.0
    w = float(w)
    tlim = float(tlim)
    rain = float(rain)

    while t < tlim - EPS:
        dt = tlim - t
        for i in range(n):
            if abs(vv[i]) < EPS:
                continue
            if vv[i] > 0:
                hit = (w - ll[i] - x[i]) / vv[i]
            else:
                hit = (0.0 - x[i]) / vv[i]
            if hit > EPS and hit < dt:
                dt = hit

        covered += integral_piece(x, vv, ll, dt)

        for i in range(n):
            x[i] += vv[i] * dt
            rb = w - ll[i]
            if abs(x[i]) < 1e-10:
                x[i] = 0.0
            if abs(x[i] - rb) < 1e-10:
                x[i] = rb

        t += dt

        for i in range(n):
            rb = w - ll[i]
            if abs(x[i]) < 1e-9 and vv[i] < 0:
                vv[i] = -vv[i]
            elif abs(x[i] - rb) < 1e-9 and vv[i] > 0:
                vv[i] = -vv[i]

    ans = (w * tlim - covered) * rain
    return f"{ans:.2f}"


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
