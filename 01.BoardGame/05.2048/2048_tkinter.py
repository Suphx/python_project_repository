#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/07/22 12:18
# FileName: 2048_tkinter.py
# Description: 
# Question:

import random
import copy

# 棋盘初始化
board = [[0, 0, 0, 0] for i in range(4)]
# 分数初始化
score = 0

# 重置
def reset():
    # 分数清0
    global score
    score = 0
    '''重新设置游戏数据,将地图恢复为初始状态，并加入两个数据 2 作用初始状态'''
    board[:] = []  # _map_data.clear()
    board.append([0, 0, 0, 0])
    board.append([0, 0, 0, 0])
    board.append([0, 0, 0, 0])
    board.append([0, 0, 0, 0])
    # 在空白地图上填充两个2
    fill2()
    fill2()


# 随机生成2
def fill2():
    i = random.randint(0, 3)
    j = random.randint(0, 3)
    # 当且仅当这个位置数字为0才能在该位置生成2
    while board[i][j] != 0:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
    board[i][j] = 2


# 合并算法
def mergeRow(col):
    global score
    # col -> list
    # 合并前，先删除这一行中所有的0
    # 删完以后，其他数字之间不会有0间隔
    while 0 in col:
        col.remove(0)
    # 对于剩下的数字，从左向右遍历col
    # 在遍历中判断相邻两位是否相等
    # 若第i位与第i+1位相等
    # 即可对col[i]自更新原来的两倍
    # 删除第i+1位
    i = 0
    while i < len(col)-1:
        if col[i] == col[i+1]:
            col[i] *= 2
            score += col[i]
            col.pop(i+1)
        i += 1
    # 用0补足4位
    col = col + [0] * (4 - len(col))
    return col


# 判断输
def isGameOver():
    # list.count(value) 统计value出现的次数
    # 仍有空格
    defeat = sum([row.count(0) for row in board])
    if defeat:
        return False
    # 横向仍可合并
    for row in board:
        for i in range(3):
            if row[i] == row[i+1]:
                return False
    # 纵向仍可合并
    for c in range(4):
        for r in range(3):
            if board[r][c] == board[r+1][c]:
                return False
    # 以上条件都不满足，则游戏结束
    return True

# 移动算法
def left():
    """游戏左键按下时或向左滑动屏幕时的算法"""
    temp = copy.deepcopy(board)  # 深拷贝，与board本身独立
    for i in range(len(board)):
        board[i] = mergeRow(board[i])
    if temp != board:
        return True
    return False


def right():
    temp = copy.deepcopy(board)
    for i in range(len(board)):
        row = board[i][::-1]
        row = mergeRow(row)
        board[i] = row[::-1]
    if temp != board:
        return True
    return False


def up():
    temp = copy.deepcopy(board)
    for i in range(len(board)):
        col = [board[0][i], board[1][i], board[2][i], board[3][i]]
        col = mergeRow(col)
        board[0][i], board[1][i], board[2][i], board[3][i] = \
            col[0], col[1], col[2], col[3]
    if temp != board:
        return True
    return False


def down():
    temp = copy.deepcopy(board)
    for i in range(len(board)):
        col = [board[0][i], board[1][i], board[2][i], board[3][i]][::-1]
        col = mergeRow(col)[::-1]
        board[0][i], board[1][i], board[2][i], board[3][i] = \
            col[0], col[1], col[2], col[3]
    if temp != board:
        return True
    return False



from tkinter import *
from tkinter import messagebox

