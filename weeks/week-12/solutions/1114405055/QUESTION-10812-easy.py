# UVA 10812 — Beat the Spread! (Easy Version with Comments)
# 超級盃賭局問題：根據和(S)和差(D)求兩隊分數

def solve_spread():
    """
    解題思路：
    - 設較高分為 H，較低分為 L
    - H + L = S (和)
    - H - L = D (差，絕對值)
    - 解得：H = (S + D) / 2，L = (S - D) / 2
    - 檢查：1. S+D 必須是偶數
             2. H 和 L 都必須是非負整數
    """
    n = int(input())  # 測試資料組數
    
    for _ in range(n):
        s, d = map(int, input().split())  # 輸入和 S 與差 D
        
        # 檢查 S + D 是否為偶數
        if (s + d) % 2 != 0:
            print("impossible")
            continue
        
        # 計算較高分和較低分
        h = (s + d) // 2  # 較高分
        l = (s - d) // 2  # 較低分
        
        # 檢查是否都是非負數
        if h >= 0 and l >= 0:
            print(h, l)  # 較大的先輸出
        else:
            print("impossible")

# 主程式
if __name__ == "__main__":
    solve_spread()
