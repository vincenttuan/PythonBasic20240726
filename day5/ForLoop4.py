# 判斷質數改良版
# 自訂函式: 判斷 n 值是否是值數?
def check_prime(n):
    # --------------------------------
    for i in range(2, n//2):
        if n % i == 0:
            return False  # 不是質數
    # --------------------------------
    return True  # 是質數


# 主程式
if __name__ == '__main__':
    n = 47
    if check_prime(n):
        print("%d 是質數" % n)
    else:
        print("%d 不是質數" % n)




