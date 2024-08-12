# QRCode 產生器
# 記得要先安裝 qrcode 套件
import qrcode
import base64

# 將明碼的資料編碼成 base64
def encode_to_base64(data):
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

# 建立 qrcode
qr = qrcode.QRCode(version=1, box_size=10, border=5)
data = "可樂 1 瓶 35 元"
# 透過 base64 編碼
data = encode_to_base64(data)
# ---------------------------------------------------
qr.add_data(data)  # 將 data 明碼寫入到 qrcode 中
qr.make(fit=True)  # qr 碼最適化
# ---------------------------------------------------
# 建立 qrcode 圖檔
img = qr.make_image(fill_color="#000000", back_color="#FFFFFF")
img.save("test_qr.png")  # 存檔
# ---------------------------------------------------
print("qrcode 原始內容:", data)
print("test_qr.png 圖檔產生成功 ! 請用手機掃描")


