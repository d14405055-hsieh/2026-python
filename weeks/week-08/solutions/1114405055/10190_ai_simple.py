"""題號 10190（依 week-08 題目敘述）：自動傘降雨量計算（AI 簡單版，含中文註解）"""

import sys


EPS = 1e-12


def union_length(intervals):
    """計算多個區間的聯集長度。"""
    if not intervals:
        return 0.0
    intervals = sorted(intervals)
    total = 0.0
    cur_l, cur_r = intervals[0]
    for l, r in intervals[1:]:
        if l <= cur_r:
            if r > cur_r:
                cur_r = r
        else:
            total += cur_r - cur_l
            cur_l, cur_r = l, r
    total += cur_r - cur_l
    return total


def covered_len_at(x0, v, lens, t):
    intervals = []
    for i in range(len(x0)):
        l = x0[i] + v[i] * t
        r = l + lens[i]
        intervals.append((l, r))
    return union_length(intervals)


def covered_integral_piece(x0, v, lens, dt):
    """在速度固定且不反彈的 dt 內，精確積分覆蓋長度。"""
    k = len(x0)
    events = [0.0, dt]

    # 收集所有端點相交時刻，確保區間排序變化都被切開
    endpoints_a = []
    for i in range(k):
        endpoints_a.append((x0[i], v[i]))
        endpoints_a.append((x0[i] + lens[i], v[i]))

    m = len(endpoints_a)
    for i in range(m):
        a1, s1 = endpoints_a[i]
        for j in range(i + 1, m):
            a2, s2 = endpoints_a[j]
            ds = s1 - s2
            if abs(ds) < EPS:
                continue
            t = (a2 - a1) / ds
            if EPS < t < dt - EPS:
                events.append(t)

    events = sorted(set(round(x, 12) for x in events))

    integral = 0.0
    for i in range(len(events) - 1):
        ta = events[i]
        tb = events[i + 1]
        fa = covered_len_at(x0, v, lens, ta)
        fb = covered_len_at(x0, v, lens, tb)
        integral += (fa + fb) * 0.5 * (tb - ta)
    return integral


def solve_one_case(n, w, t_limit, rain_v, umbrellas):
    x = [float(u[0]) for u in umbrellas]
    lens = [float(u[1]) for u in umbrellas]
    v = [float(u[2]) for u in umbrellas]

    t = 0.0
    covered_area_time = 0.0

    while t < t_limit - EPS:
        # 求下一次反彈前可前進的最小時間
        remain = t_limit - t
        dt = remain

        for i in range(n):
            if abs(v[i]) < EPS:
                continue
            if v[i] > 0:
                bound = w - lens[i]
                hit = (bound - x[i]) / v[i]
            else:
                hit = (0.0 - x[i]) / v[i]
            if hit > EPS and hit < dt:
                dt = hit

        # 在 [t, t+dt] 做積分
        covered_area_time += covered_integral_piece(x, v, lens, dt)

        # 前進位置
        for i in range(n):
            x[i] += v[i] * dt
            if abs(x[i]) < 1e-10:
                x[i] = 0.0
            right_bound = w - lens[i]
            if abs(x[i] - right_bound) < 1e-10:
                x[i] = right_bound

        t += dt

        # 到達邊界就反彈
        for i in range(n):
            right_bound = w - lens[i]
            if abs(x[i]) < 1e-9 and v[i] < 0:
                v[i] = -v[i]
            elif abs(x[i] - right_bound) < 1e-9 and v[i] > 0:
                v[i] = -v[i]

    total_area_time = w * t_limit
    uncovered_area_time = total_area_time - covered_area_time
    return uncovered_area_time * rain_v


def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    n, w, t_limit, rain_v = nums[:4]
    umbrellas = []
    p = 4
    for _ in range(n):
        umbrellas.append((nums[p], nums[p + 1], nums[p + 2]))
        p += 3

    ans = solve_one_case(n, float(w), float(t_limit), float(rain_v), umbrellas)
    return f"{ans:.2f}"


def main() -> None:
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
