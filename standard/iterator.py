#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 迭代器

# python中，只要可迭代对象，都可迭代
print('-----------判断对象是否可迭代-----------------')
from collections import Iterable
print(isinstance('123',Iterable)) # 字符串
print(isinstance([1,2,3],Iterable)) # 数组
print(isinstance((1,2,3),Iterable)) # 元组
print(isinstance({1,2,3},Iterable)) # 集合
print(isinstance({'a':1,'b':2,'c':3},Iterable)) # 元组
print(isinstance(123,Iterable)) # 数字

print('-----------for循环-----------------')
'''python中没有索引变量,底层不使用索引，使用迭代器'''
for item in '123':
    print(item)
for item in [1,2,3]:
    print(item)
for item in (1,2,3):
    print(item)
for item in {1,2,3}:
    print(item)
for item in {'a':1,'b':2,'c':3}:
    print(item)
# 变量字典
for key, value in {'a':1,'b':2,'c':3}.items():
    print(key, value)

print('-----------迭代器-----------------')
'''迭代器是有状态的，一次性使用，从中消耗一项，就消失了'''
iterator = iter({1,2,3})
print(next(iterator)) #1

print('-----------while循环和迭代器重定义for循环-----------------')
def funky_for_loop(iterable):
    iterator = iter(iterable)
    done_looping = False
    while not done_looping:
        try:
            item = next(iterator)
        except StopIteration:
            done_looping = True
        else:
            print(item)
funky_for_loop([1,2,3])

print('-----------生成器-----------------')
'''边循环边计算的机制，生成器是迭代器，可迭代'''
numbers = [1,2,3]
squares = (n**2 for n in numbers)
print(squares)

print(squares is iter(squares)) #True iter()参数为迭代器返回自己

print('-----------迭代器对象-----------------')
numbers = [1,2,3]
letters = ['a','b','c']
def func(x):
    return x**2
def is_odd(n):
    return n%2 == 1

print(enumerate(numbers))
# enumerate()获取索引
for i, value in enumerate(numbers):
    print(i, value)

print(reversed(numbers))
# zip()多个同时遍历
print(zip(numbers))
for num,lett in zip(numbers,letters):
    print(num, lett)

print(map(func,numbers))

print(filter(is_odd,numbers))
