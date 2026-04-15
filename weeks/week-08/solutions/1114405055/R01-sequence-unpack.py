# R1: Sequence unpacking

p = (4, 5)
x, y = p
print("tuple unpack ->", x, y)

data = ["ACME", 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print("record unpack ->", name, shares, price, date)

name, shares, price, (year, month, day) = data
print("nested unpack ->", year, month, day)

# Ignore values with underscore
_, shares, price, _ = data
print("ignore fields ->", shares, price)
