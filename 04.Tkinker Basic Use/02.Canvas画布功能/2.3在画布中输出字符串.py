#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/6/28 19:45
# FileName: 2.3在画布中输出字符串
# Description:
# Question:


from tkinter import *

window = Tk()  # 创建Tkinter窗口对象
window.title("2.3在画布中输出字符串")
window.bind_all()

canvas = Canvas(window, width=640, height=480)
canvas.create_text(320, 240, text="Hello, Python!")

canvas.pack()


window.mainloop()
