#! /usr/bin/python3

# -*-coding:utf-8 -*-

#author:zhanhao
#date:2016.11.16
#file:_0009.py

import re
import urllib.request

#从给定网址分析网站内链接，处理成可直接使用的clean links
def get_links(url):
    html = urllib.request.urlopen(url)
    html = html.read().decode('utf-8')
    r = re.compile(r'href="(.+?)"')
    raw_links = r.findall(html)
    links = list()
    for link in raw_links:
        if re.search("(http:.*)|(//.*)",link):
            links.append(link)
        if re.search("/[^/].*",link):
            links.append(url+link)
    return links

if __name__ == "__main__":
    url = "http://www.baidu.com"
    html = urllib.request.urlopen(url)
    links = get_links(url)
    print(links)