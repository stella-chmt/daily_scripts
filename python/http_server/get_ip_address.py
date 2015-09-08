#encoding=utf-8
'''
Created on 2015-08-20
改变connect的ip可获取不同类型的本机ip，如8.8.8.8
'''
import socket


def get_local_ip():
    try:
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(('125.125.125.125', 80))
        (addr, port) = csock.getsockname()
        csock.close()
        return addr
    except socket.error:
        return "127.0.0.1"

print get_local_ip()

