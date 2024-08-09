import tkinter
from tkinter import font

if __name__ == '__main__':
    win = tkinter.Tk()
    # 設定字型, 大小, 風格
    myfont = font.Font(family='Arial', size=20, weight='bold')
    # 宣告按鈕
    input_entry = tkinter.Entry(font=myfont, justify=tkinter.RIGHT)
    # -------------------------------------------------------------
    btn1 = tkinter.Button(text='1', font=myfont)
    btn2 = tkinter.Button(text='2', font=myfont)
    btn3 = tkinter.Button(text='3', font=myfont)
    btn_add = tkinter.Button(text='+', font=myfont)
    # -------------------------------------------------------------
    btn4 = tkinter.Button(text='4', font=myfont)
    btn5 = tkinter.Button(text='5', font=myfont)
    btn6 = tkinter.Button(text='6', font=myfont)
    btn_sub = tkinter.Button(text='-', font=myfont)
    # -------------------------------------------------------------
    btn7 = tkinter.Button(text='7', font=myfont)
    btn8 = tkinter.Button(text='8', font=myfont)
    btn9 = tkinter.Button(text='9', font=myfont)
    btn_calc = tkinter.Button(text='=', font=myfont)
    # -------------------------------------------------------------
    btn_mul = tkinter.Button(text='*', font=myfont)
    btn0 = tkinter.Button(text='0', font=myfont)
    btn_div = tkinter.Button(text='/', font=myfont)
    # -------------------------------------------------------------
    # 按鈕布局
    # EWNS: 無縫隙元件填滿
    input_entry.grid(row=0, column=0, columnspan=4, sticky='EWNS')
    # -------------------------------------------------------------
    btn1.grid(row=1, column=0, sticky='EWNS')
    btn2.grid(row=1, column=1, sticky='EWNS')
    btn3.grid(row=1, column=2, sticky='EWNS')
    btn_add.grid(row=1, column=3, sticky='EWNS')
    # -------------------------------------------------------------
    btn4.grid(row=2, column=0, sticky='EWNS')
    btn5.grid(row=2, column=1, sticky='EWNS')
    btn6.grid(row=2, column=2, sticky='EWNS')
    btn_sub.grid(row=2, column=3, sticky='EWNS')
    # -------------------------------------------------------------
    btn7.grid(row=3, column=0, sticky='EWNS')
    btn8.grid(row=3, column=1, sticky='EWNS')
    btn9.grid(row=3, column=2, sticky='EWNS')
    btn_calc.grid(row=3, column=3, rowspan=2, sticky='EWNS')
    # -------------------------------------------------------------
    btn_mul.grid(row=4, column=0, sticky='EWNS')
    btn0.grid(row=4, column=1, sticky='EWNS')
    btn_div.grid(row=4, column=2, sticky='EWNS')
    # -------------------------------------------------------------
    win.mainloop()

