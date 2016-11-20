#! /usr/bin/python
# -*-coding:utf-8-*-
#author:zhanhao
#Date:2016.11.18
#file:_0010.py

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

fontpath="C:\\WINDOWS\\Fonts\\"

def get_randchar():
    randchar = random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return randchar

def get_randcolor():
    return (random.randint(30,100),random.randint(30,100),random.randint(30,100))

def get_code():
    width = 240
    height = 60
    image = Image.new('RGB',(width,height),(180,180,180))
    font = ImageFont.truetype(fontpath + 'SIMYOU.TTF', 40)
    draw = ImageDraw.Draw(image)
    for i in range(4):
        draw.text((60 * i + 10,10),get_randchar(),font=font,fill=get_randcolor())
    for i in range(random.randint(1500,3000)):
        draw.point((random.randint(0,width),random.randint(0,height)),fill=get_randcolor())
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')

if __name__ == '__main__':
    get_code()