# 例外處理應用
# 使用者輸入半徑之後可以計算出圓面積
import math

def user_input():
    r = input('請輸入半徑:')
    r = float(r)  # 字串轉浮點數
    area = r ** 2 * math.pi
    print('半徑: %.1f 圓面積: %.1f' % (r, area))


if __name__ == '__main__':
    user_input()
