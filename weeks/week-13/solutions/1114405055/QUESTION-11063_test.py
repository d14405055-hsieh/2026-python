# 測試檔：針對 QUESTION-11063 的簡單測試
from QUESTION_11063_easy import rgb_to_xyz

pixels = [(255,3,192), (0,0,0), (128,128,128)]
Ys = []
for r,g,b in pixels:
    x,y,z = rgb_to_xyz(r,g,b)
    Ys.append(y)
    print(f"{x:.4f} {y:.4f} {z:.4f}")
print(f"The average of Y is {sum(Ys)/len(Ys):.4f}")
