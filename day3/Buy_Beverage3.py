# 動動腦
# 飲料一瓶 10 元 買 x 送 y, 請問買 amount 瓶要多少 ?
price = 10  # 價格
x = 5  # 買
y = 3  # 送
amount = 10  # 買入瓶數

# 計算每 x+y 瓶要支付的瓶數
bottles_to_pay = (amount // (x+y)) * x + (amount % (x+y))
# 計算費用
total = bottles_to_pay * price
print("費用:", total)



