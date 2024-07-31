# 字串切割
message = "15, 8, 20"  # 代表長方體的長度、寬度和高度
# 求體積 = ?
parts = message.split(", ")
print(parts)
length = int(parts[0])  # 長度
width = int(parts[1])  # 寬度
height = int(parts[2])  # 高度
# 計算體積
volume = length * width * height
print("體積:", volume)
