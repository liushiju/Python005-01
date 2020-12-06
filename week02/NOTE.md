<h1>学习笔记

# <center> 第二周：掌握web开发的基石---HTTP协议</center>

## 课程资料

> 本周课程相关代码：https://gitee.com/wilsonyin/pythontrain/tree/master/version_2.0/week2

## <center>第一节：TCP/IP协议与socket编程的关系</center>

### 1、OSI参考模型与TCP/IP模型
![image.FK3QU0.png](attachment:image.FK3QU0.png)

### 2、socket编程

#### socket的工作原理

![image.ZAFUU0.png](attachment:image.ZAFUU0.png)

![image.JC6WU0.png](attachment:image.JC6WU0.png)

### 3、基于TCP的socket编程
#### socket API
- socket()
- bind()
- listen()
- accept()
- recv()
- send()
- colse()

> 实战：不使用开源框架的前提下完成一个echo服务端和echo客户端



## <center>第二节：写一个socket客户端</center>



> client1.py

```python
#!/usr/bin/env python
import requests
# pip install requests

r = requests.get('http://httpbin.org')
print(r.status_code)
print(r.headers)
# print(r.text)
```

> client2.py

```python
#!/usr/bin/env python
import socket
# AF_INET IPv4地址 ， SOCK_STREAM TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# debug
print(f"s1 : {s}")

s.connect(('www.httpbin.org', 80))

# debug
print(f"s2 : {s}")

s.send(b'GET / HTTP/1.1\r\nHOST:liushiju\r\nConnection: close\n\r\n')

buffer = []

while True:
    data = s.recv(2048)
    if data:
        buffer.append(data)
    else:
        break

s.close()

response = b''.join(buffer)

header, html = response.split(b'\r\n\r\n', 1)

print(header.decode('utf-8'))

with open('index.html', 'wb') as f:
    f.write(html)
```

## <center>第三节：Echo Server实战</center>





> echo_client.py

```python
#!/usr/bin/env python
import socket

HOST='localhost'
PORT=1111

def echo_client():
    """
    docstring
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    while True:
        data = input('input ~# >')
        if data == 'exit' or data == 'quit':
            exit(0)
        if not data:
            s.sendall('不输入内容，再牛的肖邦也弹不出哥的忧伤!'.encode())

        s.sendall(data.encode())
        data = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode())
    s.close()

if __name__ == "__main__":
    echo_client()
```

> echo_server.py

```python
#!/usr/bin/env python
import socket

HOST = 'localhost'
PORT = 1111

def echo_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
    while True:
        try:
            conn, addr = s.accept()
            print(f'client ip is {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
            conn.close()
        except KeyboardInterrupt as e:
            exit(1)
    s.close()

if __name__ == "__main__":
    echo_server()
```

## <center>第四节：web开发必备前端基础</center>


- 网页右击可查看源代码
- 需要关注的元素
    - link herf
    - body标签
    - a

- 浏览器调试工具F12
    - 指针可快速定位源代码位置
- CSS
    - header部分
    - 作用：结构和表现形式做分离
- js
    - 定义网页的一些行为
    - ajax异步数据同步技术
        - 通过xml方式发送请求，在展现网页整个结构之后，通过JavaScript来更新DOM，异步更新数据（可关注jQuery的dollar.ajax方法——目前异步更新网页数据的一个重要手段）
        
