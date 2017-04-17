# coding: utf8

# @Author: 郭 璞
# @File: JosephusRing.py                                                                 
# @Time: 2017/4/5                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 约瑟夫环问题

def notnonenumber(total):
    counter = 0
    for item in total:
        if item is not None:
            counter += 1
    return counter

def josephus(total, k):
    index = 0
    while notnonenumber(total)!= 1:
        index = (k + index) %len(total)
        print("我{}先出去了！".format(total[index]))
        total.remove(total[index])
    return total

if __name__ == '__main__':
    ls = [1,2,3,4,5,6,7,8,9,10]
    result = josephus(ls, 3-1)
    print('最后就剩下老子{}了！'.format(result))

