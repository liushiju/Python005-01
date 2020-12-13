<h1>学习笔记

## <center>第一节：MySQL安装</center>

### 1、企业级MySQL部署在Linux操作系统上，，需要注意的重点
- 注意操作系统的平台（32位、64位）
- 注意安装MySQL的版本（MySQL企业版、社区版、mariadb）
- 注意安装后避免yum自动更新（yum updata）
    - 生产环境取消掉yum源
- 注意数据库的安全性

### 2、[获取社区版MySQL软件](https://dev.mysql.com/)
![image.png](attachment:image.png)

### 3、包mysql57-community-release-el7-10.noarch.rpm的作用
- 添加索引从网络中下载mysql一部分相关包
- mysql安装后，卸载该软件包(yum remove)，移除索引，这样确保Linux环境中一个MySQL版本，而且不会随着安全更新（yum update）导致MySQL版本发生变化

### 4、安装过程

```shell
[root@python mysql]# ls
mysql-community-client-5.7.32-1.el7.x86_64.rpm
mysql-community-common-5.7.32-1.el7.x86_64.rpm
mysql-community-libs-5.7.32-1.el7.x86_64.rpm
mysql-community-libs-compat-5.7.32-1.el7.x86_64.rpm
mysql-community-server-5.7.32-1.el7.x86_64.rpm
[root@python mysql]# yum -y install *.rpm
[root@python mysql]# rpm -qa |grep mysql
mysql-community-server-5.7.32-1.el7.x86_64
mysql-community-libs-5.7.32-1.el7.x86_64
mysql-community-common-5.7.32-1.el7.x86_64
mysql-community-libs-compat-5.7.32-1.el7.x86_64
mysql-community-client-5.7.32-1.el7.x86_64
[root@python mysql]# systemctl start mysqld
[root@python mysql]# systemctl enable mysqld
[root@python mysql]# systemctl status mysqld
● mysqld.service - MySQL Server
   Loaded: loaded (/usr/lib/systemd/system/mysqld.service; enabled; vendor preset: disabled)
   Active: active (running) since 一 2020-12-07 22:16:32 CST; 14s ago
     Docs: man:mysqld(8)
           http://dev.mysql.com/doc/refman/en/using-systemd.html
 Main PID: 4538 (mysqld)
   CGroup: /system.slice/mysqld.service
           └─4538 /usr/sbin/mysqld --daemonize --pid-file=/var/run/mysqld/mysqld.pid

12月 07 22:16:27 python systemd[1]: Starting MySQL Server...
12月 07 22:16:32 python systemd[1]: Started MySQL Server.
[root@python mysql]# grep 'password' /var/log/mysqld.log    # 初始化root用户密码在/var/log/mysqld.log日志中查询
2020-12-07T14:16:29.261543Z 1 [Note] A temporary password is generated for root@localhost: %QrvNyC:I4dv
[root@python mysql]# mysql -u root -p'%QrvNyC:I4dv'
```

## <center>第二节：正确使用MySQL字符集</center>

### 1、数据库相关操作

- 进入数据库后，首先修改密码

```mysql
mysql> ALTER USER 'root'@localhost IDENTIFIED BY 'your_password';
```

- 查看并修改密码设置规则

```mysql
mysql> show variables like 'validate_pass%';
+--------------------------------------+--------+
| Variable_name                        | Value  |
+--------------------------------------+--------+
| validate_password_check_user_name    | OFF    |
| validate_password_dictionary_file    |        |
| validate_password_length             | 8      |
| validate_password_mixed_case_count   | 1      |
| validate_password_number_count       | 1      |
| validate_password_policy             | MEDIUM |
| validate_password_special_char_count | 1      |
+--------------------------------------+--------+
7 rows in set (0.00 sec)

mysql> set global validate_password_policy=0;
Query OK, 0 rows affected (0.01 sec)

```

> 注意：生产环境中应该注意密码的安全性，设置复杂度高的密码

- 查看字符集

```mysql
mysql> show variables like '%character%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | latin1                     |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | latin1                     |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.02 sec)
```
> 在/etc/my.cnf配置文件中设置

```shell
[client]
default_character_set = utf8mb4

[mysql]
default_character_set = utf8mb4

[mysqld]

```

> utf8和utfmb4区别：<br>
> utf8最多只能存3个字符。utf8mb4最多能存4个字符。例如emoji表情、特殊中文字符是需要4个中文字符才能存储，所以需要用UTF-8（数据库中utf8mb4即是UTF-8）




