# 整合應用-找零錢程式
price = 23  # 飲料價格
pay = 100  # 付款金額
exchange = pay - price  # 找錢金額
print("價格:", price, "付款:", pay, "找零:", exchange)
# 找 50 元硬幣的數量
fifty = exchange // 50
print("50元:", fifty)
exchange = exchange - fifty * 50  # 扣除掉已找 50 元的金額
print("還需找零:", exchange)
# 找 10 元硬幣的數量
ten = exchange // 10
print("10元:", ten)
exchange = exchange - ten * 10  # 扣除掉已找 10 元的金額
print("還需找零:", exchange)
# 找 5 元硬幣的數量
five = exchange // 5
print("5元:", five)
exchange = exchange - five * 5  # 扣除掉已找 5 元的金額
print("還需找零:", exchange)
# 找 1 元硬幣的數量
one = exchange
print("1元:", one)
