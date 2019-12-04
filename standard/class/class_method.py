#!/usr/bin/env python
# -*- coding: utf-8 -*-

print('--------------方法类型：静态方法，实例方法，类方法------------------------------')


class A(object):
    # self 表示实例，python默认参数，可替换为其他.实例方法把实例传递到方法，如：a.foo(x)其实等于foo(a,x)
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
    # cls 表示类，python默认参数，可替换为其他。类方法把类传递到方法。A.class_foo(x)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
    #不需要对任何绑定
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()
a.foo("foo")
a.class_foo("a class_foo")
A.class_foo("A class_foo")
a.static_foo("a static_foo")
A.static_foo("A static_foo")