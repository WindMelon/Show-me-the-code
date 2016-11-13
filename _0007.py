#!/usr/bin/python3

# -*- coding:utf-8 -*-

import os
import re

__auter__ = "zhanhao"

#定义对每个脚本代码行数进行统计，返回 总行数 代码行数 注释行数 空行数
def stat(file):
    with open(file,"rb") as f:
        lines = 0
        code = 0
        annot = 0
        space = 0
        for line in f.readlines():
            lines += 1 
            if(re.search("^\s*?#",line.decode("utf-8"))):
                annot += 1 
            if (re.search("^\s+?$",line.decode("utf-8"))):
                space +=1
            else:
                code +=1
    return lines,code,annot,space   
            

#遍历目录里文件，分别对每一个文件进行统计
def get_files(path):
    files = os.listdir(path)
    tlines = 0
    tcode = 0
    tannot = 0
    tspace = 0
    print("文件名\t总行数\t代码行数\t注释行数\t空行数")
    for file in files:
        lines,code,annot,space = stat(path+"\\"+file)
        tlines += lines
        tcode += code
        tannot += annot
        tspace += space
        print(file+"\t"+str(lines)+"\t"+str(code)+"\t"+str(annot)+"\t"+str(space))
    print("总计"+"\t"+str(tlines)+"\t"+str(tcode)+"\t"+str(tannot)+"\t"+str(tspace))
        
#代码入口
if __name__ == "__main__":
    path = input("请输入代码所在目录:")
    get_files(path)