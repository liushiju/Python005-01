# <center>第一节：如何正确区分Python版本</center>

## 一、Python有哪些版本

- Python不同版本
    - 官方文档[https://www.python.org/doc/versions](https://www.python.org/doc/versions)
    
> Python3与Python2不完全兼容

> 在日常工作中新任务尽量使用比最新的Python版本较低的1~2个版本，因为最新版本的可能有写库还不支持。如果是旧项目就需要考虑项目的版本

- 哪些第三方库支持的Python版本
    - 查看第三方库官网，会有说明支持哪个版本

## 二、不同版本有不同的特性

- 查看官方文档
    - 官方文档:[docs.python.org](https://docs.python.org)
   
- 主要查看差异化
    - 向后不兼容语法
        - 例如：Python3.7与Python3.6的async和awite做变量名的时候在Python3.7的时候做了保留的关键字，如果定义为变量名就会报错

- 新的内置特性

> 了解不同版本的用处：<br>1、在生产环境中该Python版本有哪些不兼容的设置，比如：关键字<br>2、新的内置特性，比如：使用版本哪些特性被引入，无论增强还是bug修复。<br>3、不同的Python版本会引入不同的bug

## 三、工作中都在用哪个版本
- Python3.7的新功能
    - 官方地址[https://docs.python.org/zh-cn/3.7/](https://docs.python.org/zh-cn/3.7/)

- 维护N年前的一般会用Python2.7版本
- 重新开发：Python3.7（为主）或Python3.8

> 建议：阅读官方文档，<font color=red>了解从Python3.5~Python3.9版本的特性</font>

## 四、生产环境中的Python安装

- 安装包的版本差异[https://www.python.org/downloads](https://www.python.org/downloads)

- 需要关注的差异
    - 1、操作系统平台差异
    - 2、操作系统32位和64位差异
    
- 下载源码编译安装

```shell
[root@liushiju ~]# wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
liushiju@liushiju-X99:~$ scp root@47.74.151.50:/root/Python-3.7.9.tgz .
liushiju@liushiju-X99:~$ tar -xvzf Python-3.7.9.tgz
liushiju@liushiju-X99:~$ cd Python-3.7.9
liushiju@liushiju-X99:~/Python-3.7.9$ sudo ./configure --with-ssl
liushiju@liushiju-X99:~$ sudo make
liushiju@liushiju-X99:~$ sudo make install
```

# <center>第二节：在不同操作系统中安装Python</center>

## 1、Python安装

> 注意：
> <br>1、安装目录不要有中文、空格、特殊字符
> <br>2、非必要情况下尽可能安装一个Python解释器
> <br>3、安装了多个版本的Python需注意PATH环境变量的设置

- 进入官方网站下载安装【Python3.7版本】
    - Ubuntu安装

```shell
~$ sudo apt-get install open-ssl
~$ sudo tar -xvf Python3.7.19.tar.gz
~$ cd Python3.7.19
~$ ./configure --with-ssl
~$ make
~$ make install
```

#  <center>第三节：多个Python解释器共存会有什么问题？</center>

- 人为规避
- 创建虚拟环境
- 调整制定运行Python版本，可以export PATH环境变量，在/etc/profile添加，设置位默认执行的Python执行的文件目录（调整Python版本执行顺序）
    - 可能会带来问题，如Linux系统默认安装的python2.7，需谨慎修改

## pip多版本

- 执行pip对应版本安装Python库，会相应的安装到指定版本中

> 注意：在执行二进制文件python和pip的时候，养成习惯执行下`python -V`、`pip -V`，查看对应版本

# <center>第四节：REPL初体验与pip使用技巧</center>
## Python和pip命令
- 1、Python命令：Python的解释器，官方采用CPython版本
- 2、pip命令：方便安装第三方库

## REPL（交互式解释器）
- 1、Python程序可以交互执行也可以采用文件形式加载执行

> 原始Python交互解释器

```python
(venv_Python) xxxx@base:~$ python
Python 3.7.9 (default, Aug 31 2020, 12:42:55) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> str1 = "Hello,Python!"  # 定义字符串
>>> print(str1)  # 打印字符串
Hello,Python!
>>> str1.upper()  # string的内置upper函数，将所有字符串大写
'HELLO,PYTHON!'
>>> type(str1)  # 查看str1的类型是什么
<class 'str'>
>>> help(str)  # 通过查询到的类型查看该string类型的方法函数有哪些
```

- 2、IPython可以扩展Python的交互功能

```shell
(venv_Python) xxx@base:~$ pip3 -V
pip 20.2.4 from /home/liushiju/anaconda3/envs/venv_Python/lib/python3.7/site-packages/pip (python 3.7)
(venv_Python) xxx@base:~$ pip3 install ipython

```
---

```python
In [1]: str1 = "Hello, Python!"

In [2]: str1
Out[2]: 'Hello, Python!'

In [3]: type(str1)
Out[3]: str

```

## pip安装加速
- 国内常见的镜像
> 1、豆瓣:[http://pypi.doubanio.com/simple/](http://pypi.doubanio.com/simple/)
> <br> 2、清华:[https://mirrors.tuna.tsinghua.edu.cn/help/pypi/](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

- 升级方法
    - 方法一
    ```shell
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple <software> -U
    ```
    - 方法二
    ```shell
    pip config set global.index-url http://pypi.doubanio.com/simple/
    pip install pip -U
    ```

- 配置文件
    - Windows：`c:\Users\xxx\pip\pip.ini`
    - Linux：`~/.pip/pip.conf`
- 配置文件格式
```shell
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

- 开发环境配置

```shell
(venv_Python) xxx@base:~$ mkdir -p .pip
(venv_Python) xxx@base:~$ cd .pip/
(venv_Python) xxx@base:~/.pip$ vim pip.conf
(venv_Python) xxx@base:~/.pip$ cat pip.conf 
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

# <center>第五节： Python常用IDE</center>
##  一、Visual Studio Code
- 1. Visual Studio Code 的安装
- 2. Visual Studio Code 常用快捷键演示

- 常用快捷键
    - （1）`Ctrl + shift + i`
        - <font color=red>格式化代码</font>
    - （2）`Ctrl + shift + a OR Ctrl + /`
        - <font color=red>注释选中代码或者取消代码的注释</font>
    - （3）`alt + 上下箭头`
        - <font color=red>上下移动本行代码</font>
    - （4）`Ctrl + shift + k`
        - <font color=red>删除本行代码</font>
    - （5）`Ctrl + shift + f`
        - <font color=red>搜索选中的代码</font>
    - （6）`Ctrl + shift + p`
        - <font color=red>打开命令窗口</font>
    - （7）`Ctrl + shift b`
        - <font color=red>运行程序</font>
    - （8）`shift + alt + 上下箭头 / Ctrl + shift + 上下箭头`
        - <font color=red>向上或向下边长光标，可以同步操作几行代码</font>

- 3. 使用 Visual Studio Code 和 print 函数调试一个有 Bug 的 Python 程序

## 二、其他常用IDE
- pycharm
- jupyter notebook

# <center>第六节：Python项目的一般开发流程及虚拟环境配置</center>
## 一、一般开发流程
- 1、搞清需求
- 2、编写源代码
- 3、使用Python解释器转换为目标代码
- 4、运行程序
- 5、测试
- 6、修复错误
- 7、再运行、测试

## 二、迁移部署
- 虚拟环境的用途和使用方法

> 创建虚拟环境：`python -m venv <venv1> `
> <br>激活虚拟环境：`source venv1/bin/activate`
> <br>退出虚拟环境：`deactivate`

- 部署到生产环境
    - 拷贝源代码到生产环境
    - 在开发环境中导出requirements文件：`pip freeze > requirements.txt`，并且拷贝到生产环境中
    - 生产环境中不从网络安装，从一个文件安装：`pip install -r requirements.txt`


- 如何正确使用官方文档

> 注意：
> <br>1、在生产环境中虚拟环境是保持环境一致性的必备工具
> <br>2、开发环境中可以不配置虚拟环境

# <center>第七节：Python的基本数据类型</center>
## 基本数据类型

| | |
| :----: | :---- |
| None | 空对象 |
| Bool | 布尔值 |
| 数值 | 整数、浮点数、复数 |
| 序列 | 字符串、列表、元组 |
| 集合 | 字典 |
| 可调用 | 函数 |





```python
100
```




    100




```python
0b10
```




    2




```python
0o10
```




    8




```python
0x10
```




    16




```python
3.5
```




    3.5




```python
5.8
```




    5.8




```python
int(5.8)
```




    5




```python
"123"
```




    '123'




```python
None
```


```python
var1 = None
```


```python
print(var1)
```

    None



```python
var1 is None
```




    True




```python
var2 = 123
var2 is None
```




    False




```python
x=10
y=20
x==y
```




    False




```python
x>y
```




    False




```python
x!=y
```




    True




```python
'abc'
```




    'abc'




```python
"abc"
```




    'abc'




```python
"""abc"""
```




    'abc'




```python
"I'm xxyy"
```




    "I'm xxyy"




```python
x="I'm xxyy"
```

> ### 注意：[查看字符串的内置方法(熟悉)](https://docs.python.org/zh-cn/3/library/stdtypes.html#text-sequence-type-str)


```python
y = ['a','b','c']
```


```python
y.append('d')
```


```python
y
```




    ['a', 'b', 'c', 'd']



>  ### 注意：[查看列表的内置方法(熟悉)](https://docs.python.org/zh-cn/3/library/stdtypes.html#list)


```python
z = ('a','b','c')
z
```




    ('a', 'b', 'c')



>  ### 注意：[查看元组的内置方法(熟悉)](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple)


```python
# python 之禅
import this
```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!



```python
dict1 = {'k1':'v1','k2':'v2'}
dict1
```




    {'k1': 'v1', 'k2': 'v2'}




```python
dict1['k1']
```




    'v1'




```python
dict1['k1'] = 'value3'
dict1
```




    {'k1': 'value3', 'k2': 'v2'}



>  ### 注意：[查看字典的内置方法(熟悉)](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict)

# <center>第八节：Python的高级数据类型</center>


### [collections --- 容器数据类型](https://docs.python.org/zh-cn/3/library/collections.html)

- nametuple()
    - 命名元组
- deque
    - 双端队列
- Counter
    - 计数器
- OrderedDict
    - 有顺序的字典


```python
In [1]: from collections import deque

In [2]: atog = deque('def')

In [3]: atog
Out[3]: deque(['d', 'e', 'f'])

In [4]: atog.append('g')

In [5]: atog
Out[5]: deque(['d', 'e', 'f', 'g'])

In [6]: atog.appendleft('c')

In [7]: atog
Out[7]: deque(['c', 'd', 'e', 'f', 'g'])

In [8]: for ele in atog:
   ...:     print(ele)
   ...: 
c
d
e
f
g
```

> 原子性：指事务的不可分割性，一个事务的所有操作要么不间断地全部被执行，要么一个也没有执行。

# <center>第九节：控制流</center>


|||
| :----: | :---- |
| 条件语句 | if...else |
| 循环语句 | for...in, while |
| 导入库、包、模块 | import |


```python
if True:
    print("True")
```

    True



```python
if False:
    print("nothing")
```


```python
num=100
if num>50:
    print('num>50')
else:
    print('num<50')
```

    num>50



```python
num=10
while num != 0:
    print(num)
    num -= 1
```

    10
    9
    8
    7
    6
    5
    4
    3
    2
    1



```python
list1 = ['a','b','c']
len(list1)
```




    3




```python
i=0
while i<len(list1):
    print(list1[i])
    i+=1
```

    a
    b
    c



```python
for i in list1:
    print(i)
```

    a
    b
    c


# <center>第十节：函数和模块的区别</center>

### 掌握常见Python模块

#### [time](https://docs.python.org/zh-cn/3/library/time.html)
#### [datetime](https://docs.python.org/zh-cn/3/library/datetime.html)
#### [logging](https://docs.python.org/zh-cn/3/library/logging.html)
#### [random](https://docs.python.org/zh-cn/3/library/random.html)
#### [json](https://docs.python.org/zh-cn/3/library/json.html)
#### [pathlib](https://docs.python.org/zh-cn/3/library/pathlib.html)
#### [os.path](https://docs.python.org/zh-cn/3/library/os.path.html)

> 一个或多个函数组成一个模块，多个模块放入一个文件夹中，对这个文件夹做特殊处理，该文件夹就成了包（函数--->模块--->包）

- 编写一个模块

> short.py

```python
def short_func():
    print('lift is short')
    
if __name__ == '__main__':
    short_func()
```

> main.py

```python
import short
short.short_func()
```

> 在Python里面双下划线写法叫做dander（了解）

# <center>第十三节：标准库---路径处理</center>

```python
In [1]: from random import *

In [2]: random()
Out[2]: 0.060672520329511426

In [3]: random()
Out[3]: 0.2194876916451558

In [4]: # 基于当前时间戳生成

In [6]: randrange(0,101,2)    # 生成0~101之间的任意偶数
Out[6]: 8

In [7]: choice(['red','blue','orange'])    # choice在列表中随机选择一个元素
Out[7]: 'orange'

In [8]: choice(['red','blue','orange'])
Out[8]: 'red'

In [9]: choice(['red','blue','orange'])
Out[9]: 'red'

In [10]: choice(['red','blue','orange'])
Out[10]: 'red'

In [11]: choice(['red','blue','orange'])
Out[11]: 'blue'
    
In [13]: # 随机抽取多个元素

In [14]: sample([1,2,3,4,5],k=4)
Out[14]: [1, 2, 4, 3]

In [15]: sample([1,2,3,4,5],k=4)
Out[15]: [5, 1, 3, 2]

In [18]: import json

In [19]: json.loads('["foo",{"bar":["baz",null,1.0,2]}]')    #对jason解码
Out[19]: ['foo', {'bar': ['baz', None, 1.0, 2]}]

In [20]: json.dumps("['foo', {'bar': ['baz', None, 1.0, 2]}]") #对json编码
Out[20]: '"[\'foo\', {\'bar\': [\'baz\', None, 1.0, 2]}]"'

In [1]: from pathlib import Path

In [2]: p = Path()

In [3]: p.resolve()
Out[3]: PosixPath('/Python/Python005-01/week01')    # 当前路径

In [1]: from pathlib import Path

In [2]: p = Path()

In [3]: p.resolve()   # 获取当前工作路径
Out[3]: PosixPath('/Python/Python005-01/week01')

In [4]: path="/usr/local/a.txt.py"

In [5]: p = Path(path)

In [6]: p
Out[6]: PosixPath('/usr/local/a.txt.py')

In [7]: p.name  #获取文件名
Out[7]: 'a.txt.py'

In [8]: p.stem #去除后缀
Out[8]: 'a.txt'

In [9]: p.suffix    # 获取后缀
Out[9]: '.py'
    
In [10]: p.suffixes    # 获取双扩展名
Out[10]: ['.txt', '.py']

In [11]: p.parent
Out[11]: PosixPath('/usr/local')    # 返回目录路径

In [12]: p.parents    #返回可迭代对象
Out[12]: <PosixPath.parents>

In [13]: for i in p.parents:
...:     print(i)
...: 
/usr/local
/usr
/

In [14]: p.parts   # 取出路径文件名
Out[14]: ('/', 'usr', 'local', 'a.txt.py')

In [1]: import os

In [2]: os.path.abspath('test.log')    # 获取文件名绝对路径
Out[2]: '/Python/Python005-01/test.log'

In [3]: path='/usr/local/a.txt'

In [4]: os.path.dirname(path)    # 获取文件所在目录
Out[4]: '/usr/local'

In [5]: os.path.exists('/etc/passwd')   # 判断文件或目录是否存在
Out[5]: True

In [6]: os.path.isfile('/etc/passwd')   # 判断是否为文件
Out[6]: True

In [7]: os.path.isdir('/etc/passwd')    # 判断是否为目录
Out[7]: False

In [8]: os.path.join('a','b')   # 文件路径的拼接
Out[8]: 'a/b'

In [9]: os.path.join('/a','b')
Out[9]: '/a/b'

```

# <center>第十四节：手动实现守护进程</center>

## deamon进程
- 一般运行在服务器端
- 作用
    - 当服务器启动的时候，无客户端连接时，为保证服务程序正常运行，而启用的进程
    - 脱离终端：当客户端终端关掉时，服务器无连接，服务仍然正常运行

> python Developer's Guide《python开发者指南》--> PEP Index ---> PEP 3143 -- Standard daemon process library 

> [官方：PEP 3143 -- Standard daemon process library](https://www.python.org/dev/peps/pep-3143/)

> 在实现一个daemon的时候可以参考官方文档

> 中文参考文章：[APUE:守护进程daemon](https://www.jianshu.com/p/fbe51e1147af)
> <br>另外参考网站：[stackoverflow](https://stackoverflow.com/questions/473620/how-do-you-create-a-daemon-in-python)

> daemon1.py

```python
#!/usr/local/bin/python3
import os
import sys
import time

'''
手动编写一个daemon进程
'''


def daemonize(stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    try:
        # 创建子进程
        pid = os.fork()

        if pid > 0:
            # 父进程先于子进程exit，会使子进程变成孤儿进程，
            # 这样子进程成功被init这个用户级守护进程收养
            sys.exit(0)
    except OSError as err:
        sys.stderr.write('_Fork #1 failed: {0}\n'.format(err))
        sys.exit(1)

    # 从父进程环境脱离
    # decouple from parent environment
    # chdir确认进程不占用任何目录，否则不能umount
    os.chdir('/')
    # 调用umask(0)拥有写任何文件的权限，避免继承自父进程的umask被修改导致自身权限不足
    os.umask(0)
    # setsid调用成功后，进程成为新的回话组长和新的进程组长，并与原来的登录会话和进程组脱离
    os.setsid()

    # 第二次fork
    try:
        pid = os.fork()
        if pid > 0:
            # 第二个父进程退出
            sys.exit(0)
    except OSError as err:
        sys.stderr.write('_Fork #2 failed: {0}\n'.format(err))
        sys.exit(1)

    # 重定向标准文件描述符
    sys.stdout.flush()
    sys.stderr.flush()

    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'w')

    # dup2函数原子化关闭和复制文件描述符
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

# 每秒打印一个时间戳


def test():
    sys.stdout.write('Daemon started with pid %d\n' % os.getpgid())
    while True:
        now = time.strftime("%X", time.localtime())
        sys.stdout.write(f'{time.ctime()}\n')
        sys.stdout.flush()
        time.sleep(1)


if __name__ == "__main__":
    daemonize('/dev/null', '/Python/Python005-01/week01/d1.log', '/dev/null')
    test()
```

# <center>第十五节：Python标准库：正则表达式实战</center>

## [正则表达式官方文档--通读*](https://docs.python.org/zh-cn/3.7/library/re.html)

# 本周作业

- 通过 Python 官方文档, 找到 Python 支持的基本数据类型，并列举各类型的<font color=red>定义</font>和<font color=red>赋值操作</font>（可以通过文本文档或思维导图形式提交总结）。
- （此作业需提交至 GitHub）编写一个函数, 当函数被调用时，将<font color=red>调用的时间记录在日志中</font>, 日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log
