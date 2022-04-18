# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:09:41 2021

@author: user1
"""

from tkinter import Label, Entry, Button, END, Text, Menu
import tkinter as tk
from  scipy.stats import chi2_contingency
import numpy as np
import scipy.stats

root = tk.Tk()
root.geometry('500x410+500+200')
root.title('卡方檢定(簡易)')

# 運算
def run1():
    a = int(input_1.get())
    b = int(input_2.get())
    c = int(input_3.get())
    d = int(input_4.get())
    k = np.array([[a, b], [c, d]])
    c1 = sum(k[0])
    c2 = sum(k[1])
    r1 = k[0][0] + k[1][0]
    r2 = k[0][1] + k[1][1]
    n = sum(k[0]) + sum(k[1])
    # 計算期望值細格數
    e11 = r1*c1/n
    e12 = r1*c2/n
    e21 = r2*c1/n
    e22 = r2*c2/n
    # 檢定
    if e11 > 5 and e12 > 5 and e21 > 5 and e22 > 5:
        # 卡方檢定
        chi = chi2_contingency(k)
        chi_value = round(chi[1], 3)
        if chi_value < 0.05:
            txt.insert(END, '適用檢定：卡方檢定\n')
            txt.insert(END, '檢定結果：顯著\n')
            txt.insert(END, 'P-Value：')
            txt.insert(END, chi_value)
        else:
            txt.insert(END, '適用檢定：卡方檢定\n')
            txt.insert(END, '檢定結果：不顯著\n')
            txt.insert(END, 'P-Value：')
            txt.insert(END, chi_value)
    else:
        # 費雪檢定
        fisher = scipy.stats.fisher_exact(k)
        fisher_value = round(fisher[1], 3)
        if fisher_value < 0.05:
            txt.insert(END, '適用檢定：費雪檢定\n')
            txt.insert(END, '檢定結果：顯著\n')
            txt.insert(END, 'P-Value：')
            txt.insert(END, fisher_value)
        else:
            txt.insert(END, '適用檢定：費雪檢定\n')
            txt.insert(END, '檢定結果：不顯著\n')
            txt.insert(END, 'P-Value：')
            txt.insert(END, fisher_value)
    #s = chi2_contingency(k)
    #txt.insert(END, s[0])
    #txt.insert(END, s[1])
    input_1.delete(0, END)
    input_2.delete(0, END)
    input_3.delete(0, END)
    input_4.delete(0, END)
# 清除  
def clearTextInput():
    txt.delete("1.0", "end")


# 選單
mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label='簡易')     
# mainmenu.add_command(label='aaa')
# 標籤名稱
label_1 = Label(root, text='請輸入四個正整數', font=('標楷體', 16))
label_1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)
# 輸入框_1
input_1 = Entry(root, font=('Times New Roman', 12))
input_1.place(relx=0.1, rely=0.18, relwidth=0.3, relheight=0.08)
la1 = Label(root, text="目標合格件數", font=('標楷體', 14))
la1.place(relx=0.1, rely=0.25, relwidth=0.3, relheight=0.08)
# 輸入框_2
input_2 = Entry(root, font=('Times New Roman', 12))
input_2.place(relx=0.6, rely=0.18, relwidth=0.3, relheight=0.08)
la2 = Label(root, text="目標不合格件數", font=('標楷體', 14), fg='red')
la2.place(relx=0.6, rely=0.25, relwidth=0.3, relheight=0.08)
# 輸入框_3
input_3 = Entry(root, font=('Times New Roman', 12))
input_3.place(relx=0.1, rely=0.35, relwidth=0.3, relheight=0.08)
la3 = Label(root, text="其他合格件數", font=('標楷體', 14))
la3.place(relx=0.1, rely=0.42, relwidth=0.3, relheight=0.08)
# 輸入框_4
input_4 = Entry(root, font=('Times New Roman', 12))
input_4.place(relx=0.6, rely=0.35, relwidth=0.3, relheight=0.08)
la4 = Label(root, text="其他不合格件數", font=('標楷體', 14), fg='red')
la4.place(relx=0.6, rely=0.42, relwidth=0.3, relheight=0.08)
# 呼叫
btn_1 = Button(root, text='進行檢定', font=('標楷體', 12), command=run1)
btn_1.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.08)
# 清除文字方塊按鈕
btnRead = Button(root, text='清除結果', font=('標楷體', 11), command=clearTextInput)
btnRead.place(relx=0, rely=0.57, relwidth=0.15, relheight=0.08)
#btnRead.pack() 用來布局
# 文字方塊在表單垂直自上而下位置60%處起，佈局相對錶單高度40%高的文字方塊
txt = Text(root, font=('標楷體', 14))
txt.place(rely=0.65, relheight=0.4)

root.mainloop()




