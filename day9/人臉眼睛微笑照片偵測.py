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



# -------------------------------------------------------------------------