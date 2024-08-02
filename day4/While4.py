import random
# 猜數字
# 0~9 猜一數字
# 系統會提醒猜大或猜小了
if __name__ == '__main__':
    ans = random.randint(1, 9)  # 隨機產生一個答案
    # --------------------------------------------------
    while True:
        # 使用者猜的程序
        user_guess = int(input('使用者請輸入數字(0~9):'))
        if user_guess > ans:
            print("使用者猜大了")
        elif user_guess < ans:
            print("使用者猜小了")
        else:
            print('恭喜使用者猜中了')
            break
    # --------------------------------------------------
    print("Game Over!")
