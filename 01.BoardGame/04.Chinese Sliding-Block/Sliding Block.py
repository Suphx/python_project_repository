#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/7/12 11:03
# FileName: Sliding Block
# Description:
# Question:

import random
# 初始化棋盘
global board
board = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

# 打乱棋盘
random.shuffle(board)
for i in range(len(board)):
    random.shuffle(board[i])


# 定义一个输出显示的函数
def display():
    show = [["" for _ in range(3)] for _ in range(3)]
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                show[row][col] == " "
            else:
                show[row][col] = str(board[row][col])

    print('+---+---+---+')
    for row in show:
        print("|{0:^3}|{1:^3}|{2:^3}|".format(row[0], row[1], row[2]))
        print('+---+---+---+')


# 移动控制算法
def move(n):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == n:
                indexI = i
                indexJ = j
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                zeroI = i
                zeroJ = j
    if ((indexI == zeroI and abs(indexJ - zeroJ) == 1) or
            (indexJ == zeroJ and abs(indexI - zeroI) == 1)):
        board[zeroI][zeroJ] = n
        board[indexI][indexJ] = 0


while board != [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
    display()
    n = int(input("Which number do you want to move?"))
    move(n)