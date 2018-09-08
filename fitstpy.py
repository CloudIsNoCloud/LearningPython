import math

# name = input()#这是拿来输入的，把输入的字符串转成int：name=int(name)
print('hello,来py')
# print(600+400+500)
# print('hello,chou'+name)

# 就很普通的if
num_one = 11
if num_one > 0:
    print('zheng')
else:
    print('fu')
# 用r''来取消字符串里所有转义字符的作用
print(r'\\t\\n搞铲铲')

# 据说下面这样可以多行输入''' string  '''
print('''line1
line2
line3''')

# r'''''' 和 r''效果一样= =就是这玩意儿换行
print(r'''Hello,\n
Lisa!''')

# 编码什么的只用UTF-8就行了

# 然后为什么这三个'还是多行注释啊
# 可变数组有append(在屁股加),insert(在指定位置加),pop(删屁股或者指定位置)
# 这是一个不可改变的list：tuple，只有一个数字的时候，要加','就像(1,)
tupleList = (1, 2, 3, 4, 5, 6, [7, 8])
print(tupleList)

# 循环走一波while还是那个while
sum = 0
for x in range(101):
    sum = sum+x
print(sum)

# dict就是和其他语言里的map类似得用大括号
# 用x in dict可以判断x是否在dict内，用get() key不存在时候回None或者自己给的一个值
# 当然pop(key)还是删除，我pop子招谁惹谁了
dictTest = {"name": 0, "sex": 1}

# set:这个是个key的组合，反正我在java里面从来没用过
# 设置值用set()，要传入一个[]，当[]里面有重复的值时会被过滤，然后显示是{}
# 用add(key)可以往里面加，但是重复的话就没效果，remove(key)就是移除
# 这回没有pop了
setTest = set([11, 11, 22, 22, 33, 33])

# python的函数可以用一个变量来指向
absa = abs  # 不用括号
print(absa(-10))


# 用def可以定义一个函数
# isinstance(x, (int, float)) 类型检查
# 有默认参数这么一说，可变参数加个*(本质为tuple)，关键字参数加个**(本质为dict)
def doSome(x, y):
    '''
    据说这是模块、函数和类的解释
    '''
    if not (isinstance(x, float) and isinstance(y, float)):
        # 抛出一个Error
        raise TypeError('bad operand type')
    else:
        print("可以的")
    # 据说可以返回一个tuple，然后可以用多个变量解构
    return x + y


print(doSome(10.0, 20.0))


def quadratic(a, b, c):
    '''
    求一元二次方程平方根
    '''
    if not (isinstance(a, (int, float)) and
            isinstance(b, (int, float)) and
            isinstance(c, (int, float))):
        raise TypeError('bad operand type')
    x1 = (-b+math.sqrt(math.pow(b, 2)-(4*a*c)))/(2*a)
    x2 = (-b-math.sqrt(math.pow(b, 2)-(4*a*c)))/(2*a)
    return x1, x2


print(quadratic(2, 3, 1))

# 切片，一个很牛逼的东西
qieList = list(range(100))
print(qieList[-10:])  # 倒十个到最后一个
print(qieList[::3])  # 每隔三个取一个
print(qieList[:20:2])  # 取前二十个再每隔两个取一个


def trim(s):
    '''
    自己瞎写的trim
    '''
    leng = len(s)
    i = 0
    j = leng-1
    if leng > 0:
        while i < leng:
            if s[i] != " ":
                break
            else:
                i += 1
        while j > i:
            if s[j] != " ":
                break
            else:
                j -= 1
        return s[i:j+1]
    else:
        return ""


# 测试trim:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('trim测试成功!')

# 通过collections模块的Iterable类型判断对象是否可迭代
# from collections import Iterable  # 不知道为什么
# print(isinstance([1, 2, 3, 4], Iterable))


def findMinAndMax(L):
    '''
    写的一个没什么用的找最大最小
    '''
    if L != []:
        min = L[0]
        max = L[0]
        for x in L:
            if min > x:
                min = x
            if max < x:
                max = x
        return (min, max)
    else:
        return (None, None)

 # 测试findMinAndMax
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('findMinAndMax测试成功!')

# 列表生成式
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)

# 生成器，创建一个generator，根据算法推算
g = (x * x for x in range(10))
print(g)


