#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/6/28 13:34
# FileName: 2.2在画布中画出网格线
# Description:
# Question:

from tkinter import *  # 导入 Tkinter 库

window = Tk()  # 创建Tkinter窗口对象
window.title("2.2在画布中画出网格线")

# 设置窗口大小
WIDTH = 450
HEIGHT = 450
# 横、纵网格个数
X_NUM = 9
Y_NUM = 9

canvas = Canvas(window, bg="white", height=HEIGHT, width=WIDTH)  # 创建画布大小为380x300，背景色为白色的画布
for i in range(1, X_NUM):
    canvas.create_line(0, i * HEIGHT // X_NUM, WIDTH, i * HEIGHT // X_NUM)  # 横线
for i in range(1, Y_NUM):
    canvas.create_line(i * WIDTH // Y_NUM, 0, i * WIDTH // Y_NUM, HEIGHT)  # 竖线
canvas.pack()

window.mainloop()  # 进入窗口循环

