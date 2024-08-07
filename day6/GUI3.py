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
    global timer  # 取得主程式所宣告的 timer 變數
    if timer == None:  # 判斷 timer 是否是空的
        timer = win.after(5000, game_over)  # 計時 5秒鐘, 時間到就會執行 game_over 函式

    # 取得目前 number 變數中的內容
    current_value = int(number.get())
    # +1 變成新資料
    new_value = current_value + 1
    # 將 new_value 傳為字串之後設定到 number 中
    number.set(str(new_value))

def game_over():
    add_button.config(state=tkinter.DISABLED)  # add 按鈕不可以按
    messagebox.showinfo('訊息視窗', 'Game Over')

def win_exit():
    win.quit()

if __name__ == '__main__':
    # 計時器變數
    timer = None

    win = tkinter.Tk()
    win.title("Click 我超強")
    win.geometry("300x300")
    # 設定變數
    number = tkinter.StringVar()  # 字串參照物件(tkinter專用)
    number.set('0')
    # label 配置
    label = tkinter.Label(win, textvariable=number, bg='green', fg='yellow',
                          font='Arial, 60', width=30, height=3)
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






