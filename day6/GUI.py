# 利用 tkinter 套件來實現 GUI
import tkinter

if __name__ == '__main__':
    # 建立視窗物件
    win = tkinter.Tk()

    # 設定視窗上方標題
    win.title('我的小視窗')

    # 設定視窗大小(寬x高)
    win.geometry('300x300')

    # 啟用視窗主程序
    win.mainloop()
