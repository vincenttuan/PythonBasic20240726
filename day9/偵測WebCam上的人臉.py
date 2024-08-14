import cv2  # 匯入 opencv 資源

# 人臉哈爾特徵檔
face_cascade = cv2.CascadeClassifier('ai/xml/haarcascade_frontalface_default.xml')

# 設定 WebCam
cap = cv2.VideoCapture(0)  # 0, 1, 2, ...

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

while True:
    ret, frame = cap.read()
    # print(ret, frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=15, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        # 繪製框線
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # 在框線上面撰寫文字
        cv2.putText(frame, 'Teacher', (x, y-5), 16, 1.2, (255, 0 , 0), 2)

    cv2.imshow('My Face', frame)
    # 按下 'q' 離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()