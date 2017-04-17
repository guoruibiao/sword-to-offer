# coding: utf8

# @Author: 郭 璞
# @File: 顺时针打印矩阵.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 使用顺时针的方向打印一个矩阵。

# TODO: 还是有点问题，对于奇数矩阵还是会多打印出重复数据。对于偶数矩阵可行。
def transfer(ls):
    """
    顺时针打印一个矩阵。需要考虑的是方阵和普通矩阵的情况。
    :param ls:
    :return:
    """
    row = len(ls)
    col = len(ls[0])
    # 对于奇数矩阵循环控制会有些困难！！！！！！！！！！尴尬。
    for outter in range(int((row)/2)):
        # 打印上面一层
        for x in range(outter, col-outter*2):
            print(ls[outter][x], end='\t')
        # 打印右边一列
        for y in range(1,row-outter*2):
            print(ls[y][col-1-outter], end='\t')
        # 打印下面一行
        for x in range(1,row-outter):
            print(ls[row-1-outter][col-1-x], end='\t')
        # 打印左边一列
        for y in range(1+outter,row- outter-1):
            print(ls[col-1-y][outter], end='\t')
        # 开始准备下一轮
        print()


if __name__ == '__main__':

    # ls = [
    #     [1,2],
    #     [3,4]
    # ]

    ls = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    # ls = [
    #     [1,2,3,4,5],
    #     [6,7,8,9,10],
    #     [11,12,13,14,15],
    #     [16,17,18,19,20],
    #     [21,22,23,24,25]
    # ]
    transfer(ls)