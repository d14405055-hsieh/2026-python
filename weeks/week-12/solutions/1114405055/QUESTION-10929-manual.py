# UVA 10929 — Check if Multiple of 11 (Manual Version)

while True:
    num = input().strip()
    
    if num == "0":
        break
    
    odd_pos_sum = 0
    even_pos_sum = 0
    
    for i, digit in enumerate(reversed(num)):
        pos = i + 1  # 位置從 1 開始計算
        if pos % 2 == 1:
            odd_pos_sum += int(digit)
        else:
            even_pos_sum += int(digit)
    
    difference = odd_pos_sum - even_pos_sum
    
    if difference % 11 == 0:
        print(f"{num} is a multiple of 11.")
    else:
        print(f"{num} is not a multiple of 11.")
