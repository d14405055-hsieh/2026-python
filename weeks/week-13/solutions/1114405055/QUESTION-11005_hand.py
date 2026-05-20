# UVA 11005 — Cheapest Base（手打版本）
# 以題目輸入格式處理多組測資與多筆查詢

def cost_in_base(costs, n, base):
    if n == 0:
        return costs[0]
    s = 0
    while n > 0:
        s += costs[n % base]
        n //= base
    return s


def process_case(costs, queries):
    out_lines = []
    for n in queries:
        best = None
        bases = []
        for b in range(2, 37):
            c = cost_in_base(costs, n, b)
            if best is None or c < best:
                best = c
                bases = [b]
            elif c == best:
                bases.append(b)
        out_lines.append((n, bases))
    return out_lines

if __name__ == '__main__':
    # 本檔可被作為模組匯入或命令列使用
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        print('No input')
        sys.exit(0)
    it = iter(data)
    T = int(next(it))
    case_no = 1
    for _ in range(T):
        costs = [int(next(it)) for _ in range(36)]
        qn = int(next(it))
        queries = [int(next(it)) for _ in range(qn)]
        results = process_case(costs, queries)
        print(f'Case {case_no}:')
        for n, bases in results:
            print('Cheapest base(s) for number %d:' % n, ' '.join(map(str, bases)))
        print()
        case_no += 1
