#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/7/4 16:14
# FileName: factorialDemo
# Description:
# Question:


# 计算出num的阶乘    num！= num * (num-1) * (num-2) * ... * 3 * 2 * 1
def getFactorial1(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res


def getFactorial2(num):
    if num == 1:
        return 1
    else:
        return num*getFactorial2(num-1)


# 5! = 5*4*3*2*1 = 120
print(getFactorial2(3))