#!/usr/bin/env python
import socket
import pathlib
import subprocess
import sys
'''
编写文件传输客户端
'''
HOST = 'localhost'
PORT = 1111
basedir = pathlib.Path.cwd()

# 下载文件


def get_file(s, filename):
    filepath = pathlib.Path.joinpath(basedir, filename)
    data = s.recv(1024)
    if data.decode() == 'file not found':
        print(data.decode())
    else:
        with open(filepath, 'w') as f:
            f.write(data.decode())
    s.close()

# 上传文件


def put_file(s, filename):
    filepath = pathlib.Path.joinpath(basedir, filename)
    if not pathlib.Path.exists(filepath):
        print("没有这个文件")
        sys.exit(1)
    with open(filename, 'rb') as f:
        data = f.read()
        s.sendall(data)
    data = s.recv(1024)
    print(data.decode())
    s.close()

# 列出当前目录文件


def ls():
    cmd = f"ls {basedir}"
    print(basedir)
    status, result = subprocess.getstatusoutput(cmd)
    if status != 0:
        print('error')
    print(result)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    try:
        while True:
            opcmd = input('input ~# > ')
            if not opcmd:
                print(
                    "Usage:\n  get <filename> : \t从服务器获取文件\n  put <filename> : \t从本地推送文件到服务器\n  ls : \t列出当前目录")
                continue
            if opcmd in ['exit', 'quit']:
                break
            if opcmd == 'ls':
                ls()
                continue
            print(opcmd.split()[0])
            s.sendall(opcmd.encode())
            if opcmd.split()[0] == 'get':
                get_file(s, opcmd.split()[1])
            if opcmd.split()[0] == 'put':
                put_file(s, opcmd.split()[1])
    except KeyboardInterrupt:
        pass
    s.close()


if __name__ == "__main__":
    main()
