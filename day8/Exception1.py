# 例外處理
x = 10
y = input('請輸入分母:')  # 得到字串資料
try:
    y = int(y)  # 轉型後得到整數資料
    result = 10 / y
except:
    print('y 有錯誤')
else:
    print(result)  # 當 result 沒有錯誤才會執行


