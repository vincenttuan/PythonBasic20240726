import tkinter as tk  # tk 具有傳統外觀
from tkinter import ttk, scrolledtext  # ttk 具有現代外觀
import requests
import datetime

def twii(year, month, day, yield_rate, pe, pb):
    """
    查詢台灣證券交易所的數據
    :param year: 年份
    :param month: 月份
    :param day: 日期
    :param yield_rate: 殖利率
    :param pe: 本益比
    :param pb: 股價淨值比
    :return: 符合條件的股票列表
    """
    # 構建 URL，%s 是一個佔位符，稍後會被替換為實際的日期
    url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=%s&selectType=ALL'
    # 將年月日轉換為 datetime 對象
    date = datetime.datetime(year, month, day)
    # 將 datetime 對象格式化為 YYYYMMDD 的字符串
    date_str = date.strftime('%Y%m%d')
    # 將日期字符串插入到 URL 中
    url = url % date_str

    # 發送 GET 請求獲取 CSV 數據
    csv = requests.get(url).text
    # 清理數據：移除雙引號，將 '-' 替換為 '-1'
    csv = csv.replace('"', '').replace('-', '-1')

    results = []
    # 按行分割 CSV 數據
    for row in csv.split('\r\n'):
        # 將每行分割為列表
        list = row.split(',')
        # 檢查是否為有效的數據行（8個元素且不是標題行）
        if len(list) == 8 and list[0] != '證券代號':
            # 檢查是否符合條件
            if float(list[2]) > yield_rate and float(list[4]) < pe and float(list[5]) < pb:
                # 將符合條件的行添加到結果列表
                results.append(','.join(list))

    return results

def search():
    # 取得用戶的輸入資訊
    year = int(year_entry.get())
    month = int(month_entry.get())
    day = int(day_entry.get())
    yield_rate = float(yield_rate_entry.get())
    pe = float(pe_entry.get())
    pb = float(pb_entry.get())

    # 執行查詢 twii 方法
    results = twii(year, month, day, yield_rate, pe, pb)

    # 先清空結果視窗
    result_text.delete(0, tk.END)

    # 插入標題列
    result_text.insert(tk.END, "證券代號,證券名稱,殖利率(%),股利年度,本益比,股價淨值比,財報年/季\n")

    # 插入查詢結果
    for result in results:
        result_text.insert(tk.END, result + "\n")




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

    # 查詢按鈕
    search_button = ttk.Button(main_frame, text='查詢', command=search)
    search_button.grid(row=2, column=0, columnspan=6, pady=10)

    # 放置結果資料區
    result_text = scrolledtext.ScrolledText(main_frame, width=80, height=20)
    result_text.grid(row=3, column=0, columnspan=6, padx=5, pady=5)

    # 啟動 GUI 循環
    root.mainloop()
