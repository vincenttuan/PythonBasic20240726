import qrcode  # 生成 QRCode
from PIL import Image  # 用於打開與處理圖像檔案
from pyzbar.pyzbar import decode  # 用於 QRCode 解碼
import base64

def read_qrcode(filename):
    # 打開 QR 碼圖像
    img = Image.open(filename)
    # 嘗試解碼 QRCode
    try:
        decoded_objects = decode(img)
        if decoded_objects:  #  有偵測到 QRCode
            # 取得 QRCode 解碼內容
            decoded_text = decoded_objects[0].data.decode('utf-8')
            print('解碼後的內容:', decoded_text)
            # ---------------------------------------------------------------------
            # 是否要用 base64 在進行解碼 ?
            choice = input('是否要用 base64 在進行解碼(y/n):')
            if choice == 'y':
                decoded_base64_text = base64.b64decode(decoded_text).decode('utf-8')
                print('Base64 解碼後的內容:', decoded_base64_text)
            # ---------------------------------------------------------------------
        else: #  沒有偵測到 QRCode
            print('檔案內有不含 QRCode')
    except Exception as e:
        print('解碼失敗', e)


if __name__ == '__main__':
    read_qrcode('test_qr.png')


