#!/usr/bin/env python
# -*- coding: utf-8 -*-
print('-----------------*args-----------------------')
'''
*args 不确定函数里将要传递多少参数时使用
 将参数打包成tuple元组(params1,params2,params3...)
'''
def print_everything(*args):
    for count, thing in enumerate(args):
        print('{0}. {1}'.format(count,thing))
    print(type(args))
    print(args)

print_everything('apple','banana','cabbage')

print('-----------------**kwargs-----------------------')
'''
*kwargs 允许使用没有事先定义的参数名
将参数打包成dict字典{params1,params2,params3}
'''
def table_things(**kwargs):
    for name, value in kwargs.items():
        print('{0} = {1}'.format(name,value))
    print(type(kwargs))
    print(kwargs)
table_things(apple = 'fruit', cabbage = 'vegetable')

print('-----------------args,默认参数,*args,**kwargs顺序问题-----------------------')
# 参数arg、*args、**kwargs三个参数的位置必须是一定的。必须是(arg,*args,**kwargs)这个顺序，否则程序会报错

def foo(x, y = 1, *args):
    print(x)
    print(y)
    print(args)
foo(1,2,3,4,5) # y=1值被2重置
print('======')
def foo(x,*args,y=1):
    print(x)
    print(args)
    print(y)
foo(1,2,3,4,5) # y按照默认参数
print('======')
def foo(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)
foo(1,2,3,4,y=1,a=2,b=3,c=4)
print('======')
# 默认参数 必须在 **kwargs前面，否则会报错
def foo(x,y=1,**kwargs):
    print(x)
    print(y)
    print(kwargs)
foo(1,a=2,b=3,c=4)
