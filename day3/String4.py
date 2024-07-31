# 字串切割
message = "170, 60.5"  # 表示身高, 體重
# 請利用 split 來析出身高, 體重並計算 BMI = ?
datas = message.split(", ")
print(datas)  # ['170', '60.5']
h = float(datas[0]) / 100
w = float(datas[1])
bmi = w / h**2
print("身高m:", h)
print("身高cm:", h*100)
print("體重kg:", w)
print("BMI: %.2f" % bmi)




