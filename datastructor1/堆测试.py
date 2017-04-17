# coding: utf8

# @Author: 郭 璞
# @File: 堆测试.py                                                                 
# @Time: 2017/4/6                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 堆Python标准库的内置堆的测试！

import heapq as hq
ls = []
hq.heappush(ls, 1)
hq.heappush(ls, 2)
hq.heappush(ls, 3)
print(hq.heappop(ls))
print(hq.heappop(ls))
print(hq.heappop(ls))