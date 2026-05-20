# 輔助與主程式：QUESTION-11005
# 整合原先的輔助函式，可作為主要模組或直接執行

def digit_char(d):
    if d < 10:
        return str(d)
    return chr(ord('A') + d - 10)

def to_base_str(n, base):
    if n == 0:
        return '0'
    s = ''
    while n > 0:
        s = digit_char(n % base) + s
        n //= base
    return s

def cost_in_base(costs, n, base):
    if n == 0:
        return costs[0]
    s = 0
    while n > 0:
        s += costs[n % base]
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
    # 範例執行：若需作為完整解題檔，可改為讀取 stdin
    costs = [1] * 36
    queries = [0, 10, 255]
    for q in queries:
        print(q, '->', cheapest_bases(costs, q))
