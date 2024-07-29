# if else 簡單表達式

score = 75
print(score)
# 利用一般表達式-----------------------------
if score >= 60:
    print("及格")
else:
    print("不及格")
# 利用簡單表達式 1---------------------------
print("及格" if score >= 60 else "不及格")
# 利用簡單表達式 2---------------------------
result = "及格" if score >= 60 else "不及格"
print(result)
