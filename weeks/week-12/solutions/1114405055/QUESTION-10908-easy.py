# UVA 10908 — Largest Square (Easy Version with Comments)
# 找出以給定點為中心的最大正方形邊長

def solve_largest_square():
    """
    解題思路：
    - 給定中心點 (r, c)，逐漸向外擴大正方形
    - 正方形邊長必須為奇數 (1, 3, 5, ...)
    - 檢查正方形內所有字元是否相同
    - 找到最大邊長為止
    """
    t = int(input())  # 測試資料組數
    
    for _ in range(t):
        m, n, q = map(int, input().split())  # 行數、列數、查詢次數
        print(m, n, q)
        
        # 讀入網格
        grid = []
        for _ in range(m):
            grid.append(input().strip())
        
        # 處理每個查詢
        for _ in range(q):
            r, c = map(int, input().split())  # 中心點座標
            
            # 從邊長 1 開始檢查
            max_side = 1
            
            # 逐漸增加邊長（只檢查奇數）
            for side_len in range(1, min(m, n) + 1, 2):
                dist = side_len // 2  # 距中心的距離
                
                # 檢查邊界
                if r - dist < 0 or r + dist >= m or c - dist < 0 or c + dist >= n:
                    break  # 超出邊界，停止擴大
                
                # 檢查正方形內所有字元
                center_char = grid[r][c]
                valid = True
                
                for i in range(r - dist, r + dist + 1):
                    for j in range(c - dist, c + dist + 1):
                        if grid[i][j] != center_char:
                            valid = False
                            break
                    if not valid:
                        break
                
                if valid:
                    max_side = side_len
                else:
                    break
            
            print(max_side)

# 主程式
if __name__ == "__main__":
    solve_largest_square()
