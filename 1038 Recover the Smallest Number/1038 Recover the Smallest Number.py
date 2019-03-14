"""
start time: 2019-02-22 14-56-10 周五
坑：最后一个会超时，用C++吧
cmp_to_key，类似c++的自定义cmp函数，区别在于return的是x-y,而不是x<y
"""
from functools import cmp_to_key

_, *number = input().split()
number.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)))
print(int("".join(number)))
