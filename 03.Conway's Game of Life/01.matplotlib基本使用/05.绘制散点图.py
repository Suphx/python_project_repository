#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/08/01 12:36
# FileName: 05.绘制散点图.py
# Description: 
# Question:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# 防止中文乱码，将字体设置为华文黑体
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 防止负号乱码
mpl.rcParams['axes.unicode_minus'] = False

N = 1000
# 返回一组包含1000个标准正态分布的样本
x = np.random.randn(N)
y = np.random.randn(N)
plt.scatter(x, y)
plt.show()
