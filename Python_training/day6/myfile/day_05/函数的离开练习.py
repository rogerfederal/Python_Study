#!/usr/bin/env python
#coding:utf-8

"""

NAME:函数的离开练习.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-05
Desc:




"""
#number = int(input("输入一个数字:"))


def collatz(number):
    if number%2 == 0:
        return number//2
    else:
        return 3*number+1



def main():
    num = int(input("输入一个数字:"))
    while True:
        if collatz(num) == 1:
            print(1)
            break
        else:
            num = collatz(num)
            print(num)


main()
