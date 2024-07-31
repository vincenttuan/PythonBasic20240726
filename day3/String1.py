# 字串分析-基礎
words = "she sell sea shell on the sea shore"
print(words)
print("有幾個字元(含空白):", len(words))
print("有幾個 s 字元:", words.count("s"))
print("有幾個 sea:", words.count("sea"))
print("有幾個 land:", words.count("land"))
print("sea 的位置:", words.find("sea"))
print("land 的位置:", words.find("land"))