[jQueryAPI中文文档](https://www.jquery123.com/)

[W3CSchool教程](https://www.w3school.com.cn/)

[jQuery廖雪峰](https://www.liaoxuefeng.com/wiki/1022910821149312/1023022609723552)

    


## <center>第五节：HTTP协议和浏览器的关系</center>

- 利用python库模拟浏览器行为访问页面
- HTTP还能传输什么信息？
    - F12-->Network-->Headers（网页控制信息等信息）

- HTTP状态码（响应代码）
| 状态码 | 说明 |
| :----: | :----: |
| 1xx | 信息响应 |
| 2xx | 成功响应 |
| 3xx | 重定向 |
| 4xx | 客户端响应 |
| 5xx | 服务端响应 |

- POST方式：提交用户名密码
- GET方式：请求页面内容
- 模拟浏览器Headers
    - cookie
    - User-agent
- 需要熟悉标签
    - span：文字
    - a：链接
    - img：图片

## <center>第六节：requests库入门实战</center>

- 开发步骤
    - 提出需求
    - 编码
    - 代码run起来
    - 修复和完善
    
- 需求分析
    - 获取《豆瓣电影top250》内容 https://movie.douban.com/top250?start=0
- 要求
    - 获取电影名称、上映日期、评分
    - 写入文本文件

- 代码

> mod2_requests.py

```python
# 使用requests库获取豆瓣影评

import requests

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl,headers=header)

print(response.text)
print(f'返回码是: {response.status_code}')
```
    
> mod2_urlib.py

```python
from urllib import request

# GET 方法
resp = request.urlopen('http://httpbin.org/get')
print(resp.read().decode())

# POST 方法
resp = request.urlopen('http://httpbin.org/post', data=b'key=value', timeout=10)
print(resp.read().decode())

# cookie

from http import cookiejar
# 创建一个cookiejar对象
cookie = cookiejar.CookieJar()

# 创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)

# 创建Opener对象
opener = request.build_opener(handler)

# 使用opener来发起请求
resp = opener.open('http://www.baidu.com')

# 查看之前的cookie对象，则可以看到访问百度获得的cookie
for i in cookie:
    print(i)

# 之后使用urlopen方法发起请求时，都会带上这个cookie
```

## <center>第七节：异常捕获处理</center>

#### 一、requests扩展增加程序健壮性
    - 保存到文件中
        - with open方法（上下文管理器）
    - 异常处理
    
#### 二、异常捕获
    - 参考：[https://docs.python.org/zh-cn/3.6/library/exceptions.html](https://docs.python.org/zh-cn/3.6/library/exceptions.html)所有内置的非系统退出的异常都派生自Exception类
    - Stoplteration异常示例
    
```python
gennumber = (i for i in range(0, 2))
print(next(gennumber))
print(next(gennumber))

try:
    print(next(gennumber))
except StopIteration:
    print("最后一个元素")
```

- python中所有异常都会根据Traceback去追踪

```python
def a():
    return b()
def b():
    return c()
def c():
    x = 0
    res = 100/x
    return res

a()
```

![image.png](attachment:image.png)

#### 三、异常处理机制原理
- 异常也是一个类
- 异常捕获过程
    - 1、异常类把错误消息打包到一个对象
    - 2、然后该对象会自动查找到调用栈
    - 3、直到运行系统找到声明如何处理这些类异常的位置
    
- 所有异常继承自BaseExpection
- Traceback显示了出错的位置，显示的顺序和异常信息对象传播的方向是相反的

#### 四、异常信息与异常捕获
- 异常信息在Traceback信息的最后一行，有不同的类型
- 捕获异常可以使用try ... except 语法
- try ... expect 支持多重异常处理

##### 常见的异常类型主要有
- 1、LookupError 下的 IndexError 和 KeyError
- 2、IOError
- 3、NameError
- 4、TypeError
- 5、AttributeError
- 6、ZeroDivisionError

```PYTHON
try:
    1/0
except Exception as e:    # Exception捕获所有异常，继承自BaseExpection
    print(e) # 输出异常信息
```

> 程序没有捕获异常，当出现异常时候程序运行终止；捕获异常后可正常运行，当捕获异常的地方再出现异常，可以再嵌套try ... expect

```python
try:
    1/0
except Exception as e:
    try:
        1/0
    except Exception as f:
        pass
    print(e) 
```

> 一个try ... expect捕获一次输出后，当出现其他异常时不会再进行捕获
```python
def f1():
    1/0
def f2():
    list1 = []
    list1[1]
    f1()
def f3():
    f2()

try:
    f3()
except (ZeroDivisionError,Exception) as e:
    print(e)
```

#### 自定义异常
```python
class UserInputError(Exception):
    def __init__(self, Erroinfo):
        super().__init__(self, Erroinfo)  # 父类声明记录错误信息
        self.errorinfo = Erroinfo   # 父类中接收Erroinfo回来再赋值
    def __str__(self):  # 定义__str__方法后，就可以像字符串一样正常输出
        return self.errorinfo

userinput = 'a'

try:
    if (not userinput.isdigit()):
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue)
finally:
    del userinput  # 从内存中删除错误变量，释放内存
```

#### 美化异常输出---pretty_errors
- 安装：`pip install pretty_errors`

```python
import pretty_errors
def foo():
    1/0

foo()
```

![image.png](attachment:image.png)

## <center>第八节：重构：增加程序的健壮性</center>

### [requests官方文档](https://requests.readthedocs.io/zh_CN/latest/)

> mod2_requests_v2.py

```python
# 使用requests库获取豆瓣影评
import requests
from pathlib import *
import sys
# PEP-8
# Google Python 风格指引

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent':ua}

myurl = 'https://movie.douban.com/top250'

try:
    response = requests.get(myurl, headers=header)
except requests.exceptions.ConnectTimeout as e :
    print(f"requests库超时")
    sys.exit(1)

# 将网页内容改为存入文件
# print(response.text)

# 获得python脚本的绝对路径
p = Path(__file__)
pyfile_path = p.resolve().parent
# 建立新的目录html
html_path= pyfile_path.joinpath('html')

if not html_path.is_dir():
    Path.mkdir(html_path)
page = html_path.joinpath('douban.html')

# 上下文管理器
try:
    with open(page, 'w',  encoding='utf-8') as f:
        f.write(response.text)
except FileNotFoundError as e:
    print(f'文件无法打开,{e}')
except IOError as e:
    print(f'读写文件出错,{e}')
except Exception as e:
    print(e)
```

## <center>第九节：深入了解HTTP协议</center>

- 参见第八节官方文档

## <center>第十节：深入了解POST方式和cookie</center>

- POST
- cookie

> mod2_getandpost.py

```python
# http 协议的 GET 方法
import requests
r = requests.get('https://github.com')
r.status_code
r.headers['content-type']
# r.text
r.encoding
# r.json()

# http 协议的 POST 方法
import requests
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r.json()
```

> mod2_cookies.py

```python
import requests

# 在同一个 Session 实例发出的所有请求之间保持 cookie
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'

# 会话可以使用上下文管理器
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
```

> mod2_cookie_requests.py

```python
import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
'User-Agent' : ua.random,
'Referer' : 'https://accounts.douban.com/passport/login_popup?login_source=anony'
}

s = requests.Session()
# 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie， 
# 期间使用 urllib3 的 connection pooling 功能。
# 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
login_url = 'https://accounts.douban.com/j/mobile/login/basic'
form_data = {
'ck':'',
'name':'15055495@qq.com',
'password':'',
'remember':'false',
'ticket':''
}

# post数据前获取cookie
pre_login = 'https://accounts.douban.com/passport/login'
pre_resp = s.get(pre_login, headers=headers)

response = s.post(login_url, data=form_data, headers=headers, cookies=s.cookies)


# 登陆后可以进行后续的请求
# url2 = 'https://accounts.douban.com/passport/setting'

# response2 = s.get(url2,headers = headers)
# response3 = newsession.get(url3, headers = headers, cookies = s.cookies)

# with open('profile.html','w+') as f:
    # f.write(response2.text)
```
