# 字串分析-字串切割
words = "she sell sea shell on the sea shore"
# 請問 words 字串中有幾個單字 ?
result = words.split(" ")  # 利用 split 來切割字串, result 則會存放切割後的結果
print(result)
print(type(result))
print("有幾個單字:", len(result))
print("第一個單字:", result[0])
print("第二個單字:", result[1])
print("最後一個單字:", result[7])
print("最後一個單字:", result[len(result) - 1])
