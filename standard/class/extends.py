#!/usr/bin/env python
# -*- coding: utf-8 -*-

print('-----------------多继承---------------------------')


# 经典类，多继承情况下，会按照深度优先方式查找

class D:
    def bar(self):
        print('D.bar')


class C(D):
    def bar(self):
        print('C.bar')


class B(D):
    def bar(self):
        print('B.bar')


class A(B, C):
    def bar(self):
        print('A.bar')


a = A()
a.bar()


# 新式类，多继承情况下，会按照广度优先方式查找

class D(object):
    def bar(self):
        print('D.bar')


class C(D):
    def bar(self):
        print('C.bar')


class B(D):
    def bar(self):
        print('B.bar')


class A(B, C):
    pass


a = A()
a.bar()
