#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/8/4 9:15
# FileName: 08.NumPy的基本使用
# Description:
# Question:

import numpy as np

array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
array2 = np.transpose(array1)
list2 = list(array2)
print(array1)
print(array2)
print(list2)