#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'test'

__author__ = "KinSama"

from Student import *

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

# 获取对象的类型，使用type()函数
# 如果要判断一个对象是否是函数，可以使用types模块中定义的常量
# 要判断class的类型，可以使用isinstance()函数
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态

from StudentTwo import *

if StudentTwo.count != 0:
    print('测试失败!')
else:
    bart = StudentTwo('Bart')
    if StudentTwo.count != 1:
        print('测试失败!')
    else:
        lisa = StudentTwo('Bart')
        if StudentTwo.count != 2:
            print('测试失败!')
        else:
            print('Students:', StudentTwo.count)
            print('测试通过!')

# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性

# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
from Screen import *

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)

# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。


# Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类

# 定义__str__()方法，返回一个好看的字符串

# 如果一个类想被用于for ... in循环，类似list或tuple那样就必须实现一个__iter__()方法
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值
# 直到遇到StopIteration错误时退出循环

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法

# __getattr__()方法，动态返回一个属性

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。

# 枚举
# from enum import Enum

# Month = Enum("Month", ('Jan', 'Feb', 'Mar', 'Apr', 'May',
#                        'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items(): # 莫名其妙的报错了
#     print(name, '=>', member, ',', member.value)

bart = Student('Bart', Gender.Male)
if bart.get_gender() == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
