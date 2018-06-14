#!/usr/bin/env python
#coding:utf-8

"""

NAME:图书管理系统.py
Author:YuTao
Connetc:616637861@qq.com
Date:2018-05-19
Desc:




"""

class Book(object):
    def __init__(self, name, author, state, bookIndex):
        self.name = name
        self.author = author
        # 0 借出；1 未借出
        self.state = state
        self.bookIndex = bookIndex

    def __str__(self):
        return '书名<%s> 状态<%s>'%(self.name,self.state)

class Bookmanage(object):
    book = []
    def init(self):
        self.book.append(Book('python','Guido',1,'一楼东侧'))
        self.book.append(Book('java','Guido',1,'二楼南侧'))
        self.book.append(Book('c#','Guido',1,'三楼东西侧'))
        self.book.append(Book('PHP','Guido',1,'四楼北侧'))


    def Menu(self):
        self.init()
        while True:
            print("""
                       图书管理系统
                    1.查询
                    2.增加
                    3.借阅
                    4.归还
                    5.退出
            
            """ )
            choice = input("你要办理的业务：")
            if choice == '1':
                self.referbook()
            elif choice == '2':
                self.addbook()
            elif choice == '3':
                self.borrowbook()
            elif choice == '4':
                pass
            elif choice == '5':
                print('********欢迎您下次使用********')
                exit(0)
            else:
                print("请输入正确选项！")

    def addbook(self):
        name = input("书名：")
        self.book.append(Book(name,input('作者：'),1,input('书籍位置：')))
        print('添加《%s》成功' %(name))

    def borrowbook(self):
        name = input('借阅书籍名称：')
        ret = self.chockbook(name)
        if ret != None:
            if ret.state == 0 :
                print('书籍《%s》已经借出'%(name))
            else:
                ret.state = 0
                print('书籍《%s》借阅成功'%(name))
        else:
            print('书籍《%s》不存在'%(name))


    def chockbook(self,name):
        for book in self.book:
            if book.name == name:
                return book

        else:
            return None

    def referbook(self):
        name = input('要查询的书籍名称：')
        ret = self.chockbook(name)
        if ret != None:
            if ret.state == 0 :
                print('书籍《%s》已经借出'%(name))
            else:
                print('书籍《%s》未借出'%(name))

        else:
            print('书籍《%s》不存在' % (name))


    def backbook(self):
        name = input('要归还的书籍名称：')
        ret = self.chockbook(name)
        if ret != None:
            ret.state = 1
            print('书籍《%s》归还成功')

        else:
            self.addbook()

manage = Bookmanage()
manage.Menu()












