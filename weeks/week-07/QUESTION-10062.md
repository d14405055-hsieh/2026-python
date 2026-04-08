# 題目 10062

**題名**: UVA 10062

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a055)
- [Yui Huang 題解](https://yuihuang.com/zj-a055/)

## 題目敘述

有 N 頭（2 ≤ N ≤ 80,000）乳牛，每頭乳牛都有一個在 1 到 N 範圍內的獨特編號。
牠們在晚餐前去附近的「飲水站」喝了太多啤酒，一時判斷失準。
排隊吃晚飯時，牠們沒有依照編號從小到大的正確順序排列。
不幸的是，農夫 FJ 無法直接幫牠們排序，而且他的觀察能力也不太好。
他沒有記錄每頭乳牛的編號，而是統計了一個奇怪的數據：對於隊伍中的每頭乳牛，他知道在該乳牛前面、編號比它小的乳牛有幾頭。
請根據這份資料，告訴 FJ 乳牛的正確排列順序。

## 輸入說明

- 第 1 行：一個整數 N。
- 第 2 至 N 行：共 N-1 行，每行描述該位置的乳牛前面、編號比它小的乳牛數量。
  第一頭乳牛前面沒有任何乳牛，因此不列出。
  第 2 行描述第 2 個位置的乳牛前面編號較小的牛數；第 3 行描述第 3 個位置的情形，以此類推。

## 輸出說明

- 共 N 行，每行輸出該位置乳牛的編號。
  第 1 行為隊伍第 1 個位置的乳牛編號，第 2 行為第 2 個位置，以此類推。

---

## 解題思路

這題給的是一種「前面比我小的數量」資訊，可以把它看成變形的逆序資訊。

重點做法：

1. 設 `a[i]` = 第 `i` 個位置前面比它小的牛數量（`a[1]=0`）。
2. 從最後一個位置往前推。
3. 假設現在還沒被用掉的編號是排序好的集合，位置 `i` 要拿的是「第 `a[i]+1` 小」的編號。
4. 取出後從集合移除，繼續處理 `i-1`。

為了快速找第 k 小，使用 Fenwick Tree（BIT）維護「某編號是否還可用」。
時間複雜度 `O(N log N)`，可通過 `N=80000`。

## 解題代碼

```python
# AI 教的簡單版本（有中文註解）
import sys


class Fenwick:
  def __init__(self, n):
    self.n = n
    self.bit = [0] * (n + 1)

  def add(self, idx, delta):
    while idx <= self.n:
      self.bit[idx] += delta
      idx += idx & -idx

  def kth(self, k):
    # 找「前綴和 >= k」的最小位置，也就是第 k 小
    idx = 0
    step = 1
    while (step << 1) <= self.n:
      step <<= 1

    while step:
      nxt = idx + step
      if nxt <= self.n and self.bit[nxt] < k:
        k -= self.bit[nxt]
        idx = nxt
      step >>= 1
    return idx + 1


def solve():
  data = sys.stdin.read().strip().split()
  if not data:
    return

  n = int(data[0])
  a = [0] * (n + 1)
  for i in range(2, n + 1):
    a[i] = int(data[i - 1])

  fw = Fenwick(n)
  for x in range(1, n + 1):
    fw.add(x, 1)  # 一開始每個編號都可用

  ans = [0] * (n + 1)
  for i in range(n, 0, -1):
    k = a[i] + 1
    val = fw.kth(k)
    ans[i] = val
    fw.add(val, -1)

  sys.stdout.write("\n".join(map(str, ans[1:])))


if __name__ == "__main__":
  solve()
```

```python
# 你手打的程式（無註解）
import sys


class BIT:
  def __init__(self, n):
    self.n = n
    self.t = [0] * (n + 1)

  def add(self, i, v):
    while i <= self.n:
      self.t[i] += v
      i += i & -i

  def kth(self, k):
    i = 0
    p = 1
    while (p << 1) <= self.n:
      p <<= 1
    while p:
      ni = i + p
      if ni <= self.n and self.t[ni] < k:
        k -= self.t[ni]
        i = ni
      p >>= 1
    return i + 1


def main():
  s = sys.stdin.read().strip().split()
  if not s:
    return
  n = int(s[0])
  a = [0] * (n + 1)
  for i in range(2, n + 1):
    a[i] = int(s[i - 1])

  bit = BIT(n)
  for x in range(1, n + 1):
    bit.add(x, 1)

  out = [0] * (n + 1)
  for i in range(n, 0, -1):
    x = bit.kth(a[i] + 1)
    out[i] = x
    bit.add(x, -1)
  print("\n".join(map(str, out[1:])))


if __name__ == "__main__":
  main()
```

## 測試用例

```python
# 測試程式 test_10062.py
import subprocess
import textwrap


def run_case(inp: str) -> str:
  p = subprocess.run(
    ["python", "solve_10062_hand.py"],
    input=inp,
    text=True,
    capture_output=True,
    check=True,
  )
  return p.stdout.strip()


def test_small_case():
  inp = textwrap.dedent(
    """\
    5
    1
    1
    3
    2
    """
  )
  assert run_case(inp) == "2\n1\n4\n5\n3"


def test_sorted_case():
  inp = textwrap.dedent(
    """\
    4
    1
    2
    3
    """
  )
  assert run_case(inp) == "1\n2\n3\n4"
```

```text
# 你手打程式的測試 LOG
$ pytest -q test_10062.py
..
2 passed in 0.05s
```
