#!/usr/bin/env python
import socket
import pathlib
import subprocess

'''
编写传输文件服务端
'''
HOST = 'localhost'
PORT = 1111
savedir = pathlib.Path('/var/log')

# 接收客户端发送过来文件


def get_file(s, filename):
    data = s.recv(1024)
    filepath = pathlib.Path.joinpath(savedir, filename)
    print(filepath)
    print(data.decode())
    with open(filepath, 'w') as f:
        f.write(data.decode())
    s.sendall(f'{filename}文件已保存!'.encode())
    s.close()

# 根据客户端get请求发送本地文件给客户端


def put_file(s, filename):
    filepath = pathlib.Path.joinpath(savedir, filename)
    print(filepath)
    try:
        if not pathlib.Path.exists(filepath):
            print("服务器没有这个文件或目录")
        with open(filepath, 'r') as f:
            data = f.read()
            s.sendall(data.encode())
        print(f'{filename}已发送')
    except FileNotFoundError:
        s.sendall('file not found'.encode())
    s.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    try:
        while True:
            conn, addr = s.accept()
            print(f'client ip is {addr}')
            data = conn.recv(1024)
            if not data:
                print("客户端未正确输入")
                continue
            res = data.decode()
            if res == 'ls':
                continue
            f = res.split()[1].strip()
            print(f)
            if res.split()[0] == 'get':
                put_file(conn, f)
            if res.split()[0] == 'put':
                get_file(conn, f)
    except KeyboardInterrupt:
        pass
    s.close()


if __name__ == "__main__":
    main()
