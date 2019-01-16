# coding: utf8

# @Author: 郭 璞
# @File: 连续子数组的最大和.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 连续子数组的最大和

def run(ls):
    if ls == []:
        return
    if len(ls) == 1:
        return ls[0]
    else:
        currsum = ls[0]
        result = ls[0]
        for index in range(0, len(ls)):
            if currsum <= 0:
                currsum = ls[index]
            else:
                currsum += ls[index]
            if currsum > result:
                result = currsum

        return result

if __name__ == '__main__':
    ls = [1, -2, 3, 10, -4, 7, 2, -5]
    result = run(ls)
    print(result)
