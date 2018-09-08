#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'this is a module template'

__author__ = "KinSama"

import sys


def test():
    arg = sys.argv
    if len(arg) == 1:
        print("Hello World")
    elif len(arg) == 2:
        print("Hello %s" % (arg[1]))
    else:
        print("too many arguments")


if __name__ == "__main__":
    test()
