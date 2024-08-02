# 自訂函式
# 買 x 送 y
# price 表示每瓶售價
# amount 表示購買數量
def sales_strategy(price, amount, x, y):
    # 計算每 x+y 瓶要支付的瓶數
    bottles_to_pay = (amount // (x + y)) * x + (amount % (x + y))
    # 計算費用
    total = bottles_to_pay * price
    # 印出購買清單
    print("飲料每瓶 %d 元 (買 %d 送 %d) 買進 %d 瓶 共需: %d 元" % (price, x, y, amount, total))


if __name__ == '__main__':
    sales_strategy(10, 15, 5, 2)
    sales_strategy(15, 9, 3, 2)


