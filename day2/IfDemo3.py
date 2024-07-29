# if else 簡單表達式嵌套版本
score = 95
print(score)
# 一般表達式 ----------------------
if score >= 90:
    print("優等")
elif score >= 60:
    print("及格")
else:
    print("不及格")
# 簡單表達式 ----------------------
result = "優等" if score >= 90 else "及格" if score >= 60 else "不及格"
print(result)
