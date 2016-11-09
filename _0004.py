 #-*- coding: utf-8 -*- 
import re

__author__ = "zhanhao"

#定义统计单词数的方法
def count(filepath):
    with open(filepath,"rb") as f:
        pattern = re.compile(r"\w+\'\w+|\w+")
        str = f.read().decode("utf-8")
        return len(pattern.findall(str))

#程序入口
if __name__  == "__main__":
    filepath = input("file path:")
    words = count(filepath)
    print(words,end="")