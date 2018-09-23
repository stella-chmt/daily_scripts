# coding=utf-8
'''
汉诺塔问题可以简单描述成为将a柱子上的圆盘按一定规则借助b柱子完美地复制到c柱子上。现假设有a，b，c三根柱子，
a柱子上的圆盘从上到下依次标号为1，2，3，……，n，且为递增状态。规则：每次移动一个盘子，且只能让小的放在大的上面。目标：移动到c柱子上，与原来a上的状态相同。
算法步骤：（1）将a上的除最下面一个盘子以外的n-1的圆盘借助c柱子移动到b柱子上。
　　　　　（2）将a上剩下的圆盘（即最下面的圆盘）移动到c柱子上。
　　　　　（3）将b上的刚才一过来的n-1个圆盘再借助a柱子移动到c上去。
　　　　　（4）任务完成。
定义hanoi函数，hanoi(圆盘数，初始柱，辅助柱，目标柱)
总的移动次数H(n) = 2^n - 1 (n>0)
---------------------

本文部分来自 John_kai 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/john_kai/article/details/72123970?utm_source=copy
'''

def hanoi(n, a, b, c):
    if n < 1 :
        print("Error!")
    elif n == 1 :
        print("将%s上的%d圆盘从柱子%s移到柱子%s" % (a, n, a, c))
    else:
        hanoi(n-1, a, c, b)
        print("将%s上的%d圆盘从柱子%s移到柱子%s" % (a, n, a, c))
        hanoi(n-1, b, a, c)

hanoi(4,'a','b','c')