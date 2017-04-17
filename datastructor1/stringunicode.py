# coding: utf8

# @Author: 郭 璞
# @File: 字符串全排列.py
# @Time: 2017/4/3                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 无重复的字母组成的不同的串

def entrance(s):
    if len(s)==0:
        return;
    result = []
    tempset = set([])
    digui(s, tempset, 0)
    result.extend(tempset)
    return result


def digui(chars, strset, position):
    # 递归终止条件， 一旦position到达倒数第二个位置即可停止
    if position == len(chars)-1:
        strset.add("".join(chars))
    else:
        for index in range(position, len(chars)):
            # 交换与position相邻的元素
            chars[position], chars[index] = chars[index], chars[position]
            print(chars)
            # 递归到下一个位置
            digui(chars, strset, position+1)
            # 记得交换回来
            chars[index], chars[position] = chars[position], chars[index]

if __name__ == '__main__':
    s = ['a', 'b', 'c']
    result = entrance(s)
    print(result)