- 查看校对规则

```mysql
```

> MySQL中utf8不是UTF-8字符集

- 开发环境中需要调整如下设置项

```mysql
interactive_timeout=28800  # 针对交互连接超时时间
wait_timeout=28800   # 针对非交互的超时时间
max_connections=1000    # MySQL的最大连接数
character_set_server = utf8mb4    # MySQL字符集设置
init_connect = 'SET NAMES utf8mb4'    # 服务器为每个连接的客户端执行的字符集
character_set_client_handshake = FALSE
collation_server = utf8mb4_unicode_ci
```


> 建立数据库时，如果没有指定字符集，默认根据`character_set_server`值设置，如果创建表时没有指定字符集，该表会继承数据库的字符集。如果新增字段没有指定字符集的时候会继承表的字符集。<br>
> 更新、查询的时候，会读取如下字符集

```mysql
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8mb4                    |
| character_set_connection | utf8mb4                    |
| character_set_database   | utf8mb4                    |
| character_set_filesystem | binary                     |
| character_set_results    | utf8mb4                    |
| character_set_server     | utf8mb4                    |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
```

- 创建数据库

```mysql
mysql> create database db1;
Query OK, 1 row affected (0.00 sec)

mysql> show create database db1;
+----------+--------------------------------------------------------------------------------------------+
| Database | Create Database                                                                            |
+----------+--------------------------------------------------------------------------------------------+
| db1      | CREATE DATABASE `db1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ |
+----------+--------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

```

> 创建数据库的时候后面会跟`COLLATE`校对规则，主要在字符集里用于字符比较和进行排序的一套规则，校对大小写是否敏感。默认校对规则设置，如下：

```mysql
mysql> show variables like 'collation%';
+----------------------+--------------------+
| Variable_name        | Value              |
+----------------------+--------------------+
| collation_connection | utf8mb4_unicode_ci |
| collation_database   | utf8mb4_unicode_ci |
| collation_server     | utf8mb4_unicode_ci |
+----------------------+--------------------+

# _ci    # 大小写不敏感
# _cs    # 大小写敏感
```

## <center>第三节：多种方式连接MySQL数据库</center>

### 1、python连接MySQL的方法

#### 统一概念
    - 其他语言：连接器、绑定、binding
    - python语言：python Database API、DB-API
    
> 注意：<font color=red>MySQLdb是Python2的包，适用于MySQL5.5和Python2.7</font>

#### Python3连接MySQL
- Python3按爪给你的MySQLdb包叫做mysqlclient，加载的依然是MySQLdb
- shell > pip install mysqlclient
- python > import MySQLdb

#### 其他DB-API
- shell > pip install pymysql    # 流行度高
- shell > pip install mysql-connector-python    # MySQL官方

#### 使用ORM（对象关系映射）
- shell > pip install sqlalchemy （需要与前面连接器结合）
- 还有一个是Django集成

#### 数据库操作

```mysql
mysql> create database testdb;
Query OK, 1 row affected (0.00 sec)
mysql> grant all privileges on testdb.* to 'testuser'@'%' identified by 'testpass';
Query OK, 0 rows affected, 1 warning (0.00 sec)
```

> **mod3_pymysql_conn.py**

```python
#!/usr/bin/python3
# PyMYSQL 连接 MySQL 数据库
# pip3 install PyMySQL
 
import pymysql

# 打开数据库连接
# mysql> create database testdb;
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';

db = pymysql.connect("server1","testuser","testpass","testdb" )
 
try:

    # 使用 cursor() 方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        sql = '''SELECT VERSION()'''
        # 使用 execute()  方法执行 SQL 查询 
        cursor.execute(sql)
        result = cursor.fetchone()
    db.commit()

except Exception as e:
    print(f"fetch error {e}")

finally: 
    # 关闭数据库连接
    db.close()

 
print (f"Database version : {result} ")
```

> **mod3_sqlalchemycore_conn.py**

```python
# sqlalchemy 连接 MySQL 数据库
# pip3 install sqlalchemy
#!/usr/bin/python3
 
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey

# 打开数据库连接
# mysql> create database testdb;
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
# echo=True 开启调试(生产环境去掉)
engine=create_engine("mysql+pymysql://testuser:testpass@server1:3306/testdb",echo=True)
 
# 创建元数据
metadata=MetaData(engine)
 
book_table=Table('book',metadata,
    Column('id',Integer,primary_key=True),
    Column('name',String(20)),
    )
