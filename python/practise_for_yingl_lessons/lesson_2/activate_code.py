# coding=utf-8
'''
随机生成500个激活码，格式如下：XXXX-XXXX-XXXX-XXXX，每一位是数字或者大写英文字母
'''
import random

def activateCodeGenerate():
    x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', \
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', \
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', \
         'U', 'V', 'W', 'X', 'Y', 'Z']
    codes = []
    for i in range(0, 4):
        l = []
        for j in range(0, 4):
            l.append(x[random.randint(0, len(x)-1)])
        codes.append("".join(l))
    return "-".join(codes)

for i in range(0,500):
    print(activateCodeGenerate())