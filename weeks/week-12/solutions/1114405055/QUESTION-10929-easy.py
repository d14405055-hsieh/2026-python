# UVA 10929 — Check if Multiple of 11 (Easy Version with Comments)
# 判斷一個很大的數是否為 11 的倍數

def solve_multiple_of_11():
    """
    解題思路：
    - 一個數是 11 的倍數，當且僅當「奇數位數字之和」與「偶數位數字之和」的差是 11 的倍數
    - 位數由右到左編號，第 1 位、第 3 位、第 5 位... 為奇數位
    - 第 2 位、第 4 位、第 6 位... 為偶數位
    """
    while True:
        n = input().strip()
        
        if n == "0":  # 結束輸入
            break
        
        # 計算奇數位數字之和與偶數位數字之和
        odd_sum = 0   # 奇數位（1, 3, 5...）
        even_sum = 0  # 偶數位（2, 4, 6...）
        
        # 從右到左逐位計算
        for i in range(len(n) - 1, -1, -1):
            digit = int(n[i])
            position = len(n) - i  # 位置（從右到左）
            
            if position % 2 == 1:  # 奇數位
                odd_sum += digit
            else:  # 偶數位
                even_sum += digit
        
        # 判斷差是否為 11 的倍數
        diff = odd_sum - even_sum
        
        if diff % 11 == 0:
            print(f"{n} is a multiple of 11.")
        else:
            print(f"{n} is not a multiple of 11.")

# 主程式
if __name__ == "__main__":
    solve_multiple_of_11()
