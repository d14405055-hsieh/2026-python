# TEST_CASES.md — Week 03 自訂測資

## UVA 100

輸入：

```
1 10
100 200
201 210
900 1000
```

預期輸出：

```
1 10 20
100 200 125
201 210 89
900 1000 174
```

## UVA 118

輸入：

```
5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
```

預期輸出：

```
1 1 E
3 3 N LOST
2 3 S
```

## UVA 272

輸入：

```
"To be or not to be," quoth the bard, "that is the question."
```

預期輸出：

```
``To be or not to be,'' quoth the bard, ``that is the question.''
```

## UVA 299

輸入：

```
3
3
1 3 2
4
4 3 2 1
2
2 1
```

預期輸出：

```
Optimal train swapping takes 1 swaps.
Optimal train swapping takes 6 swaps.
Optimal train swapping takes 1 swaps.
```

## UVA 490

輸入：

```
Rene Decartes once said,
"I think, therefore I am."
```

預期輸出：

```
"R
ie
 n
te
hn
ok
,e
 ,
t
Dh
 ee
cr
ae
rn
te
es
s 
 o
nn
cc
ee
 
s
a
id
,."
```

## Robot Game Unit Tests (UVA 118 Core)

- 測試檔：
	- tests/test_robot_core.py
	- tests/test_robot_scent.py
- 覆蓋重點：
	- 方向旋轉（L/R）
	- 前進與邊界判定（MOVE/LOST）
	- LOST 後命令忽略（NOOP_LOST）
	- scent 保護（SCENT_BLOCK）
	- scent 方向敏感性（同座標不同方向）
