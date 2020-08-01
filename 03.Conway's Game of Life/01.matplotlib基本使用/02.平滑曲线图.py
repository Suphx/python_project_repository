#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/08/01 10:04
# FileName: 02.平滑曲线图
# Description: 
# Question:

from matplotlib import pyplot as plt
x = [i/10 for i in range(100)]
y1 = [i for i in x]
y2 = [i**3 for i in x]
y3 = [2**i for i in x]
plt.plot(x, y1, label="y=x")
plt.plot(x, y2, label="y=x^3")
plt.plot(x, y3, label="y=2^x")
plt.legend(loc=9)
plt.show()
