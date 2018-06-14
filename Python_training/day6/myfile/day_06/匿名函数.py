#!/usr/bin/env python
#coding:utf-8

"""

NAME:匿名函数.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-06
Desc:




"""
from functools import reduce


# n = int(input("长度："))
# li = [int(input()) for i in range(n)]
# print(sorted(li, key=lambda x: 1 if 0 else 1))




# #lambda 匿名函数求和
# print(reduce(lambda x,y:x+y ,range(6)))
#
#
# print(list(lambda y:y**2,range(6)))


def comper1(base):
    def comper2(y):
        return base>y
    return comper2
comper3 = comper1(10)
print(comper3(3))