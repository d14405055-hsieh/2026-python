# QUESTION-11063 — RGB to XYZ 主程式（整合 helper）
import sys

def rgb_to_xyz(r, g, b):
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z

def fmt_xyz(x,y,z):
    return f"{x:.4f} {y:.4f} {z:.4f}"

def process_stream(data_iter):
    n = int(next(data_iter))
    Ys = []
    out_lines = []
    for _ in range(n*n):
        r = int(next(data_iter)); g = int(next(data_iter)); b = int(next(data_iter))
        x,y,z = rgb_to_xyz(r,g,b)
        Ys.append(y)
        out_lines.append(fmt_xyz(x,y,z))
    avg = sum(Ys)/len(Ys) if Ys else 0.0
    out_lines.append(f"The average of Y is {avg:.4f}")
    return out_lines

if __name__ == '__main__':
    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit(0)
    it = iter(data)
    for line in process_stream(it):
        print(line)
