# UVA 11005 — Cheapest Base（簡易版）
# 中文註解：以每個進位從 2 到 36 計算該數字的印刷成本，回傳成本最低的進位列表

def cost_in_base(costs, n, base):
    if n == 0:
        return costs[0]
    s = 0
    while n > 0:
        d = n % base
        s += costs[d]
        n //= base
    return s


def cheapest_bases(costs, n):
    best = None
    res = []
    for b in range(2, 37):
        c = cost_in_base(costs, n, b)
        if best is None or c < best:
            best = c
            res = [b]
        elif c == best:
            res.append(b)
    return res

if __name__ == '__main__':
    # 範例使用：簡單示範
    costs = [1]*36
    queries = [0, 10, 255]
    for q in queries:
        print(q, '->', cheapest_bases(costs, q))
