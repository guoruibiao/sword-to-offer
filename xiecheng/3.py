# coding: utf8

# @Author: 郭 璞
# @File: 3.py                                                                 
# @Time: 2017/4/11                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 携程笔试第三题题解实现

def getinput():
    ls = [int(item) for item in input().split(' ')]
    return ls

def compute(ls, k):
    # 第一天为买进，
    shouyi = 0
    mairu = ls[0]
    maichu = 0
    #  1 2 3 5 2 6 3 7
    for index in range(k,len(ls), k):
        #print('dsadasdsads', index)
        if(index>=len(ls)):
            break
        maichu = ls[index+1]
        shouyi += (maichu - shouyi)
        mairu = maichu

    return shouyi

ls = getinput()
k = int(input())
result = compute(ls, k)
print(result)
