def fn(n):
    return lambda x: x * n

f2 = fn(2)
print(f2(3))