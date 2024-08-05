# for 迴圈 (步進迴圈, 一步一步做)
# 印出 1~5 的數字
for i in range(1, 6):  # i 的內容會從 1 開始到小於 6
    print("i=%d" % i)

# 練習利用 for 迴圈如何印出 5 個 python
for i in range(1, 6):
    print("Python")

# 練習利用 for 迴圈如何計算 1~10 的總和與平均 ?
total = 0  # 總和累計
for i in range(1, 11):
    total += i  # total = total + i

print(total, total/10)
