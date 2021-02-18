# 学习笔记

## 第一节：Scrapy并发参数优化原理

### 学习参考文档

[Twisted 学习参考文档](https://pypi.org/project/Twisted/)
[asyncio — 异步 I/O 学习文档](https://docs.python.org/zh-cn/3.7/library/asyncio.html)

requests: 同步请求数据

### Scarapy 参数优化

settings.py 参数调优

``` python
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# 下载延时，3秒
DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
# 域名 和 ip 进行设置
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
```

### 基于 twisted 的异步 IO 框架

多任务模型分为同步模型和异步模型
Scrapy 使用的是 Twisted 模型

Twisted 是异步编程模型，任务之间互相独立，用于大量 I/O 密集操作

<img src="images/基于twisted异步IO框架.png" alt="基于twisted异步IO框架">

[twisted_demo](twisted_demo.py)

``` python
from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor

def response(*args, **kwargs):
    # print(args, kwargs)
    print('返回网页的内容')

def callback(*args):
    print('执行了一个回调',args)

@defer.inlineCallbacks
def start(url):
    d = getPage(url.encode('utf-8'))
    d.addCallback(response)
    d.addCallback(callback)
    yield d

def stop(*args, **kwargs):
    reactor.stop()

urls = ['http://www.baidu.com','http://www.sougou.com']
li = []

for url in urls:
    ret = start(url)
    li.append(ret)
print(li)

d = defer.DeferredList(li)
d.addBoth(stop)
reactor.run()
```

## 第二节：多进程：进程的创建

### 多进程模型

多进程、多线程、协程的目的都是希望尽可能多处理任务

产生新的进程可以使用以下方式：

``` python
os.fork()
multiprocessing.Process()
```

多进程的第一个问题：进程的父子关系

[p1_firstproc.py](1进程/p1_firstproc.py)

``` python
# only for linux mac

# fork()
import os

os.fork()
print('1111111111')
# 执行结果：
# 1111111111
# 1111111111
# # fork函数一旦运行就会生出一条新的进程，2个进程一起执行导致输出了2行
```

[p2_fork.py](1进程/p2_fork.py)

``` python
# 区分父子进程
import os
import time

res = os.fork()
print(f'res == {res}')

if res == 0:
    print(f'我是子进程,我的pid是:{os.getpid()}我的父进程id是:{os.getppid()}')
else:
    print(f'我是父进程,我的pid是: {os.getpid()}')

# fork()运行时，会有2个返回值，返回值为大于0时，此进程为父进程，且返回的数字为子进程的PID；当返回值为0时，此进程为子进程。
# 注意：父进程结束时，子进程并不会随父进程立刻结束。同样，父进程不会等待子进程执行完。
# 注意：os.fork()无法在windows上运行。
```

[p3_process.py](1进程/p3_process.py)

``` python
# 参数
# multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})

# - group：分组，实际上很少使用
# - target：表示调用对象，你可以传入方法的名字
# - name：别名，相当于给这个进程取一个名字
# - args：表示被调用对象的位置参数元组，比如target是函数a，他有两个参数m，n，那么args就传入(m, n)即可
# - kwargs：表示调用对象的字典

from multiprocessing import Process

def f(name):
    print(f'hello {name}')

if __name__ == '__main__':
    p = Process(target=f, args=('john',))
    p.start()
    p.join()
# join([timeout])
# 如果可选参数 timeout 是 None （默认值），则该方法将阻塞，
# 直到调用 join() 方法的进程终止。如果 timeout 是一个正数，
# 它最多会阻塞 timeout 秒。
# 请注意，如果进程终止或方法超时，则该方法返回 None 。
# 检查进程的 exitcode 以确定它是否终止。
# 一个进程可以合并多次。
# 进程无法并入自身，因为这会导致死锁。
# 尝试在启动进程之前合并进程是错误的。
```

> os.fork()用于研究多进程
> multiprocessing.Process()用于实际场景
