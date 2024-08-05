# 奧運跳水計分邏輯
# 10 個裁判, 每一個裁判評分0~10
# 去掉最高與最低分數各二個之後, 中間六筆資料計算平均

# 自訂函式: 計算平均
def calaulate_average(scores):
    sorted_scores = sorted(scores)  # 資料由小到大排序
    trimmed_scores = sorted_scores[2:-2]
    # 計算平均(sum() 自動加總, len() 得到個數)
    average_score = sum(trimmed_scores) / len(trimmed_scores)
    return average_score


# 主程式
if __name__ == '__main__':
    # 10 個裁判評分
    scores = [5, 8, 7, 6, 9, 4, 6, 7, 8, 5]
    # 計算平均分數
    average_score = calaulate_average(scores)
    # 印出平均分數
    print("平均分數: %.1f" % average_score)
