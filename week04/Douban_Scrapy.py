#!/usr/bin/env python
import requests
from fake_useragent import UserAgent
from lxml import etree

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey,desc,func,and_,or_,not_
from sqlalchemy.ext.declarative import declarative_base

useragent=UserAgent(verify_ssl=False)
headers={
    'User-Agent' : useragent.random
}
s=requests.Session()

firsturl='https://movie.douban.com/subject/26752088/comments?limit=20&status=P&sort=new_score'
secondurl='https://movie.douban.com/subject/26752088/comments?start=20&limit=20&status=P&sort=new_score'

first_resp = s.get(firsturl, headers=headers)
selector = etree.HTML(first_resp.text)
comment=selector.xpath('//div[@class="comment"]/p/span/text()')
star=selector.xpath('//div[@class="comment"]/h3/span[@class="comment-info"]/span[2]/@class')


commentstar=dict(zip(comment,star))

Base = declarative_base()

class Comment(Base):
    __tablename__='comment_star'
    comment_id=Column(Integer(),primary_key=True)
    comment=Column(String(1000))
    star=Column(String(50))

dburl="mysql+pymysql://doubanuser:doubanpass@192.168.0.168:3306/doubandb?charset=utf8mb4"
engine=create_engine(dburl,echo=True,encoding="utf-8")

Base.metadata.create_all(engine)

SessionClass=sessionmaker(bind=engine)
session=SessionClass()

for cs in commentstar :
    comment1=Comment(comment=cs,star=commentstar[cs])
    session.add(comment1)

session.commit()

second_resp = s.get(secondurl, headers=headers)
selector2 = etree.HTML(second_resp.text)
comment2=selector2.xpath('//div[@class="comment"]/p/span/text()')
star2=selector2.xpath('//div[@class="comment"]/h3/span[@class="comment-info"]/span[2]/@class')


commentstar2=dict(zip(comment2,star2))
for cs2 in commentstar2 :
    comment2=Comment(comment=cs2,star=commentstar2[cs2])
    session.add(comment2)

session.commit()

