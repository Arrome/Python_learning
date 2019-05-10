#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
    # self 特殊参数，必填
    # 构造函数，类实例化自动执行
    def __init__(self, name, score, id):
        self.name = name
        self.score = score
        self.__id = id

    def print_score(self):
        print('%s, %s' % (self.name, self.score))

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.id = id

bart = Student('Bart', 95.0, 1)
list = Student('List', 87.1, 2)

'''python默认将bart传给self参数，即bart.print_score(bart)'''
bart.print_score()
list.print_score()

bart.sex = '女'
print(bart.sex)

print('--------------方法类型：静态方法，实例方法，类方法------------------------------')

class A(object):
    # self 表示实例，python默认参数，可替换为其他.实例方法把实例传递到方法，如：a.foo(x)其实等于foo(a,x)
    def foo(self, x):
        print("executing foo(%s,%s)"%(self,x))
    # cls 表示类，python默认参数，可替换为其他。类方法把类传递到方法。A.class_foo(x)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)"%(cls,x))
    #不需要对任何绑定
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)
a = A()
a.foo("foo")
a.class_foo("a class_foo")
A.class_foo("A class_foo")
a.static_foo("a static_foo")
A.static_foo("A static_foo")

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

print('-----------------多继承---------------------------')
'''
经典类，多继承情况下，会按照深度优先方式查找
'''
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

'''
新式类，多继承情况下，会按照广度优先方式查找
'''
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
def Func(obj):
    print(obj.show())

s1_obj = S1()
Func(s1_obj)
s2_obj = S2()
Func(s2_obj)
