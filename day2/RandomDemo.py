# 隨機數套件
import random

print(random.random())  # 產生0~1的隨機數
print(random.randint(1, 9))  # 產生1~9的隨機數
# -----------------------------------------------
# 四星彩電腦選號
n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
n4 = random.randint(0, 9)
print(n1, n2, n3, n4)
