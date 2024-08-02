import random
# 迴圈
# 不斷印出 0~100 任意"偶數"數字
# 遇到 0 則跳離(break)迴圈

if __name__ == '__main__':
    while True:
        number = random.randint(0, 100)
        # ----------------------------------
        if number % 2 == 0:
            print(number, end=' ')
        # ----------------------------------
        if number == 0:
            break
        # ----------------------------------
    
