# if 條件判斷
score = int(input('請輸入分數:'))
print("score: %d" % score)
# 判斷是否及格
if 60 <= score <= 100:
    print("及格")
elif 0 <= score < 60:
    print("不及格")
else:
    print("成績錯誤")
# -------------------------
# 判斷等第
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
elif 0 <= score < 60:
    print("F")
else:
    print("成績錯誤")
