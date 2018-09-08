#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class Screen'

__author__ = "KinSama"


class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def resolution(self):
        return self.__width*self.__height
