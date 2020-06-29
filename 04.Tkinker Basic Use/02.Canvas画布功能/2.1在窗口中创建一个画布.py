#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/6/28 13:13
# FileName: 2.1在窗口中创建一个画布.py
# Description:
# Question:

from tkinter import *  # 导入 Tkinter 库

window = Tk()  # 创建Tkinter窗口对象

canvas = Canvas(window, bg="white", height=300, width=380)  # 创建画布大小为380x300，背景色为白色的画布
canvas.pack(side='top')

window.mainloop()  # 进入窗口循环

