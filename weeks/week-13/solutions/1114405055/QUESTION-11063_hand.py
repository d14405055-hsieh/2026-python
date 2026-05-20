# UVA 11063 — 完整手打版本，從 stdin 讀取資料並輸出格式化結果
import sys

def rgb_to_xyz(r, g, b):
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z

if __name__ == '__main__':
    data = sys.stdin.read().strip().split()
    if not data:
        print('')
        sys.exit(0)
    it = iter(data)
    n = int(next(it))
    Ys = []
    for _ in range(n*n):
        r = int(next(it)); g = int(next(it)); b = int(next(it))
        x,y,z = rgb_to_xyz(r,g,b)
        Ys.append(y)
        print(f"{x:.4f} {y:.4f} {z:.4f}")
    avg = sum(Ys)/len(Ys) if Ys else 0.0
    print(f"The average of Y is {avg:.4f}")
