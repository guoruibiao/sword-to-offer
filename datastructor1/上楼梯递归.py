# coding: utf8

# @Author: 郭 璞
# @File: 上楼梯递归.py                                                                 
# @Time: 2017/4/6                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 一次可以1步，2步，3步，上10个台阶的所有可能的方法； 变态青蛙跳

def run(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    return run(n-1)+run(n-2)+run(n-3)

def forgjump(n):
    """
    青蛙一次可以跳一个台阶，2个台阶，，，n个台阶。求所有可能的解法
    Fib(n) = 2*Fib(n-1)     n >= 2
    :param n:
    :return:
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    index = 3
    total = 0
    while index <= n:
        total += 2*forgjump(n-1)
        index += 1
    return total


if __name__ == '__main__':
    # print(run(10))
    print(forgjump(3))
