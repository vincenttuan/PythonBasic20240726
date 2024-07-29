# 輸入測試
# 使用者輸入身高體重, 得出 bmi
h = input('請輸入身高:')
print(h, type(h))  # 印出 h 的內容與資料型態
h = int(h)  # 將 str (字串) 轉 int (整數)
print(h, type(h))  # 印出 h 的內容與資料型態
# ---------------------------------------
w = int(input('請輸入體重:'))  # 直接轉型
print(w, type(w))
# ---------------------------------------
bmi = w / (h/100)**2
print("BMI:", bmi)
print("BMI: %.2f" % bmi)

