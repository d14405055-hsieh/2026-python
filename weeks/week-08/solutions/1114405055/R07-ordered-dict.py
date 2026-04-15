# R7: OrderedDict

import json
from collections import OrderedDict


d = OrderedDict()
d["foo"] = 1
d["bar"] = 2
d["spam"] = 3

print("ordered dict ->", d)
print("json ->", json.dumps(d))
