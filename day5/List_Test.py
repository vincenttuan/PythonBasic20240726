# 數組
# []     List 列表, value元素可以重複
# set()  Set 列表, value元素不可以重複
# dict() 字典列表, (key/value 形式存放) key 不可重複, value 可以重複

scores = [100, 50, 70, 50, 30]
#          0   1   2   3   4  <-- 位置(維度)
print(scores)            # [100, 50, 70, 50, 30]
# 變更元素位置=1的內容為 95
scores[1] = 95
print(scores)            # [100, 95, 70, 50, 30]
# 增加元素
scores.append(60)
print(scores)            # [100, 95, 70, 50, 30, 60]
# 移除元素內容 = 30 的元素
scores.remove(30)        # [100, 95, 70, 50, 60]
print(scores)
# 移除指定位置的元素
scores.__delitem__(2)  # 移除指定位置=2的元素
print(scores)            # [100, 95, 50, 60]
# -----------------------------------------
