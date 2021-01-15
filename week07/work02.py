#!/usr/bin/env python
'''
自定义一个 python 函数，实现 map() 函数的功能。
'''


def my_map(func, *iterable):
    iters = [iter(it) for it in iterable]
    while True:
        try:
            yield func(*[next(it) for it in iters])
        except StopIteration:
            return


# 验证 x+y+z 结果
test_my_map_01 = my_map(lambda x, y, z: x+y+z, [1, 2], [1, 2], [1, 2])
print(list(test_my_map_01))
test_map_01 = map(lambda x, y, z: x+y+z, [1, 2], [1, 2], [1, 2])
print(list(test_map_01))

# 验证 (x+y)*z 的结果


def calc(x, y, z):
    return (x+y)*z


test_my_map_02 = my_map(calc, [1, 2], [1, 2], [1, 2])
print(list(test_my_map_02))
test_map_02 = map(calc, [1, 2], [1, 2], [1, 2])
print(list(test_map_02))

# 验证把 python 每个元素变成 str
test_my_map_03 = my_map(str, 'python')
print(list(test_my_map_03))

test_map_03 = map(str, 'python')
print(list(test_map_03))
