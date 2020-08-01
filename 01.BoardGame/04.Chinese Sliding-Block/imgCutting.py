#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/07/22 12:37
# FileName: imgCutting.py
# Description: 
# Question:

from PIL import Image
import sys


#切图
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0,3):#两重循环，生成9张图片基于原图的位置
        for j in range(0,3):
            #print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]
    return image_list


#保存
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('./crop/pika/'+str(index) + '.png', 'PNG')
        index += 1


if __name__ == '__main__':
    file_path = "src/pikaSrc.jpg"
    image = Image.open(file_path)
    # #image.show()
    # image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list)