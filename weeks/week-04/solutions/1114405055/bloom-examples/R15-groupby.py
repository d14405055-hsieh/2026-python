# R15. 分組 groupby（1.15）

from itertools import groupby
from operator import itemgetter

rows = [
    {"date": "07/01/2012", "address": "5412 N CLARK"},
    {"date": "07/01/2012", "address": "4801 N BROADWAY"},
    {"date": "07/02/2012", "address": "1039 W GRANVILLE"},
    {"date": "07/04/2012", "address": "5148 N CLARK"},
]

# groupby 只會把「連續」且 key 相同的資料分在一起，所以要先排序。
rows.sort(key=itemgetter("date"))

for date, items in groupby(rows, key=itemgetter("date")):
    print(f"{date}:")
    for item in items:
        print("  ", item["address"])
