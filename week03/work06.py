#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Float, Column, Integer, DECIMAL, String, Date, DateTime, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

'''
张三给李四通过网银转账 100 极客币，现有数据库中三张表：

用户表：包含用户 ID 和用户名字，
用户资产表：包含用户 ID 用户总资产，
审计用表：记录了转账时间，转账 id，被转账 id，转账金额。

请合理设计三张表的字段类型和表结构；
请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。
'''

Base = declarative_base()


class User_table(Base):
    __tablename__ = 'GK_User'
    user_id = Column(Integer(), primary_key=True, autoincrement=True)
    user_name = Column(String(50), index=True)


class Assets_table(Base):
    __tablename__ = 'GK_User_Assets'
    user_id = Column(Integer(), primary_key=True)
    assets = Column(DECIMAL(15, 3), index=True)


class Audit_table(Base):
    __tablename__ = 'GK_Audit'
    uid_from = Column(Integer(), primary_key=True)
    uid_to = Column(Integer(), primary_key=True)
    posted_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    amount = Column(DECIMAL(21, 3), index=True)


# 实例一个引擎
dburl = "mysql+pymysql://testuser:testpass@192.168.0.168:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")
Base.metadata.create_all(engine)

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加用户数据
user_demo = User_table(user_name='李四')
user_demo2 = User_table(user_name='张三')
user_demo3 = User_table(user_name='王五')
session.add(user_demo)
session.add(user_demo2)
session.add(user_demo3)

session.commit()

# 增加资产数据
assets_demo = Assets_table(user_id=1, assets=1000.500)
assets_demo2 = Assets_table(user_id=2, assets=50.000)
assets_demo3 = Assets_table(user_id=3, assets=120.000)
session.add(assets_demo)
session.add(assets_demo2)
session.add(assets_demo3)
session.commit()

transfer_user = session.query(Assets_table).filter(
    Assets_table.user_id == 2).one()
be_transfered_user = session.query(Assets_table).filter(
    Assets_table.user_id == 1).one()

transfer_value = 100

if transfer_user.assets >= transfer_value:
    transaction_demo = Audit_table(uid_from=2, uid_to=1, amount=transfer_value )
    asset_demo2 = Assets_table(user_id=transfer_user, asset= transfer_user.assets - transfer_value )
    asset_demo1 = Assets_table(user_id=be_transfered_user, asset= be_transfered_user.assets +  transfer_value)
    session.commit()
    print('交易成功')
else:
    print('余额不足')
    session.rollback()
