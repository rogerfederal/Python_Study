#!/usr/bin/env python
#coding:utf-8

"""

NAME:生成器.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-05
Desc:




"""


# g = (i**2 for i in range(1,10))
# for j in g:
#     print(j)

#菲波纳妾数列
def fib(num):
    a,b,count = 0,1,1
    while count <= num:
        print(b)
        a,b = b,a+b
        count += 1
fib(100)
