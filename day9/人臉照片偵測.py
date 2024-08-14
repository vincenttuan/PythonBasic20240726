import cv2  # 匯入 opencv 資源

# 人臉哈爾特徵檔
face_cascade = cv2.CascadeClassifier('ai/xml/haarcascade_frontalface_default.xml')

# 讀取影像
frame = cv2.imread('ai/image/girl.jpg')

# 印出影像原始資料
print(frame)

# -----------------------------------------------------
# 人臉辨識, 得到臉部的 (x, y, w, h)
faces = face_cascade.detectMultiScale(
    frame,  # 目標圖片(待偵測的圖像資訊)
    scaleFactor=1.1,  # 檢測粒度(最小: 1.1)
    minNeighbors=15,  # 重複檢測次數, 針對解析度高的圖片要調高, 反之調低)
    minSize=(30, 30),  # 搜尋比對最小尺寸
    flags=cv2.CASCADE_SCALE_IMAGE  # 偵測影像 image
)
print("臉部座標 (x, y, w, h):", faces)

# 在 face 上畫出矩形
for (x, y, w, h) in faces:
    # (x, y) 左上角, (x+w, y+h) 右下角, (0, 0, 255) BGR 顏色, 5: 框線寬度
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)


# -----------------------------------------------------

# 顯示圖片
cv2.imshow('My Image', frame)

# 在圖片上按下任意鍵離開(例如: q)
c = cv2.waitKey(0)
