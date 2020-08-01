#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/08/01 11:14
# FileName: 05.数据可视化—学生成绩
# Description: 
# Question:

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
# 防止中文乱码，将字体设置为华文黑体
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体 SimHei为黑体

# 用subplot()方法绘制多幅图形
plt.figure(figsize=(6, 6), dpi=80)
# 创建第一个画板
plt.figure(1)
# 将第一个画板划分为2行1列组成的区块，并获取到第一块区域
ax1 = plt.subplot(211)

# 在第一个子区域中绘图
plt.scatter([1, 3, 5], [2, 4, 5], marker="v", s=50, color="r")
# 选中第二个子区域，并绘图
ax2 = plt.subplot(212)
plt.plot([2, 4, 6], [7, 9, 15])

# 为第一个画板的第一个区域添加标题
ax1.set_title("第一个画板中第一个区域")
ax2.set_title("第一个画板中第二个区域")

# 调整每隔子图之间的距离
plt.tight_layout()
plt.show()
