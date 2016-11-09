#-*- coding:utf-8 -*-
import os
import sys
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance, ImageFilter    

__author__ = "zhanhao"

#定义裁剪图片的方法
def cut(pic):
    (w,h) = pic.size
    if(w > h):
        if(w > 640):
            h = h * 640 / w
            w = 640
    if(h > w):
        if(h > 1136):
            w = w * 1136 / h
            h = 1136
    pic = pic.resize((int(w),int(h)),Image.ANTIALIAS)
    return pic
    

#从指定目录获取图片名和路径
def get_img():
    path = input("图片所在目录：")
    files = os.listdir(path)
    return files,path

#逐个处理图片
def process():
    (files,path) = get_img()
    for img in files:
        pic = Image.open(path+"\\"+img)
        pic = cut(pic)
        pic.save(path+"\\"+img)
        print("处理完毕！")


if __name__ == "__main__":
    process()