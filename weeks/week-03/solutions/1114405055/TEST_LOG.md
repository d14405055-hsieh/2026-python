# TEST_LOG.md — Week 03 測試執行紀錄

## Run 1

- 目的：確認 5 題程式可以獨立執行，並符合經典範例輸出。
- 執行方式：使用 PowerShell 管線把範例輸入導入程式。
- 結果：全部通過（5/5）。

### UVA 100

指令：

```powershell
"1 10`n100 200`n201 210`n900 1000" | python .\uva100_3n1.py
```

輸出：

```text
1 10 20
100 200 125
201 210 89
900 1000 174
```

### UVA 118

指令：

```powershell
"5 3`n1 1 E`nRFRFRFRF`n3 2 N`nFRRFLLFFRRFLL`n0 3 W`nLLFFFLFLFL" | python .\uva118_mutant_flatworld.py
```

輸出：

```text
1 1 E
3 3 N LOST
2 3 S
```

### UVA 272

指令：

```powershell
$input272 = @'
"To be or not to be," quoth the bard, "that is the question."
'@
$input272 | python .\uva272_tex_quotes.py
```

輸出：

```text
``To be or not to be,'' quoth the bard, ``that is the question.''
```

### UVA 299

指令：

```powershell
"3`n3`n1 3 2`n4`n4 3 2 1`n2`n2 1" | python .\uva299_train_swapping.py
```

輸出：

```text
Optimal train swapping takes 1 swaps.
Optimal train swapping takes 6 swaps.
Optimal train swapping takes 1 swaps.
```

### UVA 490

指令：

```powershell
$input490 = @'
Rene Decartes once said,
"I think, therefore I am."
'@
$input490 | python .\uva490_rotating_sentences.py
```

輸出：

```text
"R
Ie
 n
te
h
iD
ne
kc
,a
 r
tt
he
es
r
eo
fn
oc
re
e
 s
Ia
 i
ad
m,
.
"
```

補充驗證：

```powershell
$input = @'
HELLO
WORLD
'@
$input | python .\uva490_rotating_sentences.py
```

```text
WH
OE
RL
LL
DO
```
