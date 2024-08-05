# 1.請印出 2~100 有哪些值數 ?
# 2.上述範圍的質數有幾個 ?
# 3.上述範圍的質數總和為何 ?
from day5.ForLoop4 import check_prime

if __name__ == '__main__':
    count = 0  # 紀錄質數有幾個
    total = 0  # 紀錄質數的總和
    # ------------------------
    for n in range(2, 101):
        if check_prime(n):
            print(n)  # 印出質數
            count += 1  # 累計質數個數
            total += n  # 累計加總質數
    # ------------------------
    print("質數個數: %d" % count)
    print("質數總和: %d" % total)
    print("平均值: %.1f" % (total/count))

