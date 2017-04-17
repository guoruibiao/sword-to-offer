# coding: utf8
# @Description: Python实现霍夫曼树

import random


# 定义节点
class Node:
    def __init__(self, weight=0, left=None, right=None):
        self.weight = weight
        self.left = left
        self.right = right


# 按权值排序
def sort(list):
    return sorted(list, key=lambda node: node.weight)


# 构建哈夫曼树
def Huffman(list):
    while len(list) != 1:
        a, b = list[0], list[1]
        new = Node()
        new.weight = a.weight + b.weight
        new.left, new.right = a, b
        list.remove(a)
        list.remove(b)
        list.append(new)
        list = sort(list)
    return list


# 中序遍历
def traval(First):
    if First == None: return
    print(First.weight)
    traval(First.left)
    traval(First.right)


# 获得树的长度
def get_height(node):
    if node.left == None and node.right == None: return 1
    return get_height(node.left) + get_height(node.right)


if __name__ == '__main__':
    list = []

    for i in range(1, 11):
        list.append(Node(i))

    list = sort(list)

    head = Huffman(list)[0]
    traval(head)
