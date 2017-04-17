# coding: utf8

# @Author: 郭 璞
# @File: 丑数相关.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 如果一个数的因子只是2,3,5，那么这个数被称为丑数。

def isUglyNumber(n):
    if n ==1:
        return True
    else:
        while n:
            n = int(n/2)
        while n:
            n = int(n/3)
        while n:
            n = int(n/5)
        return True if n == 1 else False

def commonway(k):
    """
    求从大到小排列的第n个丑数。但是这样的计算效率简直低的不能再低了。所以不采取。
    :return:
    """
    counter = 1
    target = None
    while counter<=k:
        for i in range(1000):
            if isUglyNumber(i):
                counter += 1
                print(target)
                target = i
    return target

if __name__ == '__main__':
    result = commonway(10)
    print(result)
    print(pow(2, 1499))

