# 利用 for 步進敘述產生 4 個 0~9 之間的隨機數
import random

for i in range(0, 4):
    number = random.randint(0, 9)
    print(number, end=' ')
