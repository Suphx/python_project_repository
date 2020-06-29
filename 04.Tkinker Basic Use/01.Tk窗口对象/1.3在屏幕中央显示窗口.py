#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/6/28 13:01
# FileName: 1.3在屏幕中央显示窗口.py
# Description:
# Question:

from tkinter import *  # 导入 Tkinter 库

window = Tk()  # 创建Tkinter窗口对象
window.title("1.3在屏幕中央显示窗口")  # 设置窗体的标题栏名称

# 设置窗口大小
WIDTH = 380
HEIGHT = 300
# 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

alignstr = '%dx%d+%d+%d' % (WIDTH, HEIGHT, (screenwidth - WIDTH) / 2, (screenheight - HEIGHT) / 2)
window.geometry(alignstr)  # 设置窗体大小

window.resizable(width=False, height=True)  # 限制窗口可调整大小范围

window.mainloop()  # 进入窗口循环



