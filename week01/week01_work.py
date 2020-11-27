#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import sys
import pathlib
import time
import logging
import subprocess

'''
编写日常巡检获取系统根目录使用容量脚本，可放入crond定时执行
'''


def _get_root_cap():
    # 设置日志路径
    logfiledir = pathlib.Path('/var/log/')
    dt = time.strftime("%Y%m%d", time.localtime())
    logdir = pathlib.Path.joinpath(logfiledir, 'python-{0}'.format(dt))
    if not pathlib.Path.exists(logdir):
        pathlib.Path.mkdir(logdir)
    logfile = pathlib.Path.joinpath(logdir,'getrootcap.log')
    # 配置log记录
    logging.basicConfig(filename=logfile,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG,
                        format='%(asctime)-8s - %(name)-8s - %(levelname)-8s - [line:%(lineno)d] - %(message)s'
                        )
    try:
        cmd = "df -h |awk '{if($NF==\"/\") print $(NF-1)}'"
        status, result = subprocess.getstatusoutput(cmd)
        # print(result)
        if status != 0:
            logging.error("cmd EXEC failed!")
            sys.exit(1)
        res = int(result.split('%')[0])
        if res > 90:
            logging.warning("Note that {0} of the root capacity is used".format(result))
        logging.debug("The root capacity is used {0}".format(result))
    except TypeError as e:
        logging.critical(e)


if __name__ == "__main__":
    _get_root_cap()
