# coding: utf8

# @Author: 郭 璞
# @File: 霍夫曼树创建.py                                                                 
# @Time: 2017/4/6                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 实现一个霍夫曼树

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None
        self.charcode = ''

    def __str__(self):
        return str(self.value)+" : "+self.charcode

class Huffman(object):

    def __init__(self, items=[]):
        while len(items)!=1:
            a, b = items[0], items[1]
            newvalue = a.value + b.value
            newnode = Node(value=newvalue)
            newnode.left, newnode.right = a, b
            items.remove(a)
            items.remove(b)
            items.append(newnode)
            items = sorted(items, key=lambda node: int(node.value))
            # 每次都要记得更新新的霍夫曼树的根节点
            self.root = newnode

    def print(self):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value, end='\t')
            if(current.left):
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()

def sortlists(lists):
    return sorted(lists, key=lambda node: int(node.value))

def create_huffman_tree(lists):
    while len(lists)>1:
        a, b = lists[0], lists[1]
        node = Node(value=int(a.value+b.value))
        node.left, node.right = a, b
        lists.remove(a)
        lists.remove(b)
        lists.append(node)
        lists = sorted(lists, key=lambda node: node.value)
    return lists


def scan(root):
    if root:
        queue = [root]
        while queue:
            current = queue.pop(0)
            print(current.value, end='\t')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


# 根据创建好的霍夫曼打印出相应的编码信息
def computecode(root):
    current = root
    if current.left is None and current.right is None:
        current.charcode += str(current.value)
    if current.left:
        current.charcode += str('0')
        computecode(current.left)
    if current.right:
        current.charcode += str('1')
        computecode(current.right)

def printcode(root):
    current = root
    while current:
        if current.left is None and current.right is None:
            print(current.charcode)
        if current.left:
            current = current.left
        if current.right:
            current = current.right



if __name__ == '__main__':
    ls = [Node(i) for i in range(1, 5)]
    huffman = Huffman(items=ls)
    huffman.print()
    print('===================================, 下面的方式不正确的原因是ls已经被上面代码修改过了，需要重新设置一下！')
    lssl = [Node(i) for i in range(1, 5)]
    root = create_huffman_tree(lssl)[0]
    scan(root)
    print('编码结果获取')
    computecode(huffman.root)
    printcode(huffman.root)