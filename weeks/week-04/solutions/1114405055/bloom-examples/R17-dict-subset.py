# R17. 字典子集（1.17）

prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM": 205.55,
    "HPQ": 37.20,
    "MSFT": 310.10,
}

# 依 value 篩選：找出股價大於 200 的股票。
expensive = {name: price for name, price in prices.items() if price > 200}
print("expensive:", expensive)

tech_names = {"AAPL", "IBM", "MSFT"}

# 依 key 篩選：只保留特定名稱。
tech_stocks = {name: price for name, price in prices.items() if name in tech_names}
print("tech stocks:", tech_stocks)