def main():
    reset()  # 先重新设置游戏数据

    root = Tk()  # 创建tkinter窗口
    root.title('2048游戏')  # 设置标题文字
    root.resizable(width=False, height=False)  # 固定宽和高

    # 以下是键盘映射
    keymap = {
        'a': left,
        'd': right,
        'w': up,
        's': down,
        'Left': left,
        'Right': right,
        'Up': up,
        'Down': down,
        'q': root.quit,
    }

    game_bg_color = "#bbada0"  # 设置背景颜色

    # 设置游戏中每个数据对应色块的颜色
    mapcolor = {
        0: ("#cdc1b4", "#776e65"),
        2: ("#eee4da", "#776e65"),
        4: ("#ede0c8", "#f9f6f2"),
        8: ("#f2b179", "#f9f6f2"),
        16: ("#f59563", "#f9f6f2"),
        32: ("#f67c5f", "#f9f6f2"),
        64: ("#f65e3b", "#f9f6f2"),
        128: ("#edcf72", "#f9f6f2"),
        256: ("#edcc61", "#f9f6f2"),
        512: ("#e4c02a", "#f9f6f2"),
        1024: ("#e2ba13", "#f9f6f2"),
        2048: ("#ecc400", "#f9f6f2"),
        4096: ("#ae84a8", "#f9f6f2"),
        8192: ("#b06ca8", "#f9f6f2"),
        # ----其它颜色都与8192相同---------
        2 ** 14: ("#b06ca8", "#f9f6f2"),
        2 ** 15: ("#b06ca8", "#f9f6f2"),
        2 ** 16: ("#b06ca8", "#f9f6f2"),
        2 ** 17: ("#b06ca8", "#f9f6f2"),
        2 ** 18: ("#b06ca8", "#f9f6f2"),
        2 ** 19: ("#b06ca8", "#f9f6f2"),
        2 ** 20: ("#b06ca8", "#f9f6f2"),
    }

    def on_key_down(event):
        '键盘按下处理函数'
        keysym = event.keysym
        if keysym in keymap:
            if keymap[keysym]():  # 如果有数字移动
                fill2()  # 填充一个新的2
        update_ui()
        if isGameOver():
            mb = messagebox.askyesno(
                title="gameover", message="游戏结束!\n是否退出游戏!")
            if mb:
                root.quit()
            else:
                reset()
                update_ui()

    def update_ui():
        '''刷新界面函数
        根据计算出的f地图数据,更新各个Label的设置
        '''
        for r in range(4):
            for c in range(len(board[0])):
                number = board[r][c]  # 设置数字
                label = map_labels[r][c]  # 选中Lable控件
                label['text'] = str(number) if number else ''
                label['bg'] = mapcolor[number][0]
                label['foreground'] = mapcolor[number][1]
        label_score['text'] = str(score)  # 重设置分数

    # 创建一个frame窗口，此创建将容纳全部的widget部件
    frame = Frame(root, bg=game_bg_color)
    frame.grid(sticky=N + E + W + S)
    # 设置焦点能接收按键事件
    frame.focus_set()
    frame.bind("<Key>", on_key_down)

    # 初始化图形界面
    map_labels = []
    for r in range(4):
        row = []
        for c in range(len(board[0])):
            value = board[r][c]
            text = str(value) if value else ''
            label = Label(frame, text=text, width=4, height=2,
                          font=("黑体", 30, "bold"))
            label.grid(row=r, column=c, padx=5, pady=5, sticky=N + E + W + S)
            row.append(label)
        map_labels.append(row)

    # 设置显示分数的Lable
    label = Label(frame, text='分数', font=("黑体", 30, "bold"),
                  bg="#bbada0", fg="#eee4da")
    label.grid(row=4, column=0, padx=5, pady=5)
    label_score = Label(frame, text='0', font=("黑体", 30, "bold"),
                        bg="#bbada0", fg="#ffffff")
    label_score.grid(row=4, columnspan=2, column=1, padx=5, pady=5)

    # 以下设置重新开始按钮
    def reset_game():
        reset()
        update_ui()

    restart_button = Button(frame, text='重新开始', font=("黑体", 12, "bold"),
                            bg="#8f7a66", fg="#f9f6f2", command=reset_game)
    restart_button.grid(row=4, column=3, padx=5, pady=5)

    update_ui()  # 更新界面

    root.mainloop()  # 进入tkinter主事件循环


main()  # 启动游戏