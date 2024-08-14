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

# -------------------------------------------------------------------------

# 顯示圖片
cv2.imshow('My Image', frame)

# 在圖片上按下任意鍵離開(例如: q)
c = cv2.waitKey(0)
