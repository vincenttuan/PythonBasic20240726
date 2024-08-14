import cv2

# 人臉哈爾特徵檔
face_cascade = cv2.CascadeClassifier('ai/xml/haarcascade_frontalface_default.xml')

# 眼睛哈爾特徵檔
eye_cascade = cv2.CascadeClassifier('ai/xml/haarcascade_eye.xml')

# 微笑哈爾特徵檔
smile_cascade = cv2.CascadeClassifier('ai/xml/haarcascade_smile.xml')

# 讀取影像
frame = cv2.imread('ai/image/girl.jpg')

# 將彩色影像轉灰階, 可以增加辨識效率
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# -------------------------------------------------------------------------
# 人臉偵測
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=15, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE
)

# 在 face 上畫出矩形
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # 偵測眼睛 (要在 for 裡面)
    # 建立 roi 人臉區域 (因為要在人臉內部偵測眼睛)
    roi_color = frame[y:y+h, x:x+w]  # 人臉的有效區域-彩色版
    roi_gray = gray[y:y+h, x:x+w]  # 人臉的有效區域-灰階版
    # 進行人臉內的眼睛偵測
    eyes = eye_cascade.detectMultiScale(
        roi_gray, scaleFactor=1.1, minNeighbors=15, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE
    )
    # 進行眼睛矩形繪製
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    # ---------------------------------------------------------------------
    # 進行微笑偵測
    smile = smile_cascade.detectMultiScale(
        roi_gray, scaleFactor=1.1, minNeighbors=15, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE
    )
    # 進行微笑矩形繪製
    for (sx, sy, sw, sh) in smile:
        cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 2)

# -------------------------------------------------------------------------

# 顯示圖片
cv2.imshow('My Image', frame)

# 在圖片上按下任意鍵離開(例如: q)
c = cv2.waitKey(0)
