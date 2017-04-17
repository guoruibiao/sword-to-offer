# coding: utf8

# @Author: 郭 璞
# @File: 数组中出现次数最多的那个元素的值.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 数组中出现次数最多的那个元素的值。如[1,2,3,4,5,6,2,2,2,2,27,8]结果为2

def run(ls):
    """
    基于桶排序原理，这里使用字典代替，统计每个元素出现的次数。但是天生对负数无效哦。切记！！！
    :param ls:
    :return:
    """
    dic = dict()
    for index in range(max(ls)):
        dic[str(index)] = 0
    # 开始统计
    for item in ls:
        if str(item) in dic.keys():
            dic[str(item)] += 1
    # 返回出现次数最多的那个元素的值
    temp = -1
    target = 0
    for key, value in dic.items():
        if temp <=value:
            target = key
            temp = value
    return target

if __name__ == '__main__':
    ls = [1,2,3,4,5,6,2,2,2,2,27,7,7,7,7,7,7,7,78,9]
    result = run(ls)
    print(result)