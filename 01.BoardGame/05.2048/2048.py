#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/6/30 9:13
# FileName: 2048
# Description:
# Question:


"""2048游戏
本模块已完整实现2048游戏的算法及分数的计算算法
本游戏的界面采用python 标准库 tkinter 来实现
此界面的布局采用tkinter中的grid布局
"""

import random
import math
import sys

_map_data = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


# -------------------------以下为2048游戏的基本算法---------------------------

# 重置
def reset():
    '''重新设置游戏数据,将地图恢复为初始状态，并加入两个数据 2 作用初始状态'''
    _map_data[:] = []  # _map_data.clear()
    _map_data.append([0, 0, 0, 0])
    _map_data.append([0, 0, 0, 0])
    _map_data.append([0, 0, 0, 0])
    _map_data.append([0, 0, 0, 0])
    # 在空白地图上填充两个2
    fill2()
    fill2()


# 获取 0 个数
def get_space_count():
    """获取没有数字的方格的数量,如果数量为0则说有无法填充新数据，游戏即将结束
    """
    count = 0
    for r in _map_data:
        count += r.count(0)
    return count


# 计算分数
def get_score():
    '''获取游戏的分数,得分规则是每次有两个数加在一起则生成相应的分数。
    如 2 和 2 合并后得4分, 8 和 8 分并后得 16分.
    根据一个大于2的数字就可以知道他共合并了多少次，可以直接算出分数:
    如:
       4 一定由两个2合并，得4分
       8 一定由两个4合并,则计:8 + 4 + 4 得32分
       ... 以此类推
    '''
    score = 0
    for r in _map_data:
        for c in r:
            score += 0 if c < 4 else c * int((math.log(c, 2) - 1.0))
    return score  # 导入数学模块


# 随机数生成
def fill2():
    '''填充2到空位置，如果填度成功返回True,如果已满，则返回False'''
    blank_count = get_space_count()  # 得到地图上空白位置的个数
    if 0 == blank_count:
        return False
    # 生成随机位置, 如，当只有四个空时，则生成0~3的数，代表自左至右，自上而下的空位置
    pos = random.randrange(0, blank_count)
    offset = 0
    for row in _map_data:  # row为行row
        for col in range(4):  # col 为列，column
            if 0 == row[col]:
                if offset == pos:
                    # 把2填充到第row行，第col列的位置，返回True
                    row[col] = 2
                    return True
                offset += 1


# 结束判定
def is_gameover():
    """判断游戏是否结束,如果结束返回True,否是返回False
    """
    for r in _map_data:
        # 如果水平方向还有0,则游戏没有结束
        if r.count(0):
            return False
        # 水平方向如果有两个相邻的元素相同，应当是可以合并的，则游戏没有结束
        for i in range(3):
            if r[i] == r[i + 1]:
                return False
    for c in range(4):
        # 竖直方向如果有两个相邻的元素相同，应当可以合并的，则游戏没有结束
        for r in range(3):
            if _map_data[r][c] == _map_data[r + 1][c]:
                return False
    # 以上都没有，则游戏结束
    return True


# 移动合并分数
def _left_move_number(line):
    '''左移一行数字,如果有数据移动则返回True，否则返回False:
    如: line = [0, 2, 0, 8] 即表达如下一行:
        +---+---+---+---+
        | 0 | 2 | 0 | 8 |      <----向左移动
        +---+---+---+---+
    此行数据需要左移三次:
      第一次左移结果:
        +---+---+---+---+
        | 2 | 0 | 8 | 0 |
        +---+---+---+---+
      第二次左移结果:
        +---+---+---+---+
        | 2 | 8 | 0 | 0 |
        +---+---+---+---+
      第三次左移结果:
        +---+---+---+---+
        | 2 | 8 | 0 | 0 |  # 因为最左则为2,所以8不动
        +---+---+---+---+
     最终结果: line = [4, 8, 0, 0]
    '''
    moveflag = False  # 是否移动的标识,先假设没有移动
    for _ in range(3):  # 重复执行下面算法三次
        for i in range(3):  # i为索引
            if 0 == line[i]:  # 此处有空位，右侧相邻数字向左侧移动，右侧填空白
                moveflag = True
                line[i] = line[i + 1]
                line[i + 1] = 0
    return moveflag


