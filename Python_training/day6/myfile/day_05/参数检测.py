#!/usr/bin/env python
#coding:utf-8

"""

NAME:参数检测.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-05
Desc:




"""
#判度是否可迭代
#1：
from collections import Iterable
print(isinstance(1,int))
print(isinstance(1,Iterable))    #判断‘1’是否为可迭代的
print(isinstance({1,2,3},Iterable))    #判断‘1’是否为可迭代的

#2:可以用for循环判断

