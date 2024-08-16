# 台灣證券交易所：每日個股日本益比、殖利率及股價淨值比
# https://www.twse.com.tw/zh/page/trading/exchange/BWIBBU_d.html
# 證券代號,證券名稱,殖利率(%),股利年度,本益比,股價淨值比,財報年/季,

import requests
import datetime

# year, month, day, yield_rate 殖利率, pe 本益比, pb 股價淨值比
def twii(year, month, day, yield_rate, pe, pb):
    url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=%s&selectType=ALL'
    date = datetime.datetime(year, month, day)  # 日期格式
    date_str = date.strftime('%Y%m%d')  # 將日期格式轉字串
    print(date_str)
    url = url % date_str
    print(url)
    # ----------------------------
    # 取得 csv 資料
    csv = requests.get(url).text
    # print(csv)
    # ----------------------------
    # 過濾雜訊
    csv = csv.replace('"', '')  # 移除雙引號
    csv = csv.replace('-', '-1')  # 將 - 轉換成 -1
    # print(csv)
    # ----------------------------
    # 資料分析
    print('證券代號,證券名稱,殖利率(%),股利年度,本益比,股價淨值比,財報年/季')
    for row in csv.split('\r\n'):  # 逐行切割
        list = row.split(',')
        if len(list) == 8 and list[0] != '證券代號':
            # print(list)
            if float(list[2]) > yield_rate and float(list[4]) < pe and float(list[5]) < pb:
                print(list)



if __name__ == '__main__':
    twii(2024, 8, 15, 7, 10, 1)
    print('----------------------------------------------------')
    twii(2024, 8, 15, 7, 20, 5)




