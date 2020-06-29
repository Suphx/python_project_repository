#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/6/29 12:14
# FileName: 2.4画布坐标系统
# Description:
# Question:

from tkinter import *  # 导入 Tkinter 库
from tkinter.messagebox import *
window = Tk()  # 创建Tkinter窗口对象
canvas = Canvas(window, width=300, height=300)
canvas.pack()


# 自定义函数
def sayHello(event):
    # Canvas坐标系统
    axisinfo = "鼠标位置：(%d,%d)" % (event.x, event.y)
    showinfo("鼠标位置", axisinfo)


# 绑定鼠标左键点击事件
canvas.bind_all("<Button-1>", sayHello)

window.mainloop()  # 进入窗口循环