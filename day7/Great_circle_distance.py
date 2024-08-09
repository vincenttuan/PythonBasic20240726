import math

# 大圓距離
# lat1 緯度, lon1 經度, lat2 緯度, lon2 經度
def get_distance(lat1, lon1, lat2, lon2):
    # 地球半徑(m)
    R = 6371000

    # 將經緯度轉換為弧度
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # 緯度和經度的差值
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine 公式
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # 計算距離
    distance = R * c

    return distance


if __name__ == '__main__':
    # 台北市忠孝東路四段169號
    lat1, lon1 = 25.04190, 121.55050
    # 國父紀念館
    lat2, lon2 = 25.04012, 121.56008
    # 計算距離
    distance = get_distance(lat1, lon1, lat2, lon2)
    print("距離: %.1f m" % distance)