author_table = Table('author', metadata,
    Column('id', Integer, primary_key=True),
    Column('book_id', None, ForeignKey('book.id')),
    Column('author_name', String(128), nullable=False)
    )

try:
    metadata.create_all()
except Exception as e:
    print(f"create error {e}")
```

> **mod3_orm_conn.py** （流行、覆盖其他变成语言）

```python
# ORM方式连接 MySQL 数据库
# pip3 install sqlalchemy
#!/usr/bin/python3
 
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# 打开数据库连接
# mysql> create database testdb;
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';

Base = declarative_base()  # 必须的

class Book_table(Base): 
    __tablename__ = 'bookorm'    # 创建表的名称
    book_id = Column(Integer(), primary_key=True)   # 必须要有一个组件，至少有一个Column类
    book_name = Column(String(50), index=True) 


# book_table=Table('book',metadata,
#     Column('id',Integer,primary_key=True),
#     Column('name',String(20)),
#     )

# 定义一个更多的列属性的类
# 规范写法要记得写在最上面
from datetime import datetime 
from sqlalchemy import DateTime

class Author_table(Base): 
    __tablename__ = 'authororm' 
    user_id = Column(Integer(), primary_key=True) 
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now) 
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

# 实例一个引擎
dburl="mysql+pymysql://testuser:testpass@server1:3306/testdb?charset=utf8mb4"
engine=create_engine(dburl, echo=True, encoding="utf-8")  # 显示设置utf-8

