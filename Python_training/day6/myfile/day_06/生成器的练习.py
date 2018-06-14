#!/usr/bin/env python
#coding:utf-8

"""

NAME:生成器的练习.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-06
Desc:




"""

def printer(text):
    while True:
        coun = 1
        s = yield
        print("[%.3d]%s"%(coun,s))
        coun += 1





def main():
    p = printer('hh')
    next(p)
    p.send('aaaaaa')
main()










