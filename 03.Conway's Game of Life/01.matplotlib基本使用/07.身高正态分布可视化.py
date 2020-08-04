#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/08/01 12:47
# FileName: 07.身高正态分布可视化
# Description: 
# Question:
from numpy import array
from numpy.random import normal
import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
# 防止中文乱码，将字体设置为华文黑体
mpl.rcParams['font.sans-serif'] = ['SimHei']


def genData():
    heights = []
    weights = []
    N = 1000000

    for i in range(N):
        # 身高服从均值172，标准差为6的正态分布
        height = normal(172, 6)
        # 体重由身高作为自变量的线性回归模型产生，误差服从标准正态分布
        weight = (height - 80) * 0.7 + normal(0, 1)
        heights.append(height)
        weights.append(weight)
    return array(heights), array(weights),


heights, weights = genData()


# 绘制直方图
def drawHist(values, xlabel, ylabel, title):
    # 创建直方图
    # 第一个参数为待绘制的定量数据，不同于定性数据，这里并没有事先进行频数统计
    # 第二个参数为划分的区间个数
    _, bins, _ = plt.hist(values, 400, density=True, alpha=0.75)
    print(bins)
    y = ((1 / (np.power(2 * np.pi, 0.5) * 6)) * np.exp(-0.5 * np.power((bins - 172) / 6, 2)))
    print(y)
    plt.plot(bins, y, ls="--")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


heightsXlabel = '身高'
heightsYlabel = '概率'
heightsTitle = '成年男性身高分布图（均值为172，标准差为6）'
drawHist(heights, heightsXlabel, heightsYlabel, heightsTitle)


# 绘制散点图
def drawScatter(heights, weights, xlabel, ylabel, title):
    # 创建散点图
    # 第一个参数为点的横坐标
    # 第二个参数为点的纵坐标
    plt.scatter(heights, weights)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


heightsXlabel = '身高'
heightsYlabel = '体重'
heightsTitle = '成年男性“身高-体重”线性模型'
drawScatter(heights, weights, heightsXlabel, heightsYlabel, heightsTitle)