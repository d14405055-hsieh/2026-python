# UVA 10812 — Beat the Spread! (Manual Version)

n = int(input())

for _ in range(n):
    s, d = map(int, input().split())
    
    # 計算較高分 = (S + D) / 2，較低分 = (S - D) / 2
    if (s + d) % 2 != 0:
        print("impossible")
    else:
        higher = (s + d) // 2
        lower = (s - d) // 2
        
        if higher >= 0 and lower >= 0:
            print(higher, lower)
        else:
            print("impossible")
