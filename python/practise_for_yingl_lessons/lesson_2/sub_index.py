# coding=utf-8
'''
对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。 如果不存在，则返回 -1
其实就是str.find()
'''
def subIndexA(source, sub):
    exits = None
    i = 0
    while i <= len(source) - len(sub):
        for j in range(len(sub)):
            if source[i + j] != sub [j]:
                exits = False
                break
            else:
                exits = True
        if exits == True:
            return i
        i += 1
    if exits == False:
        return -1

#老师的做法
def subIndexB(source, target):
    if (source is None) or (target is None):
        return -1
    else:
        for i in range(len(source) - len(target) + 1):
            if source[i: i + len(target)] == target:
                return i
    return -1

s = "abcedf"
sub1 = "bce"
sub2 = "bcd"
print(subIndexA(s, sub1))
print(subIndexA(s, sub2))
print(subIndexB(s, sub1))
print(subIndexB(s, sub2))

