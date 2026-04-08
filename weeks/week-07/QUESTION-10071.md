# 題目 10071

**題名**: UVA 10071

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a064)
- [Yui Huang 題解](https://yuihuang.com/zj-a064/)

## 題目敘述

給定一個整數集合 S，其元素均介於 -30000 到 30000 之間（含首尾）。
請計算满足条件的六元組數量：a + b + c + d + e = f，其中 a、b、c、d、e、f 均屬於 S（可重複使用）。

## 輸入說明

第一行包含一個整數 N（1 ≤ N ≤ 100），代表集合 S 的元素個數。
接下來的 N 行，每行一個整數，為 S 的元素。
所有數字均不重複。

## 輸出說明

輸出符合條件的六元組總數量。

---

## 解題思路

目標是計算滿足 `a+b+c+d+e=f` 的六元組數量（元素可重複選）。

直接六層迴圈是 `O(N^6)`，太慢。

改寫成：

`a+b+c = f-d-e`

做法：

1. 先列舉所有 `a,b,c`，把和存到雜湊表 `cnt3[sum]`（共有 `N^3` 種）。
2. 再列舉所有 `d,e,f`，查 `cnt3[f-d-e]` 累加答案（也是 `N^3` 次）。

總複雜度 `O(N^3)`，`N <= 100` 時可接受。

## 解題代碼

```python
# AI 教的簡單版本（有中文註解）
import sys
from collections import defaultdict


def solve():
	data = sys.stdin.read().strip().split()
	if not data:
		return

	n = int(data[0])
	s = list(map(int, data[1:1 + n]))

	# cnt3[x] = 有多少種 (a,b,c) 使得 a+b+c=x
	cnt3 = defaultdict(int)
	for a in s:
		for b in s:
			for c in s:
				cnt3[a + b + c] += 1

	ans = 0
	for d in s:
		for e in s:
			for f in s:
				ans += cnt3[f - d - e]

	print(ans)


if __name__ == "__main__":
	solve()
```

```python
# 你手打的程式（無註解）
import sys
from collections import defaultdict


def main():
	arr = sys.stdin.read().strip().split()
	if not arr:
		return
	n = int(arr[0])
	nums = list(map(int, arr[1:1 + n]))

	c3 = defaultdict(int)
	for x in nums:
		for y in nums:
			for z in nums:
				c3[x + y + z] += 1

	total = 0
	for d in nums:
		for e in nums:
			for f in nums:
				total += c3[f - d - e]
	print(total)


if __name__ == "__main__":
	main()
```

## 測試用例

```python
# 測試程式 test_10071.py
import subprocess


def run_case(inp: str) -> str:
	p = subprocess.run(
		["python", "solve_10071_hand.py"],
		input=inp,
		text=True,
		capture_output=True,
		check=True,
	)
	return p.stdout.strip()


def brute(nums):
	ans = 0
	for a in nums:
		for b in nums:
			for c in nums:
				for d in nums:
					for e in nums:
						for f in nums:
							if a + b + c + d + e == f:
								ans += 1
	return ans


def test_case_1():
	nums = [1, 2]
	inp = "2\n1\n2\n"
	assert run_case(inp) == str(brute(nums))


def test_case_2():
	nums = [-1, 0, 1]
	inp = "3\n-1\n0\n1\n"
	assert run_case(inp) == str(brute(nums))
```

```text
# 你手打程式的測試 LOG
$ pytest -q test_10071.py
..
2 passed in 0.12s
```
