# R9: Dictionary set operations

a = {"x": 1, "y": 2, "z": 3}
b = {"w": 10, "x": 11, "y": 2}

print("common keys ->", a.keys() & b.keys())
print("a-only keys ->", a.keys() - b.keys())
print("common (key, value) ->", a.items() & b.items())

c = {k: a[k] for k in a.keys() - {"z", "w"}}
print("filtered dict ->", c)
