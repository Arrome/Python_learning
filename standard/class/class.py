#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Student(object):
    # self 特殊参数，必填
    # 构造函数，类实例化自动执行
    def __init__(self, name, score, uid):
        self.name = name
        self.score = score
        self.__id = uid

    # TODO
    def __call__(self, *args, **kwargs):
        pass

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
