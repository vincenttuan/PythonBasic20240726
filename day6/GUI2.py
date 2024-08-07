import tkinter
'''
    +--------+
    |  Label |
    | B1  B2 |
    +--------+
'''
if __name__ == '__main__':
    # 視窗建立與設定------------------------------------
    win = tkinter.Tk()
    win.title('我的小小視窗')
    win.geometry('300x200')
    # 元件配置-----------------------------------------
    hello_label = tkinter.Label(win,
                                text='Hello !',    # 標籤文字
                                font='Arial, 30',  # 字型大小
                                bg='green',        # 背景顏色
                                fg='yellow',       # 前景顏色
                                width=15,          # 標籤寬度
                                height=2)          # 標籤高度
    hello_label.pack()  # 配置到視窗中
    ok_button = tkinter.Button(win, text="OK", font='Arial, 30')
    ok_button.pack(side=tkinter.LEFT)  # 配置到視窗左側
    exit_button = tkinter.Button(win, text="Exit", font='Arial, 30')
    exit_button.pack(side=tkinter.RIGHT)  # 配置到視窗右側
    # ------------------------------------------------
    win.mainloop()

