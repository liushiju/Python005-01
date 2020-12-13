# 作业01
## 在Linux环境下，安装MySQL5.6以上版本，修改字符集为UTF8mb4并验证，新建一个数据库testdb，并为该数据库增加远程访问

- 安装并修改字符集
```shell
[root@python mysql]# ls
mysql-community-client-5.7.32-1.el7.x86_64.rpm
mysql-community-common-5.7.32-1.el7.x86_64.rpm
mysql-community-libs-5.7.32-1.el7.x86_64.rpm
mysql-community-libs-compat-5.7.32-1.el7.x86_64.rpm
mysql-community-server-5.7.32-1.el7.x86_64.rpm
[root@python mysql]# yum -y install *.rpm
[root@python mysql]# systemctl start mysqld
[root@python mysql]# systemctl enable mysqld

# 修改/etc/my.cnf配置文件
[client]
default_character_set = utf8mb4

[mysql]
default_character_set = utf8mb4

character_set_server = utf8mb4    # MySQL字符集设置
init_connect = 'SET NAMES utf8mb4'    # 服务器为每个连接的客户端执行的字符集

# 验证
mysql> show variables like '%character%';
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

# 新建testdb数据库，并增加远程访问
mysql> create database testdb;
mysql> show databases;
mysql> grant all privileges on testdb.* to 'testuser'@'%' identified by 'testpass';
```