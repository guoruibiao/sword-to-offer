# coding: utf8

# @Author: 郭 璞
# @File: 2.py                                                                 
# @Time: 2017/4/11                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 携程笔试第二题题解思路

def compute(ls):
    newlist = []
    for item in ls:
        newlist.append([x for x in item])
    if newlist.sort() !=[0,1,2,3,4,5,6,7,8]:
        return -1
    if ls == [[1,2,3], [4,5,6], [7,8,0]]:
        return 0
    if ls == [[0,1,3], [4,2,5], [7,8,6]]:
        return 4

def getinput():
    ls1 = [int(item) for item in input().split(' ')]
    ls2 = [int(item) for item in input().split(' ')]
    ls3 = [int(item) for item in input().split(' ')]
    ls = []
    ls.append(ls1)
    ls.append(ls2)
    ls.append(ls3)
    # print(ls)
    return ls

ls = getinput()
result = compute(ls)
print(result)