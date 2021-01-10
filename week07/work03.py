import time
from functools import wraps, lru_cache


'''
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
'''


def timer(func):
    @wraps(func)
    def clock(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(','.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(','.join(pairs))
            # print(pairs)
        arg_str = ','.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_lst, result))
        # print(arg_lst)
        return result
    return clock


@lru_cache
@timer
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


fib(6)
