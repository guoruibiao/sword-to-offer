# coding: utf8

# @Author: 郭 璞
# @File: Backage.py                                                                 
# @Time: 2017/4/6                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 一个背包里面可以存放重量为weight的物品， 现有n件物品的集合s,其中质量分别为w0, w1,...wn-1.问能否从中选出若干物品，其和正好为weight

def compute(weight, items, n):
    if weight == 0:
        return True
    if weight < 0 or n <0 or n > len(items):
        return False
    if compute((weight-items[n-1]), items, n-1):
        print("Item: {}".format(items[n-1]))
        return True
    if compute(weight, items, n - 1):
        return True
    else:
        return False

def compute2(weight, items, n):
    if weight == 0:
        return True
    if weight < 0 or n <0 or n > len(items):
        return False
    if compute(weight, items, n - 1):
        return True
    if compute((weight-items[n]), items, n-1):
        print("Item: {}".format(items[n]))
        return True

if __name__ == '__main__':
    items = [1,2,3,4,5,6,7,8,9]
    weight = 31
    compute(weight, items, len(items))
    print('--------------------------')
    compute2(weight, items, len(items))