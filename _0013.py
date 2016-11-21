#! /usr/bin/python3
# -*- coding:utf-8 -*-
#author:zhanhao
#Date:2016.11.21
#file:_0013.py

from urllib import request
import re

def down_pic(url):
    i = 0
    url = str(url)
    html = request.urlopen(url)
    html = html.read().decode('utf-8')
    links = re.findall('<img.*?class="BDE_Image".*?src="(.*?)".*?>',html)
    downloaded = list()
    for img in links:
        if img in downloaded:
            continue
        downloaded.append(img)
        print("正在下载"+img+"\n")
        request.urlretrieve(img,filename="imgs\\img"+str(i)+".jpg")
        i += 1


if __name__ == '__main__':
    url = input("输入要爬取图片的网址：")
    down_pic(url)