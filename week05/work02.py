#!/usr/bin/env python
import redis

'''
在使用短信群发业务时，公司的短信接口限制接收短信的手机号，每分钟最多发送五次
'''

cpool = redis.ConnectionPool(
    host='192.168.0.167', password='CentOS2020@', max_connections=5)
client = redis.Redis(connection_pool=cpool)


def send_msg(telephone_number, content, count):
    print(f"手机号 {telephone_number} 消息发送成功: {content} , 第{int(count) + 1}次")


def send_lefive(telephone_number: int, content, count):
    send_msg(telephone_number, content, count)
    client.incr(telephone_number)


def send_gtfive(telephone_number: int, content):
    client.expire(telephone_number, 60)
    print("每分钟相同手机号最多发送5次，请一分钟后重试 ... ...")


def send_count(sendsum, telephone_number: int, content):
    if sendsum in ['1', '2', '3', '4']:
        send_lefive(telephone_number, content, sendsum)
    else:
        send_gtfive(telephone_number, content)


def sendsms(telephone_number: int, content):
    sendsum = client.get(telephone_number)
    if not sendsum:
        send_msg(telephone_number, content, '0')
        client.set(telephone_number, 1)
    else:
        send_count(sendsum.decode(), telephone_number, content)


if __name__ == "__main__":
    sendsms(15012345678, 'hello')
    sendsms(15012345678, 'hello')
    sendsms(15012345678, 'hello')
    sendsms(15012345678, 'hello')
    sendsms(15012345678, 'hello')
    sendsms(13250307890, 'hello')
    sendsms(15012345678, 'hello')
