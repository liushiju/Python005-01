# 学习笔记

## 第一节：异常捕获与处理

课程源码： `git checkout 2d`

[pretty_errors 官方文档链接](https://pypi.org/project/pretty-errors/)

[try 语句官方文档](https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-try-statement)

[with 语句官方文档](https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-with-statement)

[with 语句上下文管理器官方文档](https://docs.python.org/zh-cn/3.7/reference/datamodel.html#with-statement-context-managers)

### 异常捕获

参考 https://docs.python.org/zh-cn/3.6/library/exceptions.html
所有内置的非系统退出的异常都派生自 Exception 类

StopIteration 异常示例：

``` python
gennumber = ( i for i in range(0,2))
print(next(gennumber))
print(next(gennumber))

try:
    print(next(gennumber))
except StopIteration:
    print('最后一个元素')
```

[exception_demo.py](课程代码/exception_demo.py)

``` python
def a():
    return b()

def b():
    return c()

def c():
    return d()

def d():
    x = 0
    return 100/x

a()
```

### 异常处理机制的原理

异常也是一个类

异常捕获过程：

* 异常类把错误消息打包到一个对象
* 然后该对象会自动查找到调用栈
* 直到运行系统找到明确声明如何处理这些类异常的位置

所有异常继承自 BaseException

Traceback 显示了出错的位置，显示的顺序和异常信息对象

### 异常信息与异常捕获

异常信息在 Traceback 信息的最后一行，有不同的类型

捕获异常可以使用 try…except 语法

try…except 支持多重异常处理

常见的异常类型主要有：

* 1. LookupError 下的 IndexError 和 KeyError
* 2. IOError
* 3. NameError
* 4. TypeError
* 5. AttributeError
* 6. ZeroDivisionError

[exception_demo/p1_dive0.py](课程代码/exception_demo/p1_dive0.py)

``` python
1/0
# 发生异常后面的程序不再执行
print('never see me')
```

[exception_demo/p2_try.py](课程代码/exception_demo/p2_try.py)


[exception_demo/p3_chain.py](课程代码/exception_demo/p3_chain.py)

自己定义抛出异常
[exception_demo/p4_inputerror.py](课程代码/exception_demo/p4_inputerror.py)

对异常结果优化，可以使用第三方库 pretty库
[exception_demo/p5_pretty.py](课程代码/exception_demo/p5_pretty.py)

[exception_demo/p6_with.py](课程代码/exception_demo/p6_with.py)

[exception_demo/p7_custom_with.py](课程代码/exception_demo/p7_custom_with.py)