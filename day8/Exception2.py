# 例外處理
x = 10
y = input('請輸入分母:')  # 得到字串資料
try:
    y = int(y)  # 轉型後得到整數資料
    result = 10 / y
except Exception as e:
    print('y 有錯誤')
    print('錯誤訊息', e)
    print('錯誤類型', e.__class__)
else:
    print(result)  # 當 result 沒有錯誤才會執行


