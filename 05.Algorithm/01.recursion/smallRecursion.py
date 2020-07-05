#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/7/4 11:57
# FileName: smallRecursion
# Description:
# Question:


def countdown(i):
    print(i)
    if i < 1:
        return None
    else:
        countdown(i-1)


countdown(5)