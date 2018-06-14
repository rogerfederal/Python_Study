#!/usr/bin/env python
#coding:utf-8

"""

NAME:hanshu.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-05
Desc:




"""


#
#
# def fun(name):
#     print("hello "+name)
# fun('yutao')
import random
def level(scores):
    if 90<scores<=100:
        return "A"
    elif 80<scores<=90:
        return "B"
    else:
        return "C"


def main():
    score = []
    for i in range(10):
        score.append(random.randint(0,100))
    for scores in score:
        print(level(scores))

main()








