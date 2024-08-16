# 台灣證券交易所：每日個股日本益比、殖利率及股價淨值比
# https://www.twse.com.tw/zh/page/trading/exchange/BWIBBU_d.html
# 證券代號,證券名稱,殖利率(%),股利年度,本益比,股價淨值比,財報年/季,

import requests
import datetime

def twii(year, month, day):
    url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=%s&selectType=ALL'
    date = datetime.datetime(year, month, day)  # 日期格式
    date_str = date.strftime('%Y%m%d')  # 將日期格式轉字串
    print(date_str)
    url = url % date_str
    print(url)
    # ----------------------------
    # 取得 csv 資料
    csv = requests.get(url).text
    print(csv)

if __name__ == '__main__':
    twii(2024, 8, 15)





