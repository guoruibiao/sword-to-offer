# coding: utf8

# @Author: 郭 璞
# @File: getmethods.py                                                                 
# @Time: 2017/4/5                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 获取一个模块或者类中的所有方法及参数列表

import re

def parse(filepath, repattern):
    with open(filepath, 'rb') as f:
        lines = f.readlines()
    # 预解析正则
    rep = re.compile(repattern)
    # 创建保存方法和参数列表的结果集列表
    result = []
    # 开始正式的匹配实现
    for line in lines:
        res = re.findall(rep, str(line))
        print("{}的匹配结果{}".format(str(line), res))
        if len(res)!=0 or res is not None:
            result.append(res)
        else:
            continue
    return [item for item in result if item !=[]]


if __name__ == '__main__':
    repattern = "def (.[^_0-9]+\(.*?\)):"
    filepath = './TwoBranchTree.py'
    result = parse(filepath, repattern)
    for item in result:
        print(str(item))
