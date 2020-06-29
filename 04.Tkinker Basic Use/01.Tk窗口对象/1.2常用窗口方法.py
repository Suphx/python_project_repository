#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/6/28 12:27
# FileName: 1.2常用窗口方法.py
# Description:
# Question:

from tkinter import *  # 导入 Tkinter 库

window = Tk()  # 创建Tkinter窗口对象

window.title("1.2常用窗口方法")  # 设置窗体的标题栏名称
window.geometry('380x300')  # 设置窗体大小（固定语法: widthxheight）
window.resizabl.resizable(width=False, height=True)  # 限制窗口可调整大小范围

window.mainloop()  # 进入窗口循环

