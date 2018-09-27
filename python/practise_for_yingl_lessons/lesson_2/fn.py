'''
实现函数fn(n)，返回一个函数f，f(x) = n * x。（利用lambda表达式）
'''
def fn(n):
    return lambda x: x * n

f2 = fn(2)
print(f2(3))