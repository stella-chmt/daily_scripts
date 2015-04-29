#!/usr/bin/python
#coding=utf-8

#判断一个整数是否为质数(大于1，且只能被1和自己整除的正数)
def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x > 0:
        for i in range(2,x):
            if x % i == 0:
                return False
        else:
            return True
    else:
        return False