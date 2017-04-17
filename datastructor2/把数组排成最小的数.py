# coding: utf8

# @Author: 郭 璞
# @File: 把数组排成最小的数.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 把数组排成最小的数

def fulllist(ls, result=[], position=0):
    if position == len(ls)-1:
        result.append(''.join(ls))
    else:
        for index in range(len(ls)):
            ls[index], ls[position] = ls[position], ls[index]
            fulllist(ls, result, position+1)
            ls[position], ls[index] = ls[index], ls[position]


def method1(ls):
    """
    借助“全排列”组装成数，再求最小的那个
    :param ls:
    :return:
    """
    resultlist = []
    fulllist(ls, resultlist, 0)
    return min([int(item) for item in resultlist])

if __name__ == '__main__':
    # ls = ['321', '32', '3']
    ls = ['12', '1']
    result = method1(ls)
    print(result)