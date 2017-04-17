# coding: utf8

# @Author: 郭 璞
# @File: MergeSortedArray.py                                                                 
# @Time: 2017/4/15                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 将两个排序的数组merge成新的排好序的数组

def merge(arr1, arr2):
    result = []
    arr1len = len(arr1)
    arr2len = len(arr2)
    minlen = min(arr1len, arr2len)

    for index in range(minlen):
        temp1, temp2 = arr1[index],




if __name__ == '__main__':
    arr1 = [1,3,5,7,9]
    arr2 = [2,4,6,8,10]
    result = merge(arr1, arr2)
    print(result)
