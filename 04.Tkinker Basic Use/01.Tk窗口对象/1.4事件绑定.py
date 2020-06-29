#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/6/28 19:53
# FileName: 1.4事件绑定
# Description:
# Question:

from tkinter import *  # 导入 Tkinter 库
from tkinter.messagebox import *
window = Tk()  # 创建Tkinter窗口对象


# 自定义函数
def sayHello(event):
    showinfo("消息框", "Hello, Python!")
    # Tk坐标系统
    print("鼠标位置：(", event.x, ",", event.y, ")")


# 绑定鼠标左键点击事件
window.bind_all("<Button-1>", sayHello)

window.mainloop()  # 进入窗口循环
