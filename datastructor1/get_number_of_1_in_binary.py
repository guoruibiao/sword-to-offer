# coding: utf8

# @Author: 郭 璞
# @File: get_number_of_1_in_binary.py                                                                 
# @Time: 2017/4/13                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 输出数字的二进制中的1的个数;  判断一个数是否为2的幂

def count(number):
    if number == 0:
        return 0
    else:
        counter = 0
        while number:
            number = number&(number-1)
            counter += 1
        return counter

def is_exp_of_2(number):
    return number&(number-1)==0

if __name__ == '__main__':
    print(count(1))
    print(count(2))
    print(count(3))
    print(count(4))
    print(count(5))
    print('-------------')
    print(is_exp_of_2(1))
    print(is_exp_of_2(2))
    print(is_exp_of_2(3))
