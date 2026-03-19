# U9. groupby 為何一定要先 sort（1.15）

from itertools import groupby
from operator import itemgetter

rows = [
    {"date": "07/02/2012", "x": 1},
    {"date": "07/01/2012", "x": 2},
    {"date": "07/02/2012", "x": 3},
    {"date": "07/01/2012", "x": 4},
]

print("without sort:")
for date, group in groupby(rows, key=itemgetter("date")):
    print(date, list(group))

# groupby 只會把相鄰且 key 相同的資料分在同組，所以先排序才會正確。
rows.sort(key=itemgetter("date"))
print("\nwith sort:")
for date, group in groupby(rows, key=itemgetter("date")):
    print(date, list(group))
