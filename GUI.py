#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
import sys
import os
from plot import plot_figs


def botton_label_1():
    global entry_1
    return entry_1.get


def botton_label_2():
    global entry_2
    return entry_2.get


def delete():
    entry_1.delete(first=0, last=100)
    entry_2.delete(first=0, last=100)
    entry_3.delete(first=0, last=100)
    entry_4.delete(first=0, last=100)

def allcommand():
    s1 = var_1.get()
    s2 = var_2.get()
    s3 = var_3.get()
    s4 = var_4.get()
    plot_figs(s1, s2, s3, s4)
    # os.system("python for_plot.py --file={} --plot={}".format(s1, s2))


window = tk.Tk()
window.title('月報圖表參數輸入')
window.geometry('445x350') #'410x350')
#window.iconbitmap('C:/Users/Yuwen.Fang/Documents/Dihua/icons/stantec.ico')

# progress bar
# bar = ttk.Progressbar(window)
# bar.grid(row=12, column=0,columnspan=2, sticky='we')
# bar.start(100)

# var_1 = tk.StringVar()
# var_2 = tk.StringVar()

label_00 = tk.Label(
    window, text='_______________________________________________________________________________________')
label_01 = tk.Label(window, text=' 此執行檔為繪製月報圖表之用，故請在以下輸入')
label_02 = tk.Label(window, text=' [各式檔案的所在位置]以及[您希望圖表的存放位置]，')
label_03 = tk.Label(
    window, text=' 輸入格式請參照此範例: C:/Users/Documents/Dihua/  ("Dihua"為資料夾)')
label_04 = tk.Label(window, text=' ** 位置路徑可於資料夾點選右鍵 > 內容 > 位置獲得')
label_05 = tk.Label(window, text=' ** 建議將此執行檔以及各檔案下載至個人電腦')
label_06 = tk.Label(
    window, text='_______________________________________________________________________________________')



label_1 = tk.Label(window, text='>   請輸入各式檔案的所在位置: ')
label_2 = tk.Label(window, text='>   請輸入希望圖表的存放位置: ')
label_3 = tk.Label(window, text='>   民國年(例111): ')
label_4 = tk.Label(window, text='>   月份(二位數 例09): ')
var_1 = tk.StringVar()
var_2 = tk.StringVar()
var_3 = tk.StringVar()
var_4 = tk.StringVar()
entry_1 = tk.Entry(window, textvariable=var_1)
entry_2 = tk.Entry(window, textvariable=var_2)
entry_3 = tk.Entry(window, textvariable=var_3)  
entry_4 = tk.Entry(window, textvariable=var_4)
button_1 = tk.Button(window, text='繪   圖',
                     activebackground='orange', command=allcommand)
button_2 = tk.Button(window, text='重新輸入',
                     activebackground='orange', command=delete)
button_3 = tk.Button(window, text='離   開',
                     activebackground='orange', command=window.destroy)


# 介面設定
label_00.grid(row=0, column=0, columnspan=2, sticky='w')
label_01.grid(row=1, column=0, columnspan=2, sticky='w')
label_02.grid(row=2, column=0, columnspan=2, sticky='w')
label_03.grid(row=3, column=0, columnspan=2, sticky='w')
label_04.grid(row=4, column=0, columnspan=2, sticky='w')
label_05.grid(row=5, column=0, columnspan=2, sticky='w')
label_06.grid(row=6, column=0, columnspan=2, sticky='w')

label_1.grid(row=7, column=0, sticky='e')
label_2.grid(row=8, column=0, sticky='e')
label_3.grid(row=9, column=0, sticky='e')
label_4.grid(row=10, column=0, sticky='e')
entry_1.grid(row=7, column=1, sticky='we')
entry_2.grid(row=8, column=1, sticky='we')
entry_3.grid(row=9, column=1, sticky='we')
entry_4.grid(row=10, column=1, sticky='we')

button_1.grid(row=11, column=0, columnspan=2, sticky='we')
button_2.grid(row=12, column=0, sticky='we')
button_3.grid(row=12, column=1, sticky='we')


window.mainloop()

