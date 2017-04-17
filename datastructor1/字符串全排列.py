# coding: utf8

# @Author: 郭 璞
# @File: 字符串全排列.py                                                                 
# @Time: 2017/4/6                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description:  字符串全排列种类获取

def run(s):
    result = []
    s = list(s)
    digui(s, result, 0)
    return set(result)

def digui(s, resultset, position):
    if position == len(s)-1:
        resultset.append("".join(s))
    else:
        for index in range(0, len(s)):
            s[index], s[position] = s[position], s[index]
            digui(s, resultset, position+1)
            s[position], s[index] = s[index], s[position]

if __name__ == '__main__':
    s = 'abc'
    result = run(s)
    print(result)