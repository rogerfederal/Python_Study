#!/usr/bin/env python
#coding:utf-8

"""

NAME:yield生成器.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-06
Desc:




"""
#生成器目前是用来节省空间
g = (i for i in range(100) if i%2 ==0)
# print(g.__next__())     #print(next(g))    #两个一样，逐步进行
# for j in g:
#     print(j)




#yield是一个生成器；开辟一片空间，不至于死机
# def fib(num):
#     a,b,count = 0,1,1
#     while count <= num:
#         yield b
#         a,b = b,a+b
#         count += 1
# g = fib(10)
#
# for i in g:
#     print(i)
#



# while True:
#     print(g.__next__())     #当我们使用生成器遍历时，会以报错的方式结束。


import time
import random


def consumer(name):
    print("%s准备买包子"%(name))
    while True:
        kind = yield
        print("%s已经购买了%s口味的包子"%(name,kind))


def producer(name):
    s1 = consumer('natasha')
    s2 = consumer('meili')
    s1.__next__()
    s2.__next__()

    print("%s准备制作包子"%(name))
    for kind in ['辣','不辣']:
        time.sleep(random.random())
        print("%s制作了%s口味的包子"%(name,kind))
        s1.send(kind)
        s2.send(kind)
producer("yutao")





