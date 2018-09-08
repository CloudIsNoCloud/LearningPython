#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class Student'

__author__ = "KinSama"

from enum import unique, Enum


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):

    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender
