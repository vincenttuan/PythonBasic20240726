import random
# 猜數字
# 0~9 猜一數字
# 系統會提醒猜大或猜小了
if __name__ == '__main__':
    min, max = 1, 9
    ans = random.randint(min, max)  # 隨機產生一個答案
    # --------------------------------------------------
    while True:
        # 使用者猜的程序
        user_guess = int(input('使用者請輸入數字(%d~%d):' % (min, max)))
        if user_guess > ans:
            print("使用者猜大了")
            max = user_guess - 1  # 更新範圍的上限
        elif user_guess < ans:
            print("使用者猜小了")
            min = user_guess + 1  # 更新範圍的下限
        else:
            print('恭喜使用者猜中了')
            break
        # 電腦猜的程序
        pc_guess = random.randint(min, max)
        print('電腦所猜的數字(%d~%d):%d' % (min, max, pc_guess))
        if pc_guess > ans:
            print("電腦猜大了")
            max = pc_guess - 1  # 更新範圍的上限
        elif pc_guess < ans:
            print("電腦猜小了")
            min = pc_guess + 1  # 更新範圍的下限
        else:
            print('恭喜電腦猜中了')
            break
    # --------------------------------------------------
    print("Game Over!")
