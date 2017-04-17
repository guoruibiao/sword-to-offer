# coding: utf8

# @Author: 郭 璞
# @File: string2number.py                                                                 
# @Time: 2017/4/14                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 将一个字符串转换成数字

def transfer(s):
    """
    用原始的方式实现
    :param s:  数字内容的字符串
    :return:  字符串转换后的数字
    """
    result = 0

    for index in range(len(s)):
        result += int(s[index])*pow(10, len(s)-1-index)
        print(result)
    return result

if __name__ == '__main__':
    s = '12345'
    result = transfer(s)
    print("'{}'转换成数字的结果为： {}".format(s, result))
    print(type(s))
    print(type(result))

