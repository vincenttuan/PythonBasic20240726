# 台灣證券交易所：每日個股日本益比、殖利率及股價淨值比
# https://www.twse.com.tw/zh/page/trading/exchange/BWIBBU_d.html
# 證券代號,證券名稱,殖利率(%),股利年度,本益比,股價淨值比,財報年/季,

import requests
import datetime
url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=%s&selectType=ALL'

