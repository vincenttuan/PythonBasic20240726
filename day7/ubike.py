import requests
import json

from day7.Great_circle_distance import get_distance

# 台北市 ubike 即時資料 json 格式
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
# 取得所有 ubike 站台列表資料
ubike_list = json.loads(requests.get(url).text)
print("台北市 ubike 即時資料筆數: %d" % len(ubike_list))
#print(ubike_list)  # 印出所有 ubike 資料
# 台北市忠孝東路四段169號
lat1, lon1 = 25.04190, 121.55050
# --------------------------------------------------------------------------------------
for ubike in ubike_list:
    lat2, lon2 = ubike['latitude'], ubike['longitude']
    distance = get_distance(lat1, lon1, lat2, lon2)
    if distance <= 200 and ubike['available_rent_bikes'] > 1:
        print("距離: %dm 站名: %s 地址: %s 全部: %d 可借: %d 可還: %d" % (
            distance, ubike['sna'], ubike['ar'], ubike['total'],
            ubike['available_rent_bikes'], ubike['available_return_bikes']
        ))

