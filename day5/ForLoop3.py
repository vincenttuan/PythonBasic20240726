# 判斷質數
n = 47  # 是否是質數
is_prime = True  # 預設是質數
# 觀察餘數 ------------------------------------
for i in range(2, n):
    #print("%d %% %d = %d" % (n, i, (n % i)))
    if n % i == 0:
        is_prime = False  # 不是質數
        break  # 跳離迴圈
# 判斷結果 ------------------------------------
if is_prime:  # if is_prime == True
    print("%d 是質數" % n)
else:
    print("%d 不是質數" % n)
