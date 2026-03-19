# R18. namedtuple（1.18）

from collections import namedtuple

Subscriber = namedtuple("Subscriber", ["addr", "joined"])
sub = Subscriber("jonesy@example.com", "2012-10-19")
print("subscriber:", sub)
print("addr:", sub.addr)

Stock = namedtuple("Stock", ["name", "shares", "price"])
stock = Stock("ACME", 100, 123.45)
print("before:", stock)

# namedtuple 是不可變的，更新時用 _replace 產生新物件。
stock = stock._replace(shares=75)
print("after:", stock)
