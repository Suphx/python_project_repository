#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/8/4 11:24
# FileName: 01.create a object
# Description:
# Question:


class ball:  # 告诉Python，我们在此要创建一个类
    def __init__(self, color, size, direction):
        """在创建完对象之后会自动调用, 它完成对象的初始化的功能"""
        self.color = color
        self.size = size
        self.direction = direction

    def __str__(self):
        """返回一个对象的描述信息"""
        msg = "It's a %s %s ball." % (self.size, self.color)
        return msg

    def bounce(self):  # ?
        if self.direction == "down":
            self.direction = "up"
        else:
            self.direction = "down"


oneBall = ball("green", "small", "up")  # 含参的对象实例化
# 设置对象的属性

print("I just create a redball.")
print("The oneBall is %s." % oneBall.size)
print("The oneBall is %s." % oneBall.color)
print("The ball's direction is %s." % oneBall.direction)
print("Now I'm going to bounce the ball.")
oneBall.bounce()
print("Now the ball's direction is %s." % oneBall.direction)


print(oneBall)

