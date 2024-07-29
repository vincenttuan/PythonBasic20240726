# 數學套件-距離公式
import math

x1, y1 = 10, 10  # A 點
x2, y2 = 30, 20  # B 點
print("A點座標:", x1, y1)
print("A點座標:(%d, %d)" % (x1, y1))

print("B點座標:", x2, y2)
print("B點座標:(%d, %d)" % (x2, y2))

dx = (x1 - x2)**2
# dx = math.pow(x1 - x2, 2)

dy = (y1 - y2)**2
# dy = math.pow(y1 - y2, 2)

d = math.sqrt(dx + dy)  # 開根號
print("距離:", d)
print("距離:%f" % d)  # 預設到小數點6位會自動四捨五入
print("距離:%.2f" % d)  # 設到小數點2位會自動四捨五入
print("距離:%.1f" % d)  # 設到小數點1位會自動四捨五入