Base.metadata.create_all(engine)
```

## <center>第四节：必要的SQL知识</center>

### SQL语言功能划分
- DQL：Data Query Language，数据查询语言，开发工程师学习的重点
- DDL：Data Definition Language，数据定义语言，操作库和表结构
- DML：Data Manipulation Language，数据操作语言，操作表中记录
- DCL：Data Control Language，数据控制语言，安全和访问权限控制

### 创建表要注意哪些问题？

```mysql
CREATE TABLE `book` (
    `book_id` int(11) NOT NULL AUTO_INCREMENT,
    `book_name` varchar(255),
    PRIMARY KEY(`book_id`)
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE =  utf8_general_ci;
```

> 1、创建表之前检查数据库中表是否存在，如果存再执行指令会报错<br>
> 2、创建表语句使用反引号，名称有可能会出现单引号，为了避免该问题，保证它和MySQL保留字段的一些区别，一般创建字段的时候使用反引号<br>
> 3、指定字符集：当有些表不需要存例如emjio表情数据的时候，可以单独指定字符集

### 创建多表、多字段、设置约束条件建议（满足生产前提要求）
- 1、创建数据表的个数越少越好
- 2、表字段越少越好，相互独立，不建议字段的值是由其他字段计算出来的，这样会使数据冗余和检索效率会非常低
- 3、表联合主键的字段越少越好，联合主键中字段越多，索引占用空间越大，运行时间和效率变差
- 4、外键：如果是内部系统，只关注数据正确性，可以使用。如果是外部系统，外键要在应用层解决（类似公有云），外键和级联会造成更新阻塞，对于单机比较适用，但对于并发和分布式是完全不适用，会存在数据库更新的风暴风险（对性能非常敏感的数据不建议使用外键）

### SELECT查询关键字的顺序

```mysql
SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDERE BY ... LIMIT
```

> 注意：<br>
> 1、生产环境下因为列数相对较多，一般禁用SELECT * <br>
> 2、WHERE字段为避免全表扫描，一般需要增加索引

- 执行顺序

> FROM --> WHERE

```mysql
SELECT DISTINCT book_id,book_name, count(*) as number    #执行5
FROME book JION author ON book.sn_id = author.sn_id   # 执行1，筛选后会生产一个虚拟表，会使用不同的连接，连接到外部行
WHERE pages > 500    # 执行2，条件判断，生成新的虚拟表
GROUP BY book.book_id   # 分组排序，执行3，虚拟表分组排序
HAVING number > 10    # 筛选，执行4
ORDER BY number    # 以number顺序排序， 执行6
LIMIT 5   # 取前5个值，执行7
```

> 执行指令过程中，会产生中间虚拟表

## <center>第五节：使用聚合函数汇总数据</center>

### SQL函数有哪些？
- 算数函数
- 字符串函数
- 日期函数
- 转换函数
- 聚合函数

### 聚合函数
| | |
| :----: | :----: |
| COUNT() | 行数 |
| MAX() | 最大值 |
| MIN() | 最小值 |
| SUM() | 求和 |
| AVG() | 平均值 |

> 注意：聚合函数忽略空行；作用是汇总表的数据，数据量大的时候会比较消耗磁盘IO

- 特点
    - 输入一组数据集合，输出一个值
    - 忽略空行

### 示例

- 创建空数据库
```mysql
mysql> create database db1;
mysql> use db1
```

- 导入数据（方法1）
```mysql
mysql> source /root/t1.sql
```

- 导入数据（方法2）
```shell
# mysql -u<username> -p<password> < /root/t1.sql
```

> [t1.sql路径](https://gitee.com/liushiju/pythontrain/blob/master/version_2.0/week3/t1.sql)


```mysql
mysql> SELECT COUNT(*) FROM t1;
+----------+
| COUNT(*) |
+----------+
|      570 |
+----------+
1 row in set (0.01 sec)

mysql> SELECT COUNT(*),AVG(n_star),MAX(n_star) FROM t1 WHERE id < 10;
+----------+-------------+-------------+
| COUNT(*) | AVG(n_star) | MAX(n_star) |
+----------+-------------+-------------+
|        9 |      2.8889 |           5 |
+----------+-------------+-------------+
1 row in set (0.01 sec)

mysql> SELECT COUNT(*) ,n_star FROM t1 GROUP BY n_star;
+----------+--------+
| COUNT(*) | n_star |
+----------+--------+
|        9 |      1 |
|       56 |      2 |
|      315 |      3 |
|      150 |      4 |
|       40 |      5 |
+----------+--------+
5 rows in set (0.01 sec)
```

> 过滤分组`GROUP`的时候只能用`HAVING`不能用`WHERE`<br>
> `WHERE`只作用表中的每一行，`HAVING`作用与分组`GROUP BY`

```mysql
mysql> SELECT COUNT(*), n_star FROM t1 GROUP BY n_star HAVING n_star > 3 ORDER BY n_star DESC;
+----------+--------+
| COUNT(*) | n_star |
+----------+--------+
|       40 |      5 |
|      150 |      4 |
+----------+--------+
2 rows in set (0.00 sec)

```

## <font color=red><center>第六节：多表操作用到的子查询和join关键字解析（重点掌握）</center></font>

#### 什么是子查询
- 需要从查询结果中再次进行查询，才能得到想要的结果

#### 子查询需要关注的问题？
- 关联子查询与非关联子查询区别
    - 非关联子查询：外层一个for循环，里层只执行一次就可得到结果
    - 关联子查询：循环里面嵌套循环
    
- 何时用 IN，何时使用 EXISTS

#### 示例
- 非关联子查询

```mysql
mysql> SELECT COUNT(*),n_star FROM t1 GROUP BY n_star HAVING n_star > (SELECT avg(n_star) from t1) ORDER BY n_star DESC;
+----------+--------+
| COUNT(*) | n_star |
+----------+--------+
|       40 |      5 |
|      150 |      4 |
+----------+--------+
2 rows in set (0.01 sec)
```

> `SELECT avg(n_star) from t1`只调用一次

- 关联子查询

```mysql
mysql> SELECT * FROM TABLE_A WHERE condition IN (SELECT condition FROM TABLE_B)
mysql> SELECT * FROM TABLE_A WHERE EXISTS (SELECT condition FROM B WHERE B.condition=A.condition)

```

> 使用`EXISTS`或者`IN`就看`TABLE_A`和`TABLE_B`哪个大，小表驱动大表<br>
> <font color=red>当A<B时：使用EXISTS</font><br>
> <font color=red>当B<A时：使用IN</font><br>
    
- 类比理解(B<A)
```PYTHON
for i in TABLE_B:
    for j in TABLE_A:
        if TABLE_B.condition == TABLE_A.condition:
            ... ...
```

#### 常见的连接（join）有哪些？
- 自然连接
- ON连接
- USING连接
- 外连接
    - 左外连接
    - 右外连接
    - 全外连接（MySQL不支持）

![image.png](attachment:image.png)

## <center>第七节：事务的特性和隔离级别</center>

#### 什么是事务？
- 要么全执行，要么不执行

#### 事务的特性——ACID
- A：原子性（Atomicity）
    - 事务不可分割，要么成功，要么失败
- C：一致性（Consistency）
    - 由原来的一致状态变成另一种一致状态（成功or不成功）
- I：隔离性（Isolation）
    - 每个事务彼此独立
- D：持久性（Durabiolity）
    - 对数据修改持久
    
####  事务的隔离级别
- 读未提交：允许读到未提交的数据（不适用电商，MySQL日志，大量日志）
- 读已提交：只能读到已经提交的内容
- 可重复读：同一事务在相同查询条件下两次查询得到的数据结果一致（默认，强调一致性的时候选择）
- 可串行化：事务进行串行化，但牺牲了并发性能（加锁）

> MySQL默认自动提交<br>
> `show variables like 'autocommit'`<br>
> set autocommit=0;

- 开启事务
```mysql
BEGIN （关键字，开启）
COMMIT（提交）
ROLLBACK （回滚）
ROLLBACK TO （保存点，中间状态）
```

> 隔离级别越低，产生的有异常就会越多

## <center>第八节：PyMySQL的增删改查操作演示</center>

> 插入：mod_pymysql_insert.py

```python
#!/usr/bin/python3 
import pymysql
 
db = pymysql.connect("192.168.0.168","testuser","testpass","testdb")
 
try:

    # %s是占位符
    with db.cursor() as cursor:
        sql = 'INSERT INTO book (id, name) VALUES (%s, %s)'
        value = (1002, "活着")
        cursor.execute(sql, value)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally: 
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)
```

- 验证

```mysql
mysql> select * from book;
+------+--------+
| id   | name   |
+------+--------+
| 1002 | 活着   |
+------+--------+
1 row in set (0.00 sec)
```

> 查询：mod3_pymysql_query.py

```python
#!/usr/bin/python3 
import pymysql
 
