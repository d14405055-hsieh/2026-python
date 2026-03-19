# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）

from collections import deque

q = deque(maxlen=3)
for i in [1, 2, 3, 4, 5]:
    q.append(i)
    # 超過 maxlen 時，左端舊資料會被自動丟掉。
    print(f"append {i} ->", list(q))

print("final:", list(q))
