'collections是Python内建的一个集合模块，提供了许多有用的集合类。'

# namedtuple是一个函数，它用来创建一个自定义的tuple对象
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
# 可以验证创建的Point对象是tuple的一种子类
print(isinstance(p, Point))

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
q.popleft()
print(q)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
print(dd['key'])

# 如果要保持Key的顺序，可以用OrderedDict，Key会按照插入的顺序排列，不是Key本身排序
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(list(od.keys()))
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
# class LastUpdatedOrderedDict(OrderedDict):
#     def __init__(self, capacity):
#         super(LastUpdatedOrderedDict, self).__init__()
#         self._capacity = capacity
#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove:', last)
#         if containsKey:
#             del self[key]
#             print('set:', (key, value))
#         else:
#             print('add:', (key, value))
#         OrderedDict.__setitem__(self, key, value)

# Counter是一个简单的计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch]+1
print(c)
