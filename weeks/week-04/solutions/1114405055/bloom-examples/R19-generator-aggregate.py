# R19. 轉換+聚合：生成器表達式（1.19）

nums = [1, 2, 3, 4]

# 生成器表達式可直接餵給聚合函式，不需先建立中間 list。
sum_of_squares = sum(x * x for x in nums)
print("sum of squares:", sum_of_squares)

record = ("ACME", 50, 123.45)
csv_line = ",".join(str(value) for value in record)
print("csv line:", csv_line)

portfolio = [
    {"name": "AOL", "shares": 20},
    {"name": "YHOO", "shares": 75},
    {"name": "FB", "shares": 10},
]

min_shares = min(item["shares"] for item in portfolio)
min_position = min(portfolio, key=lambda item: item["shares"])
print("min shares:", min_shares)
print("position with min shares:", min_position)
