import matplotlib.pyplot as plt

# 字典格式(key/value)
# 學生成績字典列表
students = {'John': 90, 'Mary': 85, 'Jack': 100, 'Rose': 45, 'Helen': 72}
print(students)  # 印出所有資料
names = list(students.keys())  # 將所有 key 抓出後放到 list 列表中
print(names)  # ['John', 'Mary', 'Jack', 'Rose', 'Helen']
scores = list(students.values())  # 將所有 value 抓出後放到 list 列表中
print(scores)  # [90, 85, 100, 45, 72]
# -----------------------------------------------------------------------
# 繪製學生成績折線圖
plt.plot(names, scores)
# 設定圖標資訊
plt.title('Student score chart')
plt.xlabel('name')
plt.ylabel('score')
# 顯示圖形
plt.show()
