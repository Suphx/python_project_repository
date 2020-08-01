#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/08/01 09:51
# FileName: 03.练习—学生成绩可视化
# Description: 
# Question:

from matplotlib import pyplot as plt

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
x = ["0-60", "60-70", "70-80", "80-90", "90-100"]
y = []


def gradeCout(low, high):
    counts = 0
    for g in grades:
        if low <= g < high:
            counts += 1
    return counts


y.append(gradeCout(0, 60))
y.append(gradeCout(60, 70))
y.append(gradeCout(70, 80))
y.append(gradeCout(80, 90))
y.append(gradeCout(90, 100))

plt.bar(x, y)
plt.show()
