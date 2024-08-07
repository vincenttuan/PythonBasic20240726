import tkinter
from tkinter import messagebox
# 利用 thinker 來顯示 GUI
'''
    +------------+
    |     0      |
    | Add   Exit |
    +------------+
按下 Add 上方數字會自動 + 1
按下 Exit 會離開視窗
'''
def add():
    pass

def game_over():
    pass

def win_exit():
    pass

if __name__ == '__main__':
    win = tkinter.Tk()
    win.title("Click 我超強")
    win.geometry("300x300")
    # 設定變數
    number = tkinter.StringVar()  # 字串參照物件(tkinter專用)
    number.set(0)
    # label 配置
    label = tkinter.Label(win, textvariable=number, bg='green', fg='yellow',
                          font='Arial, 30', width=30, height=5)
    label.pack()
    # button 配置
    add_button = tkinter.Button(win, text="Add", font="Arial, 20",
                                width=10, height=2, command=add)
    exit_button = tkinter.Button(win, text="Exit", font="Arial, 20",
                                width=10, height=2, command=win_exit)
    add_button.pack(side=tkinter.LEFT)
    exit_button.pack(side=tkinter.RIGHT)
    # 視窗運行
    win.mainloop()






