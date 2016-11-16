#! /usr/bin/python3
# -*- coding:utf-8 -*-
#author : zhanhao
#file : _0008.py
#Date : 2016.11.15


import urllib.request
import re

#解析网页，获取主体内容
def get_content(url):
    html = urllib.request.urlopen(url).read()
    r = re.compile('<p>(?:<.[^>]*>)*(.*?)(?:<.[^>]*>)*?</p>')
    result = r.findall(html.decode('GBK'))
    return result

if __name__ == '__main__':
    url = input("要解析的网页:")
    content = get_content(url)
    print(content)
