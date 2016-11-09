#! /usr/bin/python3

# -*- coding:utf-8 -*-

import re
import os

__author__ = "__zhanhao__"

#统计单词，计算频率最高单词
def stat(file):
    pattern = re.compile(r"\w+")
    with open(file,"rb") as f:
        content = f.read().decode("utf-8")
        words = pattern.findall(content)
        dic = dict()
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        d = sorted(dic.items(),key=lambda t:t[1],reverse=True)
        return d[0][0],dic[d[0][0]]
        
#从指定目录获取文件
def get_files(path):
    files = os.listdir(path)
    for file in files:
        word,count = stat(path+"\\"+file)
        print("most important word in "+file+" is "+word+",appears "+str(count)+" times")

if __name__ == "__main__":
    path = input("输入文件目录:")
    get_files(path)