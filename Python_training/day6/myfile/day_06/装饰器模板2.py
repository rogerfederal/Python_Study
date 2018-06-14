#!/usr/bin/env python
#coding:utf-8

"""

NAME:装饰器模板2.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-06
Desc:




"""
from functools import wraps
def is_admin(fun):
    @wraps(fun)
    def wrpper(*args , **kwargs):
        g = fun(*args,**kwargs)
        return g
    return wrpper


def admin(name='root'):
    print("你没有权限")
print(admin(name='root'))









