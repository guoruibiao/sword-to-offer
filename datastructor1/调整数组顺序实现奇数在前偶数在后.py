# coding: utf8

# @Author: 郭 璞
# @File: 调整数组顺序实现奇数在前偶数在后.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 实现奇数在前偶数在后的数组调换。

def transfer(ls):
    """
    遍历方式
    :param ls:
    :return:
    """
    if len(ls)==2:
        if ls[0]%2==0 and ls[1]%2 is not 0:
            ls[0], ls[1] = ls[1], ls[0]
    else:
        left = 0
        while left<len(ls):
            cur = ls[left]
            if cur%2==0:
                ls.append(cur)
                ls.pop(left)

            left += 1


def pointerway(ls):
    if len(ls) == 2:
        if ls[0] % 2 == 0 and ls[1] % 2 is not 0:
            ls[0], ls[1] = ls[1], ls[0]
    else:
        left = 0
        right = len(ls)-1
        while left<right:
            print('asd')
            if ls[left]%2==0 and ls[right]%2!=0:
                ls[left], ls[right] = ls[right], ls[left]
                left += 1
                right -= 1
            if ls[left]%2==0 and ls[right]%2==0:
                right -= 1
                continue
            if ls[left]%2!=0 and ls[right]%2==0:
                left += 1
                continue




if __name__ == '__main__':
    ls = [0,0,1,1,2,3,4,5,6,7,8,9]
    # transfer(ls)
    pointerway(ls)
    print(ls)
