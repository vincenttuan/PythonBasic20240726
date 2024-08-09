import requests
import json

# 台北市 ubike 即時資料 json 格式
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
# 取得所有 ubike 站台列表資料
ubike_list = json.loads(requests.get(url).text)
print("台北市 ubike 即時資料筆數: %d" % len(ubike_list))
#print(ubike_list)  # 印出所有 ubike 資料
for ubike in ubike_list:
    distance = 0
    print("距離: %d 站名: %s 地址: %s 全部: %d 可借: %d 可還: %d" % (
        distance, ubike['sna'], ubike['ar'], ubike['total'],
        ubike['available_rent_bikes'], ubike['available_return_bikes']
    ))

