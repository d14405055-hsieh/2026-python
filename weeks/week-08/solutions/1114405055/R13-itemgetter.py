# R13: itemgetter

from operator import itemgetter


rows = [
    {"fname": "Brian", "uid": 1003},
    {"fname": "John", "uid": 1001},
    {"fname": "David", "uid": 1002},
]

print("sort by fname ->", sorted(rows, key=itemgetter("fname")))
print("sort by uid ->", sorted(rows, key=itemgetter("uid")))
print("sort by (uid, fname) ->", sorted(rows, key=itemgetter("uid", "fname")))
