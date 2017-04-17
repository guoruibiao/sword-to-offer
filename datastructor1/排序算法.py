# coding: utf8

# @Author: 郭 璞
# @File: 排序算法.py                                                                 
# @Time: 2017/4/6                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description:Python实现的各种排序算法


############################################################快速排序
def getleftposition(ls, left, right):
    temp = ls[left]
    while left < right:
        while left < right and ls[right]>=temp:
            right -= 1
        ls[left] = ls[right]

        while left< right and ls[left]<= temp:
            left += 1
        ls[right] = ls[left]
    ls[left] = temp
    return left

def quicksort(ls, left, right):
    if left<=right:
        pivot = getleftposition(ls, left, right)
        quicksort(ls, left, pivot-1)
        quicksort(ls, pivot+1, right)

###########################################################################高级快速排序
def quicksortadvanced(ls):
    return [] if ls == [] else quicksortadvanced([x for x in ls[1:] if x < ls[0]]) + [ls[0]] + quicksortadvanced([x for x in ls[1:] if x >=ls[0]])

###########################################################冒泡排序
def bubblesort(ls):
    for i in range(len(ls)-1):
        for j in range(0, len(ls)-i-1):
            if ls[j]>ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]


###########################################################冒泡排序改进版
def bubblesort_advanced(ls):
    issorted = False
    for i in range(len(ls)-1):
        issorted = True
        for j in range(len(ls)-i-1):
            if ls[j]>ls[j+1]:
                issorted = False
                ls[j], ls[j+1] = ls[j+1], ls[j]
        if issorted:
            continue

########################################################### 直接选择排序
def directselect(ls):
    for i in range(len(ls)):
        position = i
        minvalue = ls[position]
        for j in range(i, len(ls)):
            if minvalue > ls[j]:
                minvalue = ls[j]
                position = j
        if position!= i:  ls[i], ls[position] = ls[position], ls[i]



########################################################### 桶排序: 有点失败，key按照了字典顺序排列，所以对于77和8 ，77会排列在前面
def bulketsort(ls):
    # 保存最终的数据集
    result = []
    # 用字典进行处理
    dic = {}
    for item in ls:
        dic[str(item)] = 0
    for item in ls:
        dic[str(item)] += 1
    dic = [(int(k),dic[k]) for k in sorted(dic.keys())]
    print(dic)
    for item in dic:
        key, times = int(item[0]), int(item[1])
        for i in range(0, int(times)):
            result.append(key)
    # 返回最终的结果集
    return result
############################################################### 字典相关的处理   http://python.jobbole.com/85124/

if __name__ == '__main__':
    ls = [2,5,1,-9,77,6,-81,8,3,5,4]
    # quicksort(ls, 0, len(ls)-1)
    # print(ls)
    # bubblesort(ls)
    # print(ls)
    # bubblesort_advanced(ls)
    # print(ls)
    # directselect(ls)
    # print(ls)
    # ls = bulketsort(ls)
    # print(ls)
    ls = quicksortadvanced(ls)
    print(ls)
