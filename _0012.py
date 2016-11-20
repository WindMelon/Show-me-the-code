#! /usr/bin/python
# -*- coding:utf-8 -*-
#author:zhanhao
#date:2016.11.20
#file:_0011.py

import sys,os
import re
    
def filter(sentence):
    filter = list()
    filtered = str(sentence)
    with open("filtered_words.txt","r") as f:
        filter = str(f.read()).split(sep='\n')
    for i in filter:
        if(re.search(i,sentence)):
           filtered = filtered.split(sep=i)
           sep = ""
           for t in range(len(i)):
               sep += "*"
           filtered = sep.join(filtered)
    return filtered

if __name__ == "__main__":
    sentence = input("输入一句话：")
    print(filter(sentence))