# coding: utf8

# @Author: 郭 璞
# @File: 表达式互相转化.py                                                                 
# @Time: 2017/4/6                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 表达式转换，前缀中缀后缀
#    输入 a+b=c 输出（= （+ a  b））
#    输入 a+b+c输出 （+（+ a  b）c）
#    输入a*b+2 输出 （+（*  a  b）2）

# 判断是否为数字或者字母
def isnumberoralpha(item):
    return str(item).isalnum() or str(item).isalpha()

# 判断是否为操作符
def isoperator(item):
    return item in ['+', '-', '*', '/']

# 将中缀表达式转化为后缀表达式
def mid2post(mid):
    numstack = []
    opstack = []

    for item in mid:
        if isnumberoralpha(item):
            numstack.append(item)


# 计算后缀表达式的值      + 2 * a b
def compute_suffix(exp):
    exp = list(exp)
    print(exp)
    stack = []
    result = 0
    while exp:
        curr = exp.pop()
        if isnumberoralpha(curr):
            stack.append(curr)
        if isoperator(curr):
            a = stack.pop()
            b = stack.pop()
            result = eval(str(a) + str(curr) + str(b))
            exp.append(result)
    return result

if __name__ == '__main__':
    # mid = 'a+b+c'
    # result = mid2post(mid)
    # print(result)
    suffix = '+217*'
    result = compute_suffix(suffix)
    print(result)