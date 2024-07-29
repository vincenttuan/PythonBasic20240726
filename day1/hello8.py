# 整合應用-找零錢程式
# 買飲料一瓶 123 元, 付了 1000 元, 請問要找幾元 ? 如何找 ?

price = int(input('請輸入飲料價格:'))
pay = int(input('請輸入付款金額:'))
exchange = pay - price
print('飲料:', price, ' 付款:', pay, " 應找:", exchange)
# -------------------------------------------------------
# 計算找零的面額與數量
# -------------------------------------------------------
five_hundred = exchange // 500
exchange = exchange - 500*five_hundred
print("500元:", five_hundred)
# -------------------------------------------------------
one_hundred = exchange // 100
exchange = exchange - 100*one_hundred
print("100元:", one_hundred)
# -------------------------------------------------------
fifty = exchange // 50
exchange = exchange - 50*fifty
print("50元:", fifty)
# -------------------------------------------------------
ten = exchange // 10
exchange = exchange - 10*ten
print("10元:", ten)
# -------------------------------------------------------
five = exchange // 5
exchange = exchange - 5*five
print("5元:", five)
# -------------------------------------------------------
one = exchange
print("1元:", one)
# -------------------------------------------------------






