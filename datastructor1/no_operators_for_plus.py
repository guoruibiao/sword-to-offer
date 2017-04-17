# coding: utf8

# @Author: 郭 璞
# @File: no_operators_for_plus.py                                                                 
# @Time: 2017/4/13                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 没有加法运算符的加法实现， 没有减法运算符实现减法运算

def plus(a, b):
    """
    数学之美。不使用加法操作符实现加法运算
    :param a:
    :param b:
    :return:
    """
    if a == 0:
        return b
    if b == 0 :
        return a

    # 异或得到本位
    basic = a ^ b
    # 移位得到进位， 只有结果为1的时候才需要进位
    carry = (a&b)<<1
    return plus(basic, carry)

def minus(a, b):
    if a == b:
        return 0
    # 减法运算其实就是加法运算的特殊标示，即一个负数加上另外一个数。所以先转化被减数为负数
    b = plus(~b, 1)
    return plus(a, b)

if __name__ == '__main__':
    # 测试加法实现, 例外情况： (-1, 7)
    # ls = [(1, 1), (1, 6), (0, 7), (-1, -7)]
    # for item in ls:
    #     result = plus(item[0], item[1])
    #     print("加法实现结果：{} + {} = {}".format(item[0], item[1], result))
    print(plus(-1, 7))

    # 测试减法实现， 例外情况： (3, 2),
    # ls = [(1, 1), (1, 3), (-1, 7), (-7, -7)]
    # for item in ls:
    #     res = minus(item[0], item[1])
    #     print("减法实现结果：{} - {} = {} ".format(item[0], item[1], res))
    print(minus(3, 2))
