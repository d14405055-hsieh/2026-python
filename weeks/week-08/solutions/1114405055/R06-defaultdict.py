# R6: defaultdict and setdefault

from collections import defaultdict


d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
print("defaultdict(list) ->", dict(d))

d2 = defaultdict(set)
d2["a"].add(1)
d2["a"].add(2)
d2["a"].add(2)
print("defaultdict(set) ->", {k: sorted(v) for k, v in d2.items()})

d3 = {}
d3.setdefault("a", []).append(1)
d3.setdefault("a", []).append(2)
print("setdefault ->", d3)