db = pymysql.connect("192.168.0.168","testuser","testpass","testdb" )
 
try:

    # %s是占位符
    with db.cursor() as cursor:
        sql = '''SELECT name FROM book'''
        cursor.execute(sql)
        books = cursor.fetchall() # fetchone()
        for book in books: 
            print(book)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally: 
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)
```



> 更新：mod3_pymysql_update.py

```python
#!/usr/bin/python3 
import pymysql
 
db = pymysql.connect("192.168.0.168","testuser","testpass","testdb" )
 
try:

    # %s是占位符
    with db.cursor() as cursor:
        sql = 'UPDATE book SET id = %s WHERE name = %s'
        value = (1003, "活着")
        cursor.execute(sql, value)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally: 
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)
```

> mod3_pymysql_delete.py

```python
#!/usr/bin/python3 
import pymysql
 
db = pymysql.connect("192.168.0.168","testuser","testpass","testdb" )
 
try:

    # %s是占位符
    with db.cursor() as cursor:
        sql = 'DELETE FROM book WHERE name = %s'
        value = ("活着")
        cursor.execute(sql, value)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally: 
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)
```

## <center>第九节：多文件插入&如何设计一个良好的数据库连接配置文件</center>

> mod3_pymysql_insertmany.py

```python
#!/usr/bin/python3
import pymysql

db = pymysql.connect("192.168.0.168", "testuser", "testpass", "testdb")

try:

    # %s是占位符
    with db.cursor() as cursor:
        sql = 'INSERT INTO book (id, name) VALUES (%s, %s)'
        values = (
            (1004, "百年孤独"),
            (1005, "飘"),
        )
        cursor.executemany(sql, values)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally:
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)
```

> 执行多条查询，做数据库初始化，数据库大量写入的时候使用

- 设计配置文件考虑因素
    - 存储方式：文件（ini、yaml、json）更稳定
    - 可读性
    - 足够简单明确

> config.ini

```ini
[mysql]
host = 192.168.0.168
database = testdb
user = testuser
password = testpass
```

> dbconfig.py

```python
from configparser import ConfigParser


def read_db_config(filename='config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    # print(items)
    return dict(items)

if __name__ == "__main__":
    print(read_db_config())
```

> dbconnect.py

```python
import pymysql
from dbconfig import read_db_config

dbserver = read_db_config()
db = pymysql.connect(**dbserver)

try:

    # 使用 cursor() 方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        sql = '''SELECT VERSION()'''
        # 使用 execute()  方法执行 SQL 查询 
        cursor.execute(sql)
        result = cursor.fetchone()
    db.commit()

except Exception as e:
    print(f"fetch error {e}")

finally: 
    # 关闭数据库连接
    db.close()

 
print (f"Database version : {result} ")
```

## <center>第十节：使用SQLAlchemy插入数据到MySQL数据库</center>
## <center>第十一节：使用SQLAlchemy查询MySQL（上）</center>
## <center>第十二节：使用SQLAlchemy查询MySQL（下）</center>

> mod3_orm_insert.py

```python
# ORM方式连接 MySQL 数据库
# pip3 install sqlalchemy
#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Float, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

# 打开数据库连接
# mysql> create database testdb;
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
Base = declarative_base()

class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)

    def __repr__(self):
        return "Book_table(book_id='{self.book_id}', " \
            "book_name={self.book_name})".format(self=self)


