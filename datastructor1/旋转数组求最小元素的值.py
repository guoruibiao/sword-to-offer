# coding: utf8

# @Author: 郭 璞
# @File: 旋转数组求最小元素的值.py                                                                 
# @Time: 2017/4/15                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 旋转数组求最小元素的值。如[3,4,5,1,2]是[1,2,3,4,5]数组的一个旋转。而且数组中的最小元素的值为1

def compute(ls):
    """
    对于旋转了0个单位的旋转数组，如[1,2,3,4,5]不会奏效，需要额外的处理。也即是对于此类特殊数组，采用顺序查找的方式解决。
    :param ls:
    :return:
    """
    ## 特殊情况处理，如11101是01111的旋转，此时只能采用顺序查找的方法了
    if ls[0] <= ls[-1]:
        minvalue = ls[0]
        pointer = len(ls)-1
        while pointer>=1:
            minvalue = minvalue if minvalue<ls[pointer] else ls[pointer]
            pointer -= 1
        return minvalue
    # 正常情况处理
    left = 0
    right = len(ls)-1
    while left<right:
        mid = int((left+right)/2)
        if ls[left]<ls[mid]:
            left = mid
        else:
            right = mid
        # 结束条件left恰好在right的左边
        if left+1 == right:
            return ls[right]

if __name__ == '__main__':
    # ls = [4,5,6,7,1,2,3]
    # ls = [1,2,3,4,5]
    ls = [1,1,1,0,1]
    result = compute(ls)
    print(result)
