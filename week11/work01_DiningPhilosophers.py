#!/usr/bin/env python
'''
哲学家就餐问题

测试用例
输入： n = 1 （1<=n<=60，n 表示每个哲学家需要进餐的次数。）

预期输出
[[4,2,1],[4,1,1],[0,1,1],[2,2,1],[2,1,1],[2,0,3],[2,1,2],[2,2,2],[4,0,3],[4,1,2],[0,2,1],[4,2,2],[3,2,1],[3,1,1],[0,0,3],[0,1,2],[0,2,2],[1,2,1],[1,1,1],[3,0,3],[3,1,2],[3,2,2],[1,0,3],[1,1,2],[1,2,2]]
'''

import queue
import threading
import time
import random


class CountDownLatch:
    def __init__(self, count):
        self.count = count
        self.condition = threading.Condition()

    def wait(self):
        try:
            self.condition.acquire()
            while self.count > 0:
                self.condition.wait()
        finally:
            self.condition.release()

    def count_down(self):
        try:
            self.condition.acquire()
            self.count -= 1
            self.condition.notifyAll()
        finally:
            self.condition.release()


class DiningPhilosophers(threading.Thread):
    def __init__(self, philosopher_number, left_fork, right_fork, operate_queue, count_latch):
        super().__init__()
        self.philosopher_number = philosopher_number
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.operate_queue = operate_queue
        self.count_latch = count_latch

    def eat(self):
        time.sleep(0.01)
        self.operate_queue.put([self.philosopher_number, 0, 3])

    def thinking(self):
        time.sleep(random.random())

    def pick_left_fork(self):
        self.operate_queue.put([self.philosopher_number, 1, 1])

    def pick_right_fork(self):
        self.operate_queue.put([self.philosopher_number, 2, 1])

    def put_left_fork(self):
        self.left_fork.release()
        self.operate_queue.put([self.philosopher_number, 1, 2])

    def put_right_fork(self):
        self.right_fork.release()
        self.operate_queue.put([self.philosopher_number, 2, 2])

    def run(self):
        while True:
            left = self.left_fork.acquire(blocking=False)
            right = self.right_fork.acquire(blocking=False)
            if left and right:
                self.pick_left_fork()
                self.pick_right_fork()
                self.eat()
                self.put_left_fork()
                self.put_right_fork()
                break
            elif left and not right:
                self.left_fork.release()
            elif right and not left:
                self.right_fork.release()
            else:
                time.sleep(0.01)
        print('哲学家_'+ str(self.philosopher_number) + ' count_down')
        self.count_latch.count_down()


if __name__ == '__main__':
    operate_queue = queue.Queue()
    fork_1 = threading.Lock()
    fork_2 = threading.Lock()
    fork_3 = threading.Lock()
    fork_4 = threading.Lock()
    fork_5 = threading.Lock()
    n = 1
    latch = CountDownLatch(5 * n)
    for _ in range(n):
        philosopher_0 = DiningPhilosophers(
            0, fork_5, fork_1, operate_queue, latch)
        philosopher_0.start()
        philosopher_1 = DiningPhilosophers(
            1, fork_1, fork_2, operate_queue, latch)
        philosopher_1.start()
        philosopher_2 = DiningPhilosophers(
            2, fork_2, fork_3, operate_queue, latch)
        philosopher_2.start()
        philosopher_3 = DiningPhilosophers(
            3, fork_3, fork_4, operate_queue, latch)
        philosopher_3.start()
        philosopher_4 = DiningPhilosophers(
            4, fork_4, fork_5, operate_queue, latch)
        philosopher_4.start()
    latch.wait()
    queue_list = []
    for i in range(5 * 5 * n):
        queue_list.append(operate_queue.get())
    print(queue_list)
