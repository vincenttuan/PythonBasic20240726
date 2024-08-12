# 例外處理應用
# 使用者輸入半徑之後可以計算出圓面積
# 若使用者輸入非數字資料如何透過例外處理來告知使用者 ?
# 例如: 若使用者輸入 abc, 程式捕捉到錯誤之後要印出 "請輸入整數資料" 的訊息
import math

def user_input():
    r = input('請輸入半徑:')
    r = float(r)  # 字串轉浮點數
    area = r ** 2 * math.pi
    print('半徑: %.1f 圓面積: %.1f' % (r, area))


if __name__ == '__main__':
    try:
        user_input()
    except ValueError as e:
        print('請輸入整數數字')
    # -----------------------
    try:
        user_input()
    except ValueError as e:
        print('請輸入整數數字')