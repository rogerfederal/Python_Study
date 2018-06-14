#!/usr/bin/env python
#coding:utf-8

"""

NAME:sorted高阶函数.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-06
Desc:




"""

#
# s = [
#     ['001','apple','100','1000'],
#     ['002','banana','200','12000'],
#     ['003','computer','300','3000'],
#     ['004','baozi','400','4000']
# ]
# def sorted_count(item):
#     return item[2]
#
#
# sorted(s,key=sorted_count,reverse=True)
# print(sorted_count([0],[1]),sorted_count([0],[3]))
#
#
#
#

info = {
    '001':{
        'name':'apple',
        'count':1000,
        'price':2
    },

    '002': {
        'name': 'xiaomi',
        'count': 10,
        'price': 2000
    },
    '003': {
        'name': 'Oppo',
        'count': 200,
        'price': 1900
    }
}
def dict_sorted_count(item):
    return item['count']

print(sorted(info.values(), key=dict_sorted_count))