def fib(max):
    '''
    用yield关键字可以把这个函数变成一个公式给generator用
    '''
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
print(f)


def triangles():
    '''
    这个是一个杨辉三角的
    '''
    L = [1]
    while True:
        yield L  # 告诉生成器这是一个要生成的点
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))]  # 重新生成一次L


n = 0
for x in triangles():
    print(x)
    n = n + 1
    if n == 10:
        print("测试成功杨辉三角")
        break

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数

# map()传入的第一个参数是f，即函数对象本身。
# 由于结果r是一个Iterator，Iterator是惰性序列
# 因此通过list()函数让它把整个序列都计算出来并返回一个list。
# 这个可以传各种函数进去算，函数针对的是每一个元素
print(list(map(str, (list(map(abs, [1, -1, 1, -5, -20]))))))

# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字


def normalize(name):
    return name[0].upper()+name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce


def reduceFn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(reduceFn, map(char2num, "13579")))

# 接受一个list并利用reduce()求积


def prod(L):
    return reduce(lambda x, y: x*y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456


def str2float(s):
    def fn(x, y):
        return x * 10 + y
    n = s.index(".")
    s1 = list(map(int, s[:n]))
    s2 = list(map(int, s[n+1:]))
    # 先把小数点前后的数字全部变成整数的，然后小数点后的数进行处理
    return reduce(fn, s1)+reduce(fn, s2)/(10**len(s2))


print('\'123.4567\'=', str2float('123.4567'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功str2float')
else:
    print('测试失败!')

# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# 一个过滤用的东西


def is_palindrome(n):
    return str(n) == str(n)[::-1]


# 测试is_palindrome:
print('1~300:', list(filter(is_palindrome, range(1, 300))))

# sorted()可以接收一个key函数来实现自定义的排序 sorted([36, 5, -12, 9, -21], key=abs)
# 第一个参数是要排序的，第二个是指向一个函数，第三个是反向
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


def by_score(t):
    return t[1]


# key指向的函数是针对L中的每一个元素的
print(sorted(L, key=by_name))
print(sorted(L, key=by_score, reverse=True))

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量


def createCounter():
    L = [0]  # 列表L的内存地址在初次调用时已经给定

    def counter():
        L[0] += 1  # 改变列表L中第一个元素的值，但并没有改变列表L的内存地址
        return L[0]
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())

# 匿名函数 lambda 只能是一个表达式


def is_odd(n):
    return n % 2 == 1


print(list(filter(lambda n: n % 2 == 1, range(1, 20))))

# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）


def log(text):
    def decorator(fun):
        # 只需记住在定义wrapper()的前面加上@functools.wraps(func)即可
        def wrapper(*arg, **kw):
            print("%s %s():" % (text, fun.__name__))
            return fun(*arg, **kw)
        return wrapper
    return decorator


@log("dididi")
def textDecorator():
    print("2018/8/2")


textDecorator()

import functools
import time


# 可作用于任何函数上，并打印该函数的执行时间
def metric(fn):
    '''
    一个没有其他文字参数的装饰器
    '''
    @functools.wraps(fn)
    def wrapper(*arg, **kw):
        t1 = time.time()
        result = fn(*arg, **kw)  # 必须是要有这个= =
        print('%s executed in %.9f ms' % (fn.__name__, (time.time()-t1)))
        return result
    return wrapper


# 测试decorator
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


fast(11, 22)
slow(11, 22, 33)


# 写一个@log和@log("")都能用的装饰器
def log_double(arg):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print('\r\n%s %s():' % (arg, fn.__name__))
            print('begin call')  # 习题2
            res = fn(*args, **kwargs)
            print('end call')  # 习题2
            return res  # 习题2
        return wrapper
    # print("check where decorator works")
    if isinstance(arg, str):  # 判断是否传入了参数
        return decorator
    elif hasattr(arg, '__call__'):  # 判断arg是否包含了"__call__"属性
        return log_double('')(arg)  # [ 此处是重点！ ]
    else:
        pass


@log_double
def f_1():
    print("f_1")


@log_double('execute')
def f_2():
    print("f_2")


f_1()
f_2()


# functools.partial的作用就是
# 把一个函数的某些参数给固定住（也就是设置默认值）
# 返回一个新的函数，调用这个新函数会更简单
int2 = functools.partial(int, base=2)
print(int2("10101010"))
