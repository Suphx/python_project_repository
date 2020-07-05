#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/6/23 21:21
# FileName: simpleMinesweeper.py
# Description: 基于tkinter绘制9*9的棋盘模拟扫雷
# Question:

# 导入依赖库包
import random
from tkinter import *
from tkinter.messagebox import *

# 初始化全局变量
# board是扫雷核心之一，底层维护的是一个二维数组，初始化棋盘中所有位置的数字
# show是扫雷核心之一，底层维护的是一个二维数组，用于触发click以后刷新棋盘显示以及胜负判定
# window初始化的是我们用tkinter创建的一个窗口
# canvas初始化的是我们tkinter的Canvas模块创建的一个画布
global window, canvas, board, show
board = [[0 for j in range(9)] for i in range(9)]
show = [["-" for j in range(9)] for i in range(9)]
window = Tk()
canvas = Canvas(window, width=450, height=450)
canvas.pack()

window.title("扫雷")
window.resizable(0, 0)  # 特别注意，由于我们利用click的坐标修改数组，窗口的大小会影响数值的处理，这里我们限制窗口的缩放


# 初始化一个棋盘，底层维护一个二维数组board，随机生成雷的位置
def initBoard():
    # 初始化10颗雷，数字“9”代表雷
    for i in range(15):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        while board[x][y] != 0:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
        board[x][y] = 9
    # 计算其他格子的数字
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                number = 0
                # 利用循环，在当前格子的周围八个格子里“探雷”
                for s in [-1, 0, 1]:
                    for t in [-1, 0, 1]:
                        # 0 <= i + s <= 8 and 0 <= j + t <= 8 两个条件是为了避免二维数组越界
                        if 0 <= i + s <= 8 and 0 <= j + t <= 8 and board[i + s][j + t] == 9:
                            number = number + 1
                board[i][j] = number


# 棋盘内容的显示
def showBoard():
    canvas.delete(ALL)  # 每次显示前，我们会删除画布上的所有内容，根据底层的数组内容重新生成一遍
    for i in range(1, 9):
        canvas.create_line(0, i * 50, 900, i * 50)  # 初始化横线
        canvas.create_line(i * 50, 0, i * 50, 900)  # 初始化竖线
    for i in range(9):
        for j in range(9):
            x = j * 50 + 25
            y = i * 50 + 25
            canvas.create_text(x, y, text=show[i][j])  # 显示当前棋盘


# 判断胜利
def judge():
    # 判断获胜条件：检查show数组中"-"、“F”、“?”三者的个数，即可判赢（是否存在bug？）
    if sum([row.count("-") for row in show]) == 0 \
            and sum([row.count("F") for row in show]) == 9 \
            and sum([row.count("?") for row in show]) == 0:
        showinfo("WIN", "You Win!")
        # 判断结束，通知结束，窗口摧毁
        window.destroy()


# 递归实现“扩散翻格”
def bloom(x, y):
    if board[x][y] == 0:
        show[x][y] = " "
        for s in [-1, 0, 1]:
            for t in [-1, 0, 1]:
                if 0 <= x+s <= 8 and 0 <= y+t <= 8 and show[x+s][y+t] == "-":
                    bloom(x+s, y+t)
    else:
        show[x][y] = str(board[x][y])


# 初始化click事件处理逻辑
def click(event):
    # 在鼠标点击后，我们会先使用局部变量x,y记录鼠标点击窗口的位置，然后进行判赢逻辑检查
    # click中的event属性包含点击窗口的坐标位置，我们会利用这个值，做数组修改或数据判断
    x = event.y // 50
    y = event.x // 50

    judge()
    if board[x][y] == 9:
        showinfo("LOSE", "BOMB! You Lose!")
        # 判断结束，通知结束，窗口摧毁
        window.destroy()
    # 如果无输赢情况，则要修改棋盘当前显示的局面，核心是更新底层的show数组
    else:
        # 这里我们分两种情况，由bloom函数处理
        # 1. 点击处为0（即周围8个格子不存在雷），则用递归消除周围8个未显示的格子
        # 2. 点击处周围为数字，我们需显示该数字
        bloom(x, y)
    showBoard()


# 模拟插旗、插？的动作
def mark(event):
    relu = [" "] + [str(i) for i in range(1, 8)]
    x = event.y // 50
    y = event.x // 50
    if show[x][y] == "-":
        show[x][y] = "F"
    elif show[x][y] == "F":
        show[x][y] = "?"
    elif show[x][y] == "?":
        show[x][y] = "-"
    elif show[x][y] in relu:
        show[x][y] = show[x][y]
    showBoard()


# 将鼠标左右键click动作绑定函数
canvas.bind_all("<Button-1>", click)
canvas.bind_all("<Button-3>", mark)

initBoard()  # 雷区初始化
showBoard()  # 初始化游戏界面
print(board)
window.mainloop()  # 进入消息循环

