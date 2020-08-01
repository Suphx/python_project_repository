#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/7/12 19:39
# FileName: Tkinter Sliding Block
# Description:
# Question:

from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk

global board
board = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]


# 初始化棋盘
def initBoard():
    # 打乱棋盘
    random.shuffle(board)
    for i in range(len(board)):
        random.shuffle(board[i])


# 移动控制算法
def move(event):
    x = event.x // 100
    y = event.y // 100
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == board[x][y]:
                indexI = i
                indexJ = j
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                zeroI = i
                zeroJ = j
    if ((indexI == zeroI and abs(indexJ - zeroJ) == 1) or
            (indexJ == zeroJ and abs(indexI - zeroI) == 1)):
        board[zeroI][zeroJ] = board[x][y]
        board[indexI][indexJ] = 0
    # 移动后刷新棋盘
    display()


# 定义一个显示函数
def display():
    canvas.delete(ALL)
    canvas.create_line(0, 100, 300, 100, fill='white')
    canvas.create_line(0, 200, 300, 200, fill='white')
    canvas.create_line(100, 0, 100, 300, fill='white')
    canvas.create_line(200, 0, 200, 300, fill='white')

    show  = [["./crop/pika/"+str(i) + ".png" for i in range(1,4)] , \
            ["./crop/pika/" + str(i) + ".png" for i in range(4, 7)] , \
            ["./crop/pika/" + str(i) + ".png" for i in range(7, 10)]]

    for i in range(3):
        for j in range(3):
            photo = Image.open(show[i][j])
            photo = ImageTk.PhotoImage(photo)
            canvas.create_image(i * 100 + 50, j * 100 + 50, anchor=NW, image=photo)

            # canvas.create_text(i * 100 + 50, j * 100 + 50, text=show[i][j])


window = Tk()  # 创建tkinter窗口
window.title("华容道")  # 设置标题文字
window.resizable(0, 0)  # 固定宽和高

game_bg_color = "#bbada0"  # 设置背景颜色
canvas = Canvas(window, bg=game_bg_color, width=1000, height=1000)  # 利用窗口对象创建画布
canvas.pack()
# 创建3x3网格
canvas.create_line(0, 100, 300, 100, fill='white', dash=(4, 4))
canvas.create_line(0, 200, 300, 200, fill='white', dash=(4, 4))
canvas.create_line(100, 0, 100, 300, fill='white', dash=(4, 4))
canvas.create_line(200, 0, 200, 300, fill='white', dash=(4, 4))
# 初始化棋盘
initBoard()
display()

canvas.bind_all("<Button-1>", move)
window.mainloop()


