#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/6/28 21:01
# FileName: Tic-Tac-Toe
# Description:
# Question:

# 导入依赖库
from tkinter import *
from tkinter.messagebox import *

# 初始化全局变量
# board是井字棋核心之一，底层维护的是一个二维数组，初始化棋盘中所有位置的数字
# window初始化的是我们用tkinter创建的一个窗口
# canvas初始化的是我们tkinter的Canvas模块创建的一个画布
global window, canvas, board
board = [[0, 0, 0] for i in range(3)]
steps = 0  # 记录步数，用于判别下棋方


window = Tk()  # 创建一个TK窗口对象
window.title("Tic-Tac-Toe")
canvas = Canvas(window, width=300, height=300)  # 利用窗口对象创建画布


# 自定义handler函数，绑定鼠标左键下棋逻辑
def nextStep(event):
    global steps
    players = [-1, 1]
    show = ["X", "O"]
    # 读取鼠标点击画布的坐标位置并存入变量
    i = event.x // 100
    j = event.y // 100

    if board[i][j] == 0:
        board[i][j] = players[steps % 2]
        canvas.create_text(i * 100 + 50, j * 100 + 50, text=show[steps % 2])

        winner = None
        for i in range(3):
            if (sum(board[i]) in [-3, 3]) or (board[0][i] + board[1][i] + board[2][i] in [-3, 3]):
                winner = show[steps % 2]
        if (board[0][0] + board[1][1] + board[2][2] in [-3, 3]) or (board[0][2] + board[1][1] + board[2][0] in [-3, 3]):
            winner = show[steps % 2]
        if winner is not None:
            showinfo("GameOver", "The winner is " + winner)
            window.destroy()
        steps = steps + 1

    if steps == 9 and winner is None:
        showinfo("GameOver", "Draw!")
        window.destroy()


canvas.pack()
canvas.bind("<Button-1>", nextStep)

canvas.create_line(0, 100, 300, 100)
canvas.create_line(0, 200, 300, 200)
canvas.create_line(100, 0, 100, 300)
canvas.create_line(200, 0, 200, 300)

window.mainloop()
