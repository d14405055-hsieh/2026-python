# UVA 10922 — 2 the 9s (Easy Version with Comments)
# 計算其他數是否為9的倍數，以及9的深度

def digit_sum(n):
    """計算數字各位數字之和"""
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

def solve_nine_degree():
    """
    解題思路：
    - 先檢查輸入數是否為 9 的倍數（各位數字之和 % 9 == 0）
    - 若是，逐次計算各位數字之和，直到得到一位數
    - 計算需要重複的次數（即 9 的深度）
    """
    while True:
        n_str = input().strip()
        
        if n_str == "0":  # 結束輸入
            break
        
        # 將輸入字串轉為整數（可能很大）
        try:
            n = int(n_str)
        except:
            n = int(n_str)
        
        # 先計算各位數字之和
        current_sum = digit_sum(n)
        
        # 檢查是否為 9 的倍數
        if current_sum % 9 != 0:
            print(f"{n} is not a multiple of 9.")
        else:
            # 計算 9 的深度
            degree = 1
            current = current_sum
            
            # 重複計算各位數字之和，直到得到 9
            while current != 9:
                current = digit_sum(current)
                degree += 1
            
            print(f"9-degree of {n} is {degree}.")

# 主程式
if __name__ == "__main__":
    solve_nine_degree()
