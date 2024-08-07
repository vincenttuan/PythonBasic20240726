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
    hello_label = tkinter.Label(win, text='Hello !')
    hello_label.pack()  # 配置到視窗中
    ok_button = tkinter.Button(win, text="OK")
    ok_button.pack(side=tkinter.LEFT)  # 配置到視窗左側
    exit_button = tkinter.Button(win, text="Exit")
    exit_button.pack(side=tkinter.RIGHT)  # 配置到視窗右側
    # ------------------------------------------------
    win.mainloop()

