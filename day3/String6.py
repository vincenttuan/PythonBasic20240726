# 字串切割
# A, B 二人段考(國文,英文)成績
message = "100,40#90,60"  # A學生國文100,英文40 # B學生國文90,英文60
# 請問那一位學生成績較優
parts = message.split("#")
print(parts)
a_scores = parts[0]  # A 學生成績 '100,40'
b_scores = parts[1]  # B 學生成績 '90,60'
print("A 學生成績:", a_scores)
print("B 學生成績:", b_scores)
# --------------------------------------
a = a_scores.split(",")  # ['100', '40']
a_chinese = int(a[0])
a_english = int(a[1])
# --------------------------------------
b = b_scores.split(",")  # ['90', '60']
b_chinese = int(b[0])
b_english = int(b[1])
# --------------------------------------
a_sum = a_chinese + a_english  # A學生總分
b_sum = b_chinese + b_english  # B學生總分
print("A學生總分:", a_sum)
print("B學生總分:", b_sum)
# -------------------------------------------------
if a_sum > b_sum:
    print("A 學生成績較優")
else:
    print("B 學生成績較優")
# -------------------------------------------------
print("A" if a_sum > b_sum else "B", "學生成績較優")
