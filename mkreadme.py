# coding: utf8

# @Author: 郭 璞
# @File: mkreadme.py                                                                 
# @Time: 2017/4/14                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 将当前目录中所有的文件生成markdown文件特有的链接形式

import os
import re

def pathwalk(path='.', result=[]):
    dirlist = os.listdir(path=path)

    for item in dirlist:
        child = os.path.join(path, item)
        if os.path.isfile(child):
            result.append(child)
            # print(child)
        else:
            pathwalk(child, result)


def getdescription(list):
    return "".join([str(item) for item in list if "@Description:" in str(item)])

def generate(files=[], outputpath='./readme.md'):
    info = {}
    for file in files:
        if 'readme.' in str(file):
            continue
        with open(file, 'r', encoding='utf8') as f:
            temp = getdescription(f.readlines())
            temp = temp[15:]
            info[str(file)] = temp
            f.close()
    # print(len(info), info)
    info = {k:v for k,v in info.items() if v!='' and 'readme.' not in str(k)}
    print(len(info), info)

    # 生成Markdown文件
    with open(outputpath, 'a', encoding='utf8') as f:
        # f.write('标题部分\n---')
        for key, value in info.items():
            temp = " - [{}]({})\n\n".format(value, key)
            f.write(temp)
        f.close()
    print('文件已生成！')




if __name__ == '__main__':
    path = '.'
    result = []
    pathwalk(path, result)
    print(result)
    generate(result)
