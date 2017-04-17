# coding: utf8

# @Author: 郭 璞
# @File: 二进制运算相关.py
# @Time: 2017/4/15                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 求一个数二进制中1的个数

def rightscroll(n):
    """
    每次将数字与1相与运算，然后判断是不是1，之后把数字右移.
    但是这种方式只适用于正数，否则对于负数右移后需要保留符号，最终会陷入死循环。
    :param n:
    :return:
    """
    counter = 0
    while n:
        if n&1:
            counter += 1
        n = n >> 1
    return counter

def leftscroll(n):
    """
    既然右移对于负数不成立，那么试试左移。移动判断标记来间接实现。
    尴尬的是：并不能正确运行。。。
    :param n:
    :return:
    """
    counter = 0
    flag = 1
    while flag:
        if n&flag:
            counter += 1
        flag = flag << 1
    return counter


def advanced(n):
    """
    高级用法.实现求一个数的二进制表示法中1的个数。
    :param n:
    :return:
    """
    counter = 0
    while n:
        counter += 1
        n = n&(n-1)
    return counter


def isexpof2(n):
    """
    判断一个数是否为2的幂
    :param n:
    :return:
    """
    return n&(n-1)==0


def m2n(m, n):
    """
    给定的数m和n，求二者的二进制表示法，中经过几次可以变成一样的。
    按照思路：先求出二进制，然后对比二者之间对应位置上数字不一致的个数，就是结果了
    :param m:
    :param n:
    :return:
    """
    result = m^n
    counter = advanced(result)
    return counter

if __name__ == '__main__':
    n = 0xFFFFFFFF
    # result = rightscroll(n)
    # result = leftscroll(n)
    # print(result)
    # result = advanced(n)
    # print(result)

    # result = isexpof2(7)
    # print(result)
    result = m2n(10, 13)
    print(result)