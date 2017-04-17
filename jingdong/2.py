# coding: utf8

# @Author: 郭 璞
# @File: 2.py
# @Time: 2017/4/7
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 京东笔试第二题，没思路。(⊙﹏⊙)b

n = int(input())
k = int(input())

temp = n%3

if k==1:
    if temp==0:
        print(int(n/3)*2)
    elif temp ==1:
        print(int((n+2)/3)*2)
    else:
        print(int((n + 1) / 3) * 2)
elif k ==2:
    if temp == 0:
        print(n-int(n / 3 * 2)+1)
    elif temp ==1:
        print(n-int((n+2)/3)*2)
    else:
        print(n - int((n + 1) / 3) * 2)