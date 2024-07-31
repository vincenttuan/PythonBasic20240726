# 字串分析-字串切割
message = "100,90"  # 表示國文與數學的分數
print(message, type(message))
scores = message.split(",")  # 切割字串
print(scores, type(scores))  # 印出列表資料
print(scores[0], scores[1])  # 印出列表元素資料
print(type(scores[0]), type(scores[1]))  # 印出列表元素型態
print(scores[0] + scores[1])  # 10090 (列表元素相加, 因為是字串所以 + 會變成連結符號)
# 要利用 int() 來轉型
print(int(scores[0]) + int(scores[1]))  # 190
# 也可以利用 float() 來轉型
print(float(scores[0]) + float(scores[1]))  # 190.0
# 將國文與數學存放在指定變數中
chinese = float(scores[0])  # 國文成績
math = float(scores[1])  # 數學成績
# 進行分析
summary = chinese + math  # 總分
average = (chinese + math) / 2  # 平均
print("國文:", chinese)
print("數學:", math)
print("總分:", summary)
print("平均:", average)

