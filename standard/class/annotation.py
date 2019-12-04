#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Annotation(object):

    def __init__(self, def_property):
        self.def_property = def_property

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method(self):
        pass

