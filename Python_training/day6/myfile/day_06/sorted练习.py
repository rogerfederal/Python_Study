#!/usr/bin/env python
#coding:utf-8

"""

NAME:sorted练习.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-06
Desc:




"""
s = []
def count(item):
    if item == 0:
        return 1
    else:
        return 0


def main():
    g = input("请输入：")
    s.append(g)
    for i in s:
        s.int(i)
    print(sorted(s,key=count))




main()




