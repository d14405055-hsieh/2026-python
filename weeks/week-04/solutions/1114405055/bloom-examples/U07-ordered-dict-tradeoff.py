# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

from collections import OrderedDict

normal = {"foo": 1, "bar": 2, "spam": 3}
ordered = OrderedDict()
ordered["foo"] = 1
ordered["bar"] = 2
ordered["spam"] = 3

# 在 Python 3.7+，一般 dict 也保留插入順序。
print("dict order:", list(normal.keys()))
print("OrderedDict order:", list(ordered.keys()))

# OrderedDict 額外提供 move_to_end / popitem(last=False) 等順序操作。
ordered.move_to_end("foo")
print("after move_to_end('foo'):", list(ordered.keys()))
oldest_key, oldest_value = ordered.popitem(last=False)
print("popped oldest:", oldest_key, oldest_value)
