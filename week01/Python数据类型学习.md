# 基本数据类型

| | |
| :----: | :---- |
| None | 空对象 |
| Bool | 布尔值 |
| 数值 | 整数、浮点数、复数 |
| 序列 | 字符串、列表、元组 |
| 集合 | 字典 |
| 可调用 | 函数 |

# 一、空对象

> 1、此对象会由不显示地返回值的函数所返回。不支持任何特殊的操作。
> <br> 2、空对象只有一种值：<font color=red>None（内置名称）</font>
> type(None)()会生成同一个单例

```python
In [11]: type(None)
Out[11]: NoneType

In [12]: type(None)()

In [13]: None
```


# 二、布尔值

> 1、布尔值具有两个常量对象值：<font color=red>False</font>和<font color=red>True</font>
> <br>2、表示逻辑上的真假
> <br> 3、在数字类上下文中（例如：用作算术运算符的参数时），0和1可以表示为真假
> <br>3、内置函数bool()可被用来将<font color=red>任意值转换为布尔值</font>

```python
In [15]: bool('dsd')
Out[15]: True

In [16]: bool('')
Out[16]: False

In [17]: bool(None)
Out[17]: False

In [18]: bool(False)
Out[18]: False

In [19]: bool(True)
Out[19]: True

In [21]: bool(123)
Out[21]: True

```

### 逻辑值检测

> 1、任何对象都可以进行逻辑值检测，以便用于if或while作为条件或布尔运算使用
> <br>2、一个对象在默认情况下均视为真值，除非该对象被调用时其所属类定义了 `__bool__()` 方法且返回 `False` 或是定义了 `__len__()` 方法且返回`零`

- 视为假值的内置对象
    - 被定义为假值的常量: None 和 False
    - 任何数值类型的零: 0、 0.0、 0j、 Decimal(0)、 Fraction(0, 1)
    - 空的序列和多项集: ''、 ()、 []、{}、 set()、 range(0)
    
> 产生布尔值结果的运算和内置函数总是返回 0 或 False 作为假值，1 或 True 作为真值

### 布尔运算

- 按优先级升序排列

| 运算 | 结果 | 注释 |
| :---- | :---- | :----: |
| x or y | if x is false,then y,else x| (1) |
| x and y | if x is false,then x,else y | (2) |
| not x | if x is false,then True,else Flse | (3) |

> 注释：<br>
> （1）这是个短路运算符，因此只有在第一个参数为假值时才会对第二个参数求值<br>
> （2）这是个短路运算符，因此只有在第一个参数为真值时才会对第二个参数求值<br>
> （3）not 的优先级比非布尔运算符低，因此 not a == b 会被解读为 not (a == b) 而 a == not b 会引发语法错误

# [三、数字类型--- int、float、complex](https://docs.python.org/zh-cn/3.7/library/stdtypes.html#numeric-types-int-float-complex)

> 构造函数int()、float()和complex()可以用来构造特定类型的数字

# [四、序列类型--- list、tuple、range](https://docs.python.org/zh-cn/3.7/library/stdtypes.html#sequence-types-list-tuple-range)

- 通用序列操作

| 运算 | 结果 |
| :---- | :---- |
| x in s | 如果s中的某项等于x则结果为True，否则为False |
| x not in s | 如果 s 中的某项等于 x 则结果为 False，否则为 True |
| s + t | s 与 t 相拼接 |
| s * n 或 n * s | 相当于 s 与自身进行 n 次拼接 |
| s[i] | s 的第 i 项，起始为 0 |
| s[i:j] | s 从 i 到 j 的切片 |
| s[i:j:k] | s 从 i 到 j 步长为 k 的切片 |
| len(s) | s 的长度 |
| min(s) | s 的最小项 |
| max(s) | s 的最大项 |
| s.index(x[, i[, j]]) | x 在 s 中首次出现项的索引号（索引号在 i 或其后且在 j 之前） | 
| s.count(x) | x 在 s 中出现的总次数

- 示例

```python
In [24]: "gg" in "eggs"
Out[24]: True

In [25]: "x" not in "yydz"
Out[25]: True

In [26]: s = "a"

In [27]: t = "b"

In [28]: s + t
Out[28]: 'ab'

In [29]: s[0]
Out[29]: 'a'
```

## list --- 可变序列

- 构建方式
    - 使用一对方括号表示空列表：[]
    - 使用方括号，其中的项以逗号分隔：[a]、[a,b,c]
    - 使用列表推导式：[x for x in interable]
    - 使用类型的构造器：list()或list(interable)

