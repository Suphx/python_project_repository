#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/8/4 15:08
# FileName: 03.HotDog
# Description:
# Question:


class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "生的"
        self.condiments = []

    def __str__(self):
        msg = "热狗"
        if len(self.condiments) == 0:
            return self.cooked_string + "原味" + msg
        if len(self.condiments) > 0:
            msg += "浇上了"
        for i in self.condiments:
            msg += i + "，"
        msg = msg.strip("，")
        msg = self.cooked_string + msg
        return msg

    def cook(self, time):
        self.cooked_level += time
        if self.cooked_level > 8:
            self.cooked_string = "焦的"
        elif self.cooked_level > 5:
            self.cooked_string = "熟的"
        elif self.cooked_level > 3:
            self.cooked_string = "半生不熟的"
        else:
            self.cooked_string = "生的"

    def addcondiment(self, condiment):
        self.condiments.append(condiment)


myHotDog = HotDog()
print(myHotDog)
myHotDog.cook(4)
print(myHotDog)
myHotDog.cook(2)
print(myHotDog)
myHotDog.addcondiment("番茄酱")
myHotDog.addcondiment("芥末酱")
print(myHotDog)