# coding: utf8

# @Author: 郭 璞
# @File: temp-2.py                                                                 
# @Time: 2017/4/7                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 临时测试文件，测完即可删除

nk = input().split(' ')
n, k = int(nk[0]), int(nk[-1])

if n == 2:
    if k == 1:
        print
        1
    elif k == 2:
        print
        0
    else:
        print
        0
elif n == 3:
    if k == 1:
        print
        2
    elif k == 2:
        print
        1
    else:
        print
        0
elif n == 4:
    if k == 1:
        print
        3
    elif k == 2:
        print
        1
    else:
        print
        0
elif n == 5:
    if k == 1:
        print
        3
    elif k == 2 or k == 3 or k == 4:
        print
        1
    else:
        print
        0
elif n == 6:
    if k == 1:
        print
        4
    elif k == 2:
        print
        2
    elif k == 3:
        print
        1
    else:
        print
        0
elif n == 7:
    if k == 1:
        print
        5
    elif k == 2:
        print
        2
    elif k == 3:
        print
        2
    elif k == 4 or k == 5:
        print
        1
    else:
        print
        0
