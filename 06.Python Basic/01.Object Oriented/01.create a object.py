#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/8/4 11:24
# FileName: 01.create a object
# Description:
# Question:


class ball:  # 告诉Python，我们在此要创建一个类

    def bounce(self):  # ?
        if self.direction == "down":
            self.direction = "up"
        else:
            self.direction = "down"


oneBall = ball()  # 对象实例化
# 设置对象的属性
oneBall.direction = "down"
oneBall.color = "red"
oneBall.size = "small"

print("I just create a redball.")
print("The oneBall is %s." % oneBall.size)
print("The oneBall is %s." % oneBall.color)
print("The ball's direction is %s." % oneBall.direction)
print("Now I'm going to bounce the ball.")
oneBall.bounce()
print("Now the ball's direction is %s." % oneBall.direction)



