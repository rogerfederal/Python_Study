#!/usr/bin/env python
#coding:utf-8

"""

NAME:列表生成式的练习.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-05
Desc:




"""
#print([i+j for i in 'abc' for j in '123'])

# import os
# print([i for i in os.listdir('/var/log') if i.endswith('.log')])    #找出/var/log/文件下以.log结尾的文件



#k,v 互换
# d = dict(a=1,b=2)
# print({v:k for k,v in d.items()})






d = dict(a = 1,b = 5 , A = 5, c = 8, C= 10)
d2 = {}
for k,v in d.items():
    low_k = k.lower()
    if low_k not in d2:
        d2[low_k]=v
    else:
        d2[low_k] += v
print(d2)

