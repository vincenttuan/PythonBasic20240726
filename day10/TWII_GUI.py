import tkinter as tk  # tk 具有傳統外觀
from tkinter import ttk, scrolledtext  # ttk 具有現代外觀
import requests
import datetime

if __name__ == '__main__':
    # 建立主視窗
    root = tk.Tk()
    root.title("台灣證券交易所數據查詢")

    # 建立主框架
    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # 第一列 -----------------------------------------------------------------
    # 建立年份
    ttk.Label(main_frame, text="年份").grid(row=0, column=0, padx=5, pady=5)
    year_entry = ttk.Entry(main_frame, width=10)
    year_entry.grid(row=0, column=1, padx=5, pady=5)

    # 建立月份
    ttk.Label(main_frame, text="月份").grid(row=0, column=2, padx=5, pady=5)
    month_entry = ttk.Entry(main_frame, width=10)
    month_entry.grid(row=0, column=3, padx=5, pady=5)

    # 建立日期
    ttk.Label(main_frame, text="日期").grid(row=0, column=4, padx=5, pady=5)
    day_entry = ttk.Entry(main_frame, width=10)
    day_entry.grid(row=0, column=5, padx=5, pady=5)

    # 第二列 -----------------------------------------------------------------
    # 殖利率
    ttk.Label(main_frame, text="殖利率").grid(row=1, column=0, padx=5, pady=5)
    yield_rate_entry = ttk.Entry(main_frame, width=10)
    yield_rate_entry.grid(row=1, column=1, padx=5, pady=5)

    # 本益比
    ttk.Label(main_frame, text="本益比").grid(row=1, column=2, padx=5, pady=5)
    pe_entry = ttk.Entry(main_frame, width=10)
    pe_entry.grid(row=1, column=3, padx=5, pady=5)

    # 股價淨值比
    ttk.Label(main_frame, text="股價淨值比").grid(row=1, column=4, padx=5, pady=5)
    pb_entry = ttk.Entry(main_frame, width=10)
    pb_entry.grid(row=1, column=5, padx=5, pady=5)

    # 啟動 GUI 循環
    root.mainloop()
