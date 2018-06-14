#!/usr/bin/env python
#coding:utf-8

"""

NAME:函数求平均值，最大、最小值.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-05
Desc:
"""

def hello(a):
    max_num = max(a)
    min_num = min(a)
    va_nnum = sum(a)/len(a)
    return max_num,min_num,va_nnum
b = hello([2,3,4,5])
print(b)





