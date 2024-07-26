# 今有雞、兔同籠，上有三十五頭，下九十四足。問雉、兔各幾何？
total = 35  # 變數, 用來記錄或儲存資料使用
feet = 94  # 變數, 用來記錄或儲存資料使用
rabbit = (feet - total * 2) / (4-2)
chicken = total - rabbit
print(rabbit, chicken)
