# UVA 11063 — RGB to XYZ（簡易版）
# 中文註解：將輸入的 R,G,B 轉換到 X,Y,Z，Y 為亮度，並計算平均 Y

def rgb_to_xyz(r, g, b):
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z

if __name__ == '__main__':
    pixels = [(255,3,192), (0,0,0), (255,255,255)]
    Ys = []
    for (r,g,b) in pixels:
        x,y,z = rgb_to_xyz(r,g,b)
        Ys.append(y)
        print(f"{x:.4f} {y:.4f} {z:.4f}")
    print(f"The average of Y is {sum(Ys)/len(Ys):.4f}")