```python
In [49]: []
Out[49]: []

In [50]: [1,2,3]
Out[50]: [1, 2, 3]

In [51]: [x for x in range(10)]
Out[51]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [52]: list()
Out[52]: []

In [53]: list(range(10))
Out[53]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [54]: list((1,2,3,4))
Out[54]: [1, 2, 3, 4]
```

- sort方法

```python
In [75]: ll = [12,32,10,1,56,14]

In [76]: ll.sort()

In [77]: ll
Out[77]: [1, 10, 12, 14, 32, 56]
```

### 元组

> 元组是不可变序列，通常用于存储异构数据的多项集（ [enumerate()](https://docs.python.org/zh-cn/3.7/library/functions.html#enumerate) 内置函数所产生的二元组）

> 元组也被用于需要同构数据的不可变序列的情况（允许存储到 set 或 dict 的实例）

- 构建元组
    - 使用一对圆括号来表示空元组： ()
    - 使用一个后缀的逗号来表示单元组：a, 或 (a,)
    - 使用以逗号分隔的多个项：a, b, c or (a, b, c)
    - 使用内置的 tuple()： tuple() 或 tuple(iterable)

```python
In [1]: tuple("abc")
Out[1]: ('a', 'b', 'c')

In [2]: tuple([1,2,3])
Out[2]: (1, 2, 3)

In [3]: tuple(["x","y","z"])
Out[3]: ('x', 'y', 'z')
```


### 文本序列类型---str

- 字符串多种不同写法
    - 单引号: '允许包含有 "双" 引号'
    - 双引号: "允许包含有 '单' 引号"
    - 三重引号: '''三重单引号''', """三重双引号"""
    
### 字符串方法

> str.capitalize()<br>
> - 返回原字符串的副本，其首字母字符大写，其余小写

> str.casefold()<br>
>  - 返回原字符串消除大小写的副本。 消除大小写的字符串可用于忽略大小写的匹配
```python
In [14]: string = "abcd"

In [15]: string.capitalize()
Out[15]: 'Abcd'

In [16]: string.casefold()
Out[16]: 'abcd'
```





> str.center(width[, fillchar])<br>
> - 返回长度为 width 的字符串，原字符串在其正中。 使用指定的 fillchar 填充两边的空位（默认使用 ASCII 空格符）。 如果 width 小于等于 len(s) 则返回原字符串的副本。

>str.count(sub[, start[, end]])<br>
> - 反回子字符串 sub 在 [start, end] 范围内非重叠出现的次数。 可选参数 start 与 end 会被解读为切片表示法（左包右不包）。

```python
In [19]: string = "abc"

In [20]: string.center(2)
Out[20]: 'abc'

In [21]: string.center(5)
Out[21]: ' abc '

In [29]: string = "abddcde"

In [30]: string.count('d',0,2)
Out[30]: 0

In [31]: string.count('d',0,3)
Out[31]: 1

In [32]: string.count('d',0,4)
Out[32]: 2

In [33]: string.count('d',0,5)
Out[33]: 2

In [34]: string.count('d',0,6)
Out[34]: 3
```

> str.endswith(suffix[, start[, end]])<br>
> - 如果字符串以指定的 suffix 结束返回 True，否则返回 False。 suffix 也可以为由多个供查找的后缀构成的元组。 如果有可选项 start，将从所指定位置开始检查。 如果有可选项 end，将在所指定位置停止比较。

> str.expandtabs(tabsize=8)<br>
> - 返回字符串的副本，其中所有的制表符会由一个或多个空格替换，具体取决于当前列位置和给定的制表符宽度。 每 tabsize 个字符设为一个制表位（默认值 8 时设定的制表位在列 0, 8, 16 依次类推）。<br>
> - 要展开字符串，当前列将被设为零并逐一检查字符串中的每个字符。 如果字符为制表符 (\t)，则会在结果中插入一个或多个空格符，直到当前列等于下一个制表位。 （制表符本身不会被复制。） 如果字符为换行符 (\n) 或回车符 (\r)，它会被复制并将当前列重设为零。 任何其他字符会被不加修改地复制并将当前列加一，不论该字符在被打印时会如何显示。

```python
In [39]: string = "ilikepython"

In [40]: string.endswith('k',0,4)
Out[40]: True

In [41]: string.endswith('n')
Out[41]: True

In [42]: string.endswith(("thon"))
Out[42]: True
    
In [44]: '01\t012\t0123\t01234'.expandtabs()
Out[44]: '01      012     0123    01234'

In [45]: '01\t012\t0123\t01234'.expandtabs(4)
Out[45]: '01  012 0123    01234'

In [46]: '01\t012\t0123\t\r01234'.expandtabs(4)
Out[46]: '01  012 0123    \r01234'

In [47]: '01\t012\t0123\t\n01234'.expandtabs(4)
Out[47]: '01  012 0123    \n01234'
```

> str.find(sub[, start[, end]])<br>
> - 返回子字符串 sub 在 s[start:end] 切片内被找到的最小索引。 可选参数 start 与 end 会被解读为切片表示法。 如果 sub 未被找到则返回 -1。<br>

> str.format(*args, **kwargs)<br>
> - 执行字符串格式化操作。 调用此方法的字符串可以包含字符串字面值或者以花括号 {} 括起来的替换域。 每个替换域可以包含一个位置参数的数字索引，或者一个关键字参数的名称。 返回的字符串副本中每个替换域都会被替换为对应参数的字符串值。


```python
In [49]: 'Py' in 'Python'
Out[49]: True

In [50]: "The sum of 1+2 is {0}".format(1+2)
Out[50]: 'The sum of 1+2 is 3'
```

> str.index(sub[, start[, end]])
> - 类似于 find()，但在找不到子类时会引发 ValueError。

> str.isalnum()
> - 如果字符串中的所有字符都是字母或数字且至少有一个字符，则返回 True ， 否则返回 False 。 如果 c.isalpha() ， c.isdecimal() ， c.isdigit() ，或 c.isnumeric() 之中有一个返回 True ，则字符``c``是字母或数字。

```python
In [63]: string = "abcde"

In [64]: string.index('d')
Out[64]: 3

In [65]: string.index('d',0)
Out[65]: 3

In [66]: string.index('d',0,1)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-66-7a7d0dfa2948> in <module>
----> 1 string.index('d',0,1)

ValueError: substring not found

    In [67]: string.isalnum()
Out[67]: True

In [68]: ss = "asd123*"

In [69]: ss.isalnum()
Out[69]: False
```

> str.islower()
> - 如果字符串中至少有一个区分大小写的字符 4 且此类字符均为小写则返回 True ，否则返回 False 。

> str.istitle()
> - 如果字符串中至少有一个字符且为标题字符串则返回 True ，例如大写字符之后只能带非大写字符而小写字符必须有大写字符打头。 否则返回 False 。

> str.isupper()
> - 如果字符串中至少有一个区分大小写的字符 4 且此类字符均为大写则返回 True ，否则返回 False 。

> str.join(iterable)
> - 返回一个由 iterable 中的字符串拼接而成的字符串。 如果 iterable 中存在任何非字符串值包括 bytes 对象则会引发 TypeError。 调用该方法的字符串将作为元素之间的分隔。

> str.lower()
> - 返回原字符串的副本，其所有区分大小写的字符 4 均转换为小写。

> str.replace(old, new[, count])
> - 返回字符串的副本，其中出现的所有子字符串 old 都将被替换为 new。 如果给出了可选参数 count，则只替换前 count 次出现。

> str.split(sep=None, maxsplit=-1)
> - 返回一个由字符串内单词组成的列表，使用 sep 作为分隔字符串。 如果给出了 maxsplit，则最多进行 maxsplit 次拆分（因此，列表最多会有 maxsplit+1 个元素）。 如果 maxsplit 未指定或为 -1，则不限制拆分次数（进行所有可能的拆分）。

```python
In [70]: string = "aabc"

In [71]: string.islower()
Out[71]: True

In [72]: s2 = "Abcd"

In [73]: s2.istitle()
Out[73]: True

In [74]: s3 = "abcd"

In [75]: s3.isupper()
Out[75]: False

In [76]: s2.join(s3)
Out[76]: 'aAbcdbAbcdcAbcdd'

In [77]: s4 = "BDDF"

In [78]: s4.lower()
Out[78]: 'bddf'

In [79]: s4.replace('B','Z')
Out[79]: 'ZDDF'

In [80]: s4.split('D')
Out[80]: ['B', '', 'F']
```

> str.splitlines([keepends])
> - 返回由原字符串中各行组成的列表，在行边界的位置拆分。 结果列表中不包含行边界，除非给出了 keepends 且为真值。

- 此方法会以下列边界进行拆分

| 表示符 | 描述 |
| :----: | :----: |
| \n | 换行 |
| \r | 回车 |
| \r\n | 回车 + 换行 |
| \v 或 \x0b | 行制表符 |
| \f 或 \x0c | 换表单 |
| \x1c | 文件分隔符 |
| \x1d | 组分隔符 |
| \x1e | 记录分隔符 |
| \x85 | 下一行 (C1 控制码) |
| \u2028 | 行分隔符 |
| \u2029 | 段分隔符 |

```python
In [81]: 'ab c\n\nde fg\rkl\r\n'.splitlines()
Out[81]: ['ab c', '', 'de fg', 'kl']

In [82]: 'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
Out[82]: ['ab c\n', '\n', 'de fg\r', 'kl\r\n']
    
In [83]: "".splitlines()
Out[83]: []

In [84]: "One line\n".splitlines()
Out[84]: ['One line']

In [85]: ''.split('\n')
Out[85]: ['']

In [86]: 'Two lines\n'.split('\n')
Out[86]: ['Two lines', '']
```

> str.strip([chars])
> 返回原字符串的副本，移除其中的前导和末尾字符。 chars 参数为指定要移除字符的字符串。 如果省略或为 None，则 chars 参数默认移除空格符。 实际上 chars 参数并非指定单个前缀或后缀；而是会移除参数值的所有组合:

```python
In [87]:  '   spacious   '.strip()
Out[87]: 'spacious'

In [88]: 'www.example.com'.strip('cmowz.')
Out[88]: 'example'

In [89]: 'www.example.com'.strip('cmowzpxaele.')
Out[89]: ''

# 最外侧的前导和末尾 chars 参数值将从字符串中移除。 开头端的字符的移除将在遇到一个未包含于 chars 所指定字符集的字符时停止。 类似的操作也将在结尾端发生
In [90]: comment_string = '#....... Section 3.2.1 Issue #32 .......'

In [91]: comment_string.strip('.#! ')
Out[91]: 'Section 3.2.1 Issue #32'
```

> str.title()
> - 返回原字符串的标题版本，其中每个单词第一个字母为大写，其余字母为小写。

```python
In [93]: 'hello world'.title()
Out[93]: 'Hello World'
```

> str.upper()
> - 返回原字符串的副本，其中所有区分大小写的字符均转换为大写。 请注意如果 s 包含不区分大小写的字符或者如果结果字符的 Unicode 类别不是 "Lu" (Letter, uppercase) 而是 "Lt" (Letter, titlecase) 则 s.upper().isupper() 有可能为 False。

```python
In [94]: s = "hello world"

In [95]: s.upper()
Out[95]: 'HELLO WORLD'
```

# 五、映射类型 --- dict

### 创建
- 字典可以通过将以逗号分隔的 键: 值 对列表包含于花括号之内来创建
- 通过 dict 构造器来创建

```python
In [98]: a = dict(one=1, two=2, three=3)

In [99]: b = {'one':1, 'two':2, 'three':3}

In [100]: c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

In [101]: d = dict([('two', 2), ('one', 1), ('three', 3)])

In [102]: e = dict({'three': 3, 'one': 1, 'two': 2})

In [103]: a == b == c == d == e
Out[103]: True
```

### 字典支持操作

#### list(d)
> 返回字典d中使用的所有键的列表
    
```python
In [104]: d = {'one':1, 'two':2 , 'three':3}

In [105]: list(d)
Out[105]: ['one', 'two', 'three']

```

#### len(d)
> 返回字典d中的项数
    
#### d[key]
> 返回d中以key为键的项，如果映射中不存在key则会引发KeyError
 
#### d[key] = value
> 将d[key]设为value

#### del d[key]
> 将 d[key] 从 d 中移除。 如果映射中不存在 key 则会引发 KeyError。

#### key in d
> 如果 d 中存在键 key 则返回 True，否则返回 False

#### key not in d
> 等价于 not key in d

#### iter(d)
> 返回以字典的键为元素的迭代器。 这是 iter(d.keys()) 的快捷方式
    
#### clear()
> 移除字典中的所有元素。

#### copy()
> 返回原字典的浅拷贝。
    
#### get(key[, default])
> 如果 key 存在于字典中则返回 key 的值，否则返回 default。 如果 default 未给出则默认为 None，因而此方法绝不会引发 KeyError

#### items()
> 返回由字典项 ((键, 值) 对) 组成的一个新视图。

#### keys()
> 返回由字典键组成的一个新视图。
    
#### pop(key[, default])
> 如果 key 存在于字典中则将其移除并返回其值，否则返回 default。 如果 default 未给出且 key 不存在于字典中，则会引发 KeyError。

#### popitem()
> 从字典中移除并返回一个 (键, 值) 对。 键值对会按 LIFO 的顺序被返回。

#### setdefault(key[, default])
> 如果字典存在键 key ，返回它的值。如果不存在，插入值为 default 的键 key ，并返回 default 。 default 默认为 None。

#### update([other])
> 使用来自 other 的键/值对更新字典，覆盖原有的键。 返回 None。
    
#### values()
> 返回由字典值组成的一个新视图


