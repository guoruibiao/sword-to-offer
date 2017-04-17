# coding: utf8

# @Author: 郭 璞
# @File: 求1+2+到N.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 要求不使用乘除法，for，while，if,else,switch,case等关键字和三目运算实现这个和的运算。

def getsum(n):
    result = 0
    if n >0:
        result=getsum(n-1)+n
    return result

if __name__ == '__main__':
    result = getsum(5)
    print(result)



