#!/usr/bin/env python
# Usage: python work01_counter.py 1001
import redis
import sys

'''
使用python+redis实现高并发计数器功能
'''

def counter(video_id):
    client = redis.Redis(host='192.168.0.167',password='CentOS2020@')
    client.incr(video_id)
    bcount_number = client.get(video_id)
    count_number = bcount_number.decode()
    return count_number

if __name__ == "__main__":
    video_id = sys.argv[1]
    count_num = counter(video_id)
    print(count_num)
