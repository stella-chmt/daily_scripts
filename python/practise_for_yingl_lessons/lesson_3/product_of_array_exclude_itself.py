# coding=utf-8

'''
数组剔除元素后的乘积。给定一个整数数组A。 定义B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]， 计算B的时候请不要使用除法。
给出A=[1, 2, 3]，返回 B为[6, 3, 2]
'''
def productExcludeItself(A):
    B = [1] * len(A)
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j:
                B[i] *= A[j]
    return B
'''
    # 如果能用除法
    multy = 1
    for i in A:
        multy *= i
    B = []
    for i in range(len(A)):
        B.append(multy / A[i])
    return B
'''

print(productExcludeItself([1, 2, 3]))