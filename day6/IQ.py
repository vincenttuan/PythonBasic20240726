# 抓取網路資源
import requests

# 圖像 url
image_url = 'https://raw.githubusercontent.com/vincenttuan/PythonBasic20240726/main/iq/1.png'
# IQ 1 ~ 10 答案
answers = {1: 'F', 2: 'D', 3: 'B', 4: 'A', 5: 'E', 6: 'E', 7: 'B', 8: 'B', 9: 'F', 10: 'C'}

# 使用 Get 請求來得到圖片資訊
# response 得到回應
response = requests.get(image_url)

# 檢查回應是否成功?(成功時會得到 HTTP 狀態碼 200)
if response.status_code == 200:
    print("成功")
    # 將圖片資料寫入到指定檔案中(w: 寫入, b: 二進位資料(例如:圖片))
    file = open('1.png', 'wb')
    file.write(response.content)  # 將網路回樣的內容寫入到檔案中

else:
    print("失敗")

