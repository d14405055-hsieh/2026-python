# R10: Deduplicate while preserving order

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


nums = [1, 5, 2, 1, 9, 1, 5, 10]
print("dedupe nums ->", list(dedupe(nums)))

rows = [
    {"x": 1, "y": 2},
    {"x": 1, "y": 2},
    {"x": 2, "y": 3},
    {"x": 1, "y": 2},
]
print("dedupe dicts by (x,y) ->", list(dedupe2(rows, key=lambda d: (d["x"], d["y"]))))
