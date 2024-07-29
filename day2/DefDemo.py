# 自訂函式
# 打招呼的函式
def message(name):
    print("Hello", name)


def calc_bmi(h, w):
    bmi = w / (h/100)**2
    result = "過重" if bmi > 23 else "過輕" if bmi <= 18 else "正常"
    print("身高:%d 體重:%d BMI:%.2f 體重%s" % (h, w, bmi, result))


# Python 主程式
if __name__ == '__main__':
    message("John")
    message("Mary")
    calc_bmi(170, 60)
    calc_bmi(165, 48)
    calc_bmi(185, 90)

