#!/usr/bin/env python
#coding:utf-8

"""

NAME:robot.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-06
Desc:




"""
def robot():
    say = ''
    while True:
        s = yield say
        if 'age' in s:
            say = '爸爸25了'
        elif 'name'in s:
            say = '求我阿，求我我就告诉你'
        elif 'birthday' in s:
            say = '明天就是爸爸的生日啦'
        elif 'hello'in s:
            say = 'hello too'
        else:
            say = '我什么都不知道！'



def main():
    g = robot()
    next(g)
    while True:
        user_send = input('我：')
        robot_send = g.send(user_send)
        print('robot:%s'%(robot_send))

main()


