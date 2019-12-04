#!/usr/bin/env python
# -*- coding: utf-8 -*-





print('--------------类变量&实例变量------------------------------')
class Test(object):
    num_of_instance = 0
    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1

print(Test.num_of_instance)
t1 = Test('jack')
print(Test.num_of_instance)
t2 = Test('Lucy')
print(Test.num_of_instance)
print(t1.name, t1.num_of_instance)
print(t2.name, t2.num_of_instance)
print(Test.num_of_instance)

'''实例作用域里把变量的引用改变了，变成了一个实例变量'''
class Persion:
    name = "aaa"

p1 = Persion()
p2 = Persion()
# p1.name 开始指向类变量name="aaa",但在实例作用域里把变量的引用改变了，变成了一个实例变量。self.name不再引用Persion类变量name
p1.name = "bbb"
print(p1.name)  # bbb
print(p2.name) # aaa
print(Persion.name) # aaa




