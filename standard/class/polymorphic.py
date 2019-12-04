#!/usr/bin/env python
# -*- coding: utf-8 -*-

print('-----------------多态，鸭子类型---------------------------')


class F1:
    pass


class S1(F1):
    def show(self):
        print('S1.show')


class S2(F1):
    def show(self):
        print('S2.show')


# 传入任意类型，只要有方法，就是多态
def func(obj):
    print(obj.show())


s1_obj = S1()
func(s1_obj)
s2_obj = S2()
func(s2_obj)
