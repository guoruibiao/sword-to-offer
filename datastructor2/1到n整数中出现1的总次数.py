# coding: utf8

# @Author: 郭 璞
# @File: 1到n整数中出现1的总次数.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 1到n整数中出现1的总次数。如输入12，包含1的有1,10,11,12.共5个1。

def compute(n):
    """
    循环除以10，判断个位数是否为1.
    :param n:
    :return:
    """
    total = 0
    for i in range(1, n+1):
        while i:
            if i%10 == 1:
                total += 1
            # 尤其注意Python中的除法是真除，即浮点数除法。
            i = int(i / 10)
    return total


if __name__ == '__main__':
    n = 12
    result = compute(n)
    print(result)
