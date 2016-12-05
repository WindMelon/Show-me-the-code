#! /usr/bin/python3
# -*- coding:utf-8 -*-
#author:zhanhao
#Date:2016.11.22
#file:_0014.py
#description:集合14、15功能

import xlwt
import json
import os,sys

def write_xls(json_data):
    keys = sorted(json_data.keys())
    wb = xlwt.Workbook()
    sheet = wb.add_sheet("test_sheet")
    i = 0
    for key in keys:
        j = 0
        sheet.write(i,j,key)
        j += 1
        if isinstance(json_data[key],str): #判断数据类型，是字符串直接写，不是就循环写入
            sheet.write(i,j,json_data[key])
        else: 
            for value in json_data[key]:
                sheet.write(i,j,value)
                j += 1
        i += 1
    wb.save("test.xls")

def get_json(file):
    with open(file,"rb") as f:
        json_data = json.loads(f.read().decode('utf-8')) #loads处理字符串，load处理文件
        write_xls(json_data)

if __name__ == "__main__":
    get_json("输入json文件：")