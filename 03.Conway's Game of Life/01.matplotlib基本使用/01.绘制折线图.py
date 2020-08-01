#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/07/28 15:03
# FileName: 01.绘制折线图
# Description: 
# Question:

from matplotlib import pyplot as plt
import matplotlib as mpl

# 防止中文乱码，将字体设置为华文黑体
mpl.rcParams['font.sans-serif']=['SimHei']  # 指定默认字体 SimHei为黑体

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [304.94, 561.75, 926.03, 2862.5, 3078.93, 12113.46,  60878.84]
# plot()中需传入x轴数据和y轴数据
# marker表示折线上数据点处的类型
# linestyle表示折线的类型
plt.title("1950-2010年中国GDP变化量")
plt.xlabel("年份")
plt.ylabel("单位：亿美元")
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.show()