class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
# Float 
# Decimal
# Boolean
# Text
# autoincrement 

# 业务逻辑
# 持久层
# 数据库层


# 实例一个引擎
dburl = "mysql+pymysql://testuser:testpass@192.168.0.168:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加数据
book_demo = Book_table(book_name='肖申克的救赎')
book_demo2 = Book_table(book_name='活着')
book_demo3 = Book_table(book_name='水浒传')
# author_demo = Author_table()
# print(book_demo)
# print(author_demo)

# 增加多条数据
# session.add(book_demo)
# session.add(book_demo2)
# session.add(book_demo3)
# session.flush()  # 不会结束事务，没有提交

# 使用迭代代替all()
# result = session.query(Book_table).all()
# for result in session.query(Book_table):
#     print(result)

# result = session.query(Book_table).first()
# 建议用first()，如果匹配到多行会报错
# one() 
# scalar()

# 指定列数
# session.query(Book_table.book_name).first()

# 排序
from sqlalchemy import desc
# for result in session.query(Book_table.book_name, Book_table.book_id).order_by(desc(Book_table.book_id)):
#      print(result)

# 降序
# query = session.query(Book_table).order_by(desc(Book_table.book_id)).limit(3)
# print([result.book_name for result in query])

# 聚合函数
# from sqlalchemy import func
# result = session.query(func.count(Book_table.book_name)).first()
# print(result)

# 条件
# print( session.query(Book_table).filter(Book_table.book_id < 20).first() )
filter(Book_table.book_id > 10, Book_table.book_id <20)

# 连接词
# from sqlalchemy import and_, or_, not_
# filter(
#     or_(
#         Book_table.xxx.between(100, 1000),
#         Book_table.yyy.contains('book')
#     )
# )
session.commit()
```

## <center>第十三节：使用SQLAlchemy更新和删除MySQL</center>

> mod3_orm_update_delete.py

```python
# ORM方式连接 MySQL 数据库
# pip3 install sqlalchemy
#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, desc, Table, Float, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()

class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)

    def __repr__(self):
        return "Book_table(book_id='{self.book_id}', " \
            "book_name={self.book_name})".format(self=self)

# 实例一个引擎
dburl = "mysql+pymysql://testuser:testpass@192.168.0.168:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()


# 更新
query = session.query(Book_table)
query = query.filter(Book_table.book_id == 20)
query.update({Book_table.book_name: 'newbook'})
new_book = query.first()
print(new_book.book_name)

# 删除
query = session.query(Book_table)
query = query.filter(Book_table.book_id == 18)
# session.delete(query.one())
query.delete()
print(query.first())



session.commit()
```

## <center>第十四节：使用连接池优化&数据库建立连接的过程</center>

> mod3_conn_pool.py

```python
import pymysql
# pip3 install DBUtils
from dbutils.pooled_db import PooledDB
db_config = {
  "host": "192.168.0.168",
  "port": 3306,
  "user": "testuser",
  "passwd": "testpass",
  "db": "testdb",
  "charset": "utf8mb4",
  "maxconnections":0,   # 连接池允许的最大连接数
  "mincached":4,        # 初始化时连接池中至少创建的空闲的链接,0表示不创建
  "maxcached":0,        # 连接池中最多闲置的链接,0不限制
  "maxusage" :5,        # 每个连接最多被重复使用的次数,None表示无限制
  "blocking":True       # 连接池中如果没有可用连接后是否阻塞等待
                        #  True 等待; False 不等待然后报错
}
 
spool = PooledDB(pymysql, **db_config) 

conn = spool.connection()
cur = conn.cursor()
SQL = "select * from bookorm;"
cur.execute(SQL)
f = cur.fetchall()
print(f)
cur.close()
conn.close()
```

## <center>第十五节：优化数据库使用的基本原则</center>

### 调优原则
- 调优不是万能的，升级硬件往往比调优效果更明显
- 调优的效果会随着次数增加，逐渐递减
- 应该有体系的调整，而不是发现一个参数可以改动就试试
    - 增加监控，根据监控，分析出调优的点
