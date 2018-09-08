#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class StudentTwo'

__author__ = "KinSama"


class StudentTwo(object):
    count = 0  # 定义了一个类属性，这个属性虽然归类所有

    def __init__(self, name):
        self.name = name
        StudentTwo.count += 1
