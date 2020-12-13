#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pymysql
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

'''
利用ORM方式创建表user01：
用户id    用户名    年龄    生日    性别    学历    字段创建时间    字段更新时间
'''

Base = declarative_base()


class User_table(Base):
    __tablename__ = "user01"
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    age = Column(Integer())
    birthday = Column(String(20))
    gender = Column(String(10))
    education = Column(String(10))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)


def create_user01_table():
    engine = create_engine(
        'mysql+pymysql://testuser:testpass@192.168.0.168:3306/testdb?charset=utf8mb4', echo=True, encoding='utf-8')
    Base.metadata.create_all(engine)

def insert_data():
    db = db = pymysql.connect("192.168.0.168","testuser","testpass","testdb")
    try:
        with db.cursor() as cursor:
            now = datetime.now()
            sql = '''INSERT INTO user01 (username, age, birthday, gender, education, created_on, updated_on) VALUES (%s, %s, %s, %s, %s, %s)'''
            values = (
                ('bob', 25, '1995-10-01', 'male', '本科',now, now),
                ('铁锤', 26, '1996-01-01', 'female', '研究生',now, now),
                ('aha', 30, '1989-12-23', 'male', '博士',now, now),
            )
            cursor.executemany(sql, values)
        db.commit()
    except Exception as e:
        print(f'insert error {e}')
    finally:
        db.close()
        print(f'insert {cursor.rowcount} rows')

def query_data():
    db = db = pymysql.connect("192.168.0.168","testuser","testpass","testdb")
    try:
        with db.cursor() as cursor:
            sql = '''SELECT * FROM user01'''
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                print(i)
        db.commit()
    except Exception as e:
        print(f'select error {e}')
    finally:
        db.close()
        print(f'select {cursor.rowcount} rows')



if __name__ == "__main__":
    create_user01_table()
    insert_data()
    query_data()