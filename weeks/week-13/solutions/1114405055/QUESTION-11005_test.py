# 測試檔：模擬簡單輸入並顯示輸出
from QUESTION_11005_easy_import_fix import cheapest_bases

# 因為本範例檔案彼此同目錄，我們直接呼叫 easy 裡的函式
# 但為了避免 import 路徑問題，這裡以直接複寫函式示範

def cheapest_bases_local(costs, n):
    if n == 0:
        return [2]
    best = None
    res = []
    for b in range(2, 37):
        s = 0
        m = n
        if m == 0:
            s += costs[0]
        while m > 0:
            s += costs[m % b]
            m //= b
        if best is None or s < best:
            best = s
            res = [b]
        elif s == best:
            res.append(b)
    return res

if __name__ == '__main__':
    costs = [1]*36
    queries = [0, 10, 255]
    for q in queries:
        print(q, '->', cheapest_bases_local(costs, q))
