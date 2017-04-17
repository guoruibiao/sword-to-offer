# coding: utf8

# @Author: 郭 璞
# @File: 奇怪的表达式求值.py                                                                 
# @Time: 2017/4/7                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 输入为一行字符串，即一个表达式。其中运算符只有-,+,*。参与计算的数字只有0~9.
#  保证表达式都是合法的，排列规则如样例所示。从左往右依次计算即可，而且小易所在的世界没有除法，
#  输入：3+5*7  输出： 56
#  核心匹配公式：for times in range(len(s)-int((len(s)+1)/2)):

operator = "+-*"

def isnumber(a):
    return str(a).isalnum()

def isoperator(a):
    return str(a) in operator
#  核心匹配公式：for times in range(len(s)-int((len(s)+1)/2)):
def compute(s):
    s = list(s)
    result = 0
    for times in range(len(s)-int((len(s)+1)/2)):
        a = s[0]
        op = s[1]
        b = s[2]
        result = eval(str(a) + str(op) + str(b))
        s.pop(0)
        s.pop(0)
        s.pop(0)
        print(" 插入前：", s)
        s.insert(0, result)
        print(" 插入后：",s)
    return result

if __name__ == '__main__':
    s = '3+5*7+2-7'
    result = compute(s)
    print(result)