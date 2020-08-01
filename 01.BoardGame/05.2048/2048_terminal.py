#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/07/22 12:11
# FileName: 2048_terminal.py
# Description: 
# Question:

#
# 2048
# 1. 初始化一个4*4的棋盘
# 声明board、show为全局变量
global board, show
board = [[0, 0, 0, 0] for i in range(4)]
show = [[0, 0, 0, 0] for i in range(4)]


# 2. 输出2048界面的函数
def display():
    # 我新增的
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                show[i][j] = " "
            else:
                show[i][j] = board[i][j]
    print("+----+----+----+----+")
    for row in range(len(board)):
        # 格式化输出（%d -> 十进制数）
        print("| %2s | %2s | %2s | %2s |" % (show[row][0], show[row][1], show[row][2], show[row][3]))
        print("+----+----+----+----+")


# 3.生成2
# 随机生成两个下标，范围是0-3
import random


def fill2():
    i = random.randint(0, 3)
    j = random.randint(0, 3)
    # 2应当生成在空白的位置（0）
    while board[i][j] != 0:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
    board[i][j] = 2


# 4.开局，随机生成两个2，显示棋盘
fill2()
fill2()
display()


# 5.合并函数（上下左右移动）
def mergeRow(col):
    # col -> list
    # 合并前，先删除这一个一维列表中的所有的0
    # 删完以后，其他数字之间不会有0间隔
    while 0 in col:
        col.remove(0)
    # 对于剩下的数字，从左向右遍历col
    # 判断相邻的2个数字是否相同
    # 相同就合并
    # 合并后删除第i+1位
    i = 0
    while i < len(col) - 1:
        if col[i] == col[i + 1]:
            col[i] *= 2
            col.pop(i + 1)
        i += 1
    # [4,2] + [0] * (4-len(col))
    col = col + [0] * (4 - len(col))
    return col


# 6.进入游戏循环
while True:
    move = input("请输入你想移动的方向（adws）：")
    if move == "a":
        for i in range(4):
            board[i] = mergeRow(board[i])
        fill2()
        display()

    # 向右合并
    elif move == "d":
        for i in range(4):
            row = board[i][::-1]
            row = mergeRow(row)
            board[i] = row[::-1]
        fill2()
        display()

    # 向上合并
    elif move == "w":
        for j in range(4):
            col = [board[0][j], board[1][j], board[2][j], board[3][j]]
            col = mergeRow(col)
            board[0][j], board[1][j], board[2][j], board[3][j] = col[0], col[1], col[2], col[3]
        fill2()
        display()

    elif move == "s":
        for j in range(4):
            col = [board[3][j], board[2][j], board[1][j], board[0][j]]
            col = mergeRow(col)
            board[3][j], board[2][j], board[1][j], board[0][j] = col[0], col[1], col[2], col[3]
        fill2()
        display()
