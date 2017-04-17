# coding: utf8

# @Author: 郭 璞
# @File: 杨氏矩阵.py                                                                 
# @Time: 2017/4/15                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 矩阵从左至右， 从上到下依次递增，求指定的一个数是否在此矩阵

def compute(maze, value):
    row = len(maze)
    col = len(maze[0])
    if value < maze[0][0]:
        return False
    if value > maze[row-1][col-1]:
        return False

    for x in range(row):
        for y in range(col):
            if maze[x][y] == value:
                return True
            elif maze[x][y] < value:
                # x, y = x+1, y+1  # 一开始就错在了这里，因为内层循环是依次往后走的
                continue
            elif maze[x][y] > value:
                if maze[x-1][y] == value:
                    return True
                if maze[x][y-1]==value:
                    return True
    return False




if __name__ == '__main__':
    maze = [
        [1,2,8,9],
        [2,4,9,12],
        [4,7,10,13],
        [6,8,11,15]
    ]
    value = 5
    result = compute(maze, value)
    print("存在{}吗？{}".format(value, result))
