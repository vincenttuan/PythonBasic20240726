import random
# 迴圈
# 不斷印出 0~100 任意數字
# 遇到 0 則跳離(break)迴圈

if __name__ == '__main__':
    while True:
        number = random.randint(0, 100)  # 0~100 任意數字
        print(number, end=' ')
        if number == 0:
            break  # 跳離迴圈
