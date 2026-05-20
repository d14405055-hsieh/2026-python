# 測試檔：模擬幾次放陷阱的結果
from QUESTION_11321_easy import can_reach

N,M = 3,10
blocked = set()
queries = [(0,1),(1,1),(2,9),(1,0),(1,9)]
for q in queries:
    if q in blocked:
        print('>_<')
        continue
    blocked.add(q)
    if can_reach(N,M,blocked):
        print('<(_ _)>')
    else:
        blocked.remove(q)
        print('>_<')