# 移动位置
def _left_marge_number(line):
    '''向左侧进行相同单元格合并,合并结果放在左侧,右侧补零
    如: line = [2, 2, 4, 4] 即表达如下一行:
        +---+---+---+---+
        | 2 | 2 | 4 | 4 |
        +---+---+---+---+
    全并后的结果为:
        +---+---+---+---+
        | 4 | 0 | 8 | 0 |
        +---+---+---+---+
    最终结果: line = [4, 8, 8, 0]
    '''
    for i in range(3):
        if line[i] == line[i + 1]:
            moveflag = True
            line[i] *= 2  # 左侧翻倍
            line[i + 1] = 0  # 右侧归零


# 移动逻辑
def _left_move_aline(line):
    '''左移一行数据,如果有数据移动则返回True，否则返回False:
    如: line = [2, 0, 2, 8] 即表达如下一行:
        +---+---+---+---+
        | 2 |   | 2 | 8 |      <----向左移动
        +---+---+---+---+
    左移算法分为三步:
        1. 将所有数字向左移动来填补左侧空格,即:
            +---+---+---+---+
            | 2 | 2 | 8 |   |
            +---+---+---+---+
        2. 判断是否发生碰幢，如果两个相临且相等的数值则说明有碰撞需要合并,
           合并结果靠左，右则填充空格
            +---+---+---+---+
            | 4 |   | 8 |   |
            +---+---+---+---+
        3. 再重复第一步，将所有数字向左移动来填补左侧空格,即:
            +---+---+---+---+
            | 4 | 8 |   |   |
            +---+---+---+---+
        最终结果: line = [4, 8, 0, 0]
    '''
    moveflag = False
    if _left_move_number(line):
        moveflag = True
    if _left_marge_number(line):
        moveflag = True
    if _left_move_number(line):
        moveflag = True
    return moveflag


def left():
    """游戏左键按下时或向左滑动屏幕时的算法"""
    moveflag = False  # moveflag 是否成功移动数字标志位,如果有移动则为真值,原地图不变则为假值

    # 将第一行都向左移动.如果有移动就返回True
    for line in _map_data:
        if _left_move_aline(line):
            moveflag = True
    return moveflag


def right():
    """游戏右键按下时或向右滑动屏幕时的算法
    选将屏幕进行左右对调，对调后，原来的向右滑动即为现在的向左滑动
    滑动完毕后，再次左右对调回来
    """
    # 左右对调
    for r in _map_data:
        r.reverse()
    moveflag = left()  # 向左滑动
    # 再次左右对调
    for r in _map_data:
        r.reverse()
    return moveflag


def up():
    """游戏上键按下时或向上滑动屏幕时的算法
    先把每一列都自上而下放入一个列表中line中，然后执行向滑动，
    滑动完成后再将新位置摆回到原来的一列中
    """
    moveflag = False
    line = [0, 0, 0, 0]  # 先初始化一行，准备放入数据
    for col in range(4):  # 先取出每一列
        # 把一列中的每一行数入放入到line中
        for row in range(4):
            line[row] = _map_data[row][col]
        # 将当前列进行上移，即line 左移
        if (_left_move_aline(line)):
            moveflag = True
        # 把左移后的 line中的数据填充回原来的一列
        for row in range(4):
            _map_data[row][col] = line[row]
    return moveflag


def down():
    """游戏下键按下时或向下滑动屏幕时的算法
    选将屏幕进行上下对调，对调后，原来的向下滑动即为现在的向上滑动
    滑动完毕后，再次上下对调回来
    """
    _map_data.reverse()
    moveflag = up()  # 上滑
    _map_data.reverse()
    return moveflag


# -------------------------以下为2048游戏的操作界面---------------------------

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
        if is_gameover():
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
            for c in range(len(_map_data[0])):
                number = _map_data[r][c]  # 设置数字
                label = map_labels[r][c]  # 选中Lable控件
                label['text'] = str(number) if number else ''
                label['bg'] = mapcolor[number][0]
                label['foreground'] = mapcolor[number][1]
        label_score['text'] = str(get_score())  # 重设置分数

    # 创建一个frame窗口，此创建将容纳全部的widget 部件
    frame = Frame(root, bg=game_bg_color)
    frame.grid(sticky=N + E + W + S)
    # 设置焦点能接收按键事件
    frame.focus_set()
    frame.bind("<Key>", on_key_down)

    # 初始化图形界面
    map_labels = []
    for r in range(4):
        row = []
        for c in range(len(_map_data[0])):
            value = _map_data[r][c]
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