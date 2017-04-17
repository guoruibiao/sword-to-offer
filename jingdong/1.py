# coding: utf8

# @Author: 郭 璞
# @File: 1.py                                                                 
# @Time: 2017/4/7                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 京东笔试第一题：求两个二进制数异或运算后的十进制的结果

a = '1100'
b = '0100'

def getlist(n, a, b):
    result = []
    for index in range(n):
        if a[index] != b[index]:
            result.append('1')
        else:
            result.append('0')
    return result



def compute(s):
    s.reverse()
    # print(s)
    sum = 0
    for index in range(len(s)):
        if s[index]!='0':
            sum += int(pow(2, int(index)))
    return sum

n = int(input())
a = input()
b = input()

result = getlist(n, a, b)
result = compute(result)
print(result)