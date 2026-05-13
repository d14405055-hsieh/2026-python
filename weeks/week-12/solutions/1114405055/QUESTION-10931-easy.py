# UVA 10931 — Parity (Easy Version with Comments)
# 計算整數的二進位表示中，1 的個數（奇偶性）

def solve_parity():
    """
    解題思路：
    - 將整數轉換為二進位表示
    - 計算二進位中 1 的個數
    - 按格式輸出結果
    """
    while True:
        i = int(input())
        
        if i == 0:  # 結束輸入
            break
        
        # 獲得二進位表示（不含 '0b' 前綴）
        binary_str = bin(i)[2:]  # bin() 返回 '0b...'，去掉前兩個字元
        
        # 計算二進位中 1 的個數
        parity = binary_str.count('1')
        
        # 按格式輸出
        print(f"The parity of {binary_str} is {parity} (mod 2).")

# 主程式
if __name__ == "__main__":
    solve_parity()
