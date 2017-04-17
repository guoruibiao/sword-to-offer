# coding: utf8

# @Author: 郭 璞
# @File: 打印1到n之间的所有数字.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 打印1到n位长度的所有数字，如n=2, 则打印1-99；n=3,打印1-999.

# TODO: 本题未完成，待修改！

def run(n):
    if n <=0 :
        return
    ls = []
    for index in range(10):
        ls[0] = str(index)+'0'
        printRecursively(ls, n, 0)
    del ls

def printRecursively(ls, length, index):
    if index == length - 1:
        printNumber(ls)
        return
    for i in range(10):
        ls[index+1] = str(index)+"0"
        printRecursively(ls, length, index+1)

def printNumber(ls):
    print(ls)

if __name__ == '__main__':
    run(3)