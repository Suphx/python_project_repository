#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/07/28 16:36
# FileName: 02.绘制条形图
# Description: 
# Question:


from matplotlib import pyplot as plt
import matplotlib as mpl

# 防止中文乱码，将字体设置为华文黑体
mpl.rcParams['font.sans-serif']=['SimHei']  # 指定默认字体 SimHei为黑体

plt.title("经典电影获奥斯卡奖统计")
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
plt.xlabel("经典电影")
plt.ylabel("获奖数（个）")
num_oscars = [5, 11, 3, 8, 10]
plt.bar(movies, num_oscars)
plt.show()
