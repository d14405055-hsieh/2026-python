# UVA 10908 — Largest Square (Manual Version)

t = int(input())

for _ in range(t):
    m, n, q = map(int, input().split())
    print(m, n, q)
    
    grid = []
    for _ in range(m):
        grid.append(input())
    
    for _ in range(q):
        r, c = map(int, input().split())
        
        result = 1
        
        # 嘗試每個可能的正方形邊長
        for length in range(1, min(m, n) + 1, 2):
            offset = length // 2
            
            # 檢查邊界
            if r - offset < 0 or r + offset >= m or c - offset < 0 or c + offset >= n:
                break
            
            # 檢查所有字元是否相同
            ch = grid[r][c]
            is_valid = True
            
            for x in range(r - offset, r + offset + 1):
                for y in range(c - offset, c + offset + 1):
                    if grid[x][y] != ch:
                        is_valid = False
                        break
                if not is_valid:
                    break
            
            if is_valid:
                result = length
            else:
                break
        
        print(result)
