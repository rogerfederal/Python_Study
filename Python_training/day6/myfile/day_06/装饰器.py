#!/usr/bin/env python
#coding:utf-8

"""

NAME:装饰器.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-06
Desc:




"""


def add_info(fun):  # fun = saveMoney
    def wrapper():
        print("五四青年......")
        print("welcome to ICBC........")
        fun()    # saveMoney()
    return wrapper


@add_info    # saveMoney= addinfo(saveMoney)
def saveMoney():
    print("存钱.......")
#saveMoney()



import time
from functools import wraps
def timeit(fun):
    @wraps(fun)
    def wrapper(*args,**kwargs):
        star_time = time.time()
        g =fun(*args,**kwargs)
        end_tame = time.time()
        print("%s的运行时间为%s"%(fun.__name__,end_tame-star_time))
        return g
    return wrapper

@timeit
def aaa():
    """
    this is 测试函数
    无实际意义
    :return: hello
    """
    time.sleep(0.5)
    print("hello")
aaa()
print(aaa.__name__)
print(aaa.__doc__)


@timeit
def add(x,y):
    """

    :param x:
    :param y:
    :return:x+y
    """
    return x+y
print(add(1,3))
print(add.__name__)
print(add.__doc__)