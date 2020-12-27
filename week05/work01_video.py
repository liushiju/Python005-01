#!/usr/bin/env python
import redis

'''
写入电影相关信息
'''

def movie():
    client = redis.Redis(host='192.168.0.167',password='CentOS2020@')
    client.set('1001',0)
    client.set('1002',0)
    client.set('1003',0)

if __name__ == "__main__":
    movie()