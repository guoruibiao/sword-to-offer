# coding: utf8

# @Author: 郭 璞
# @File: 二叉树中和为某一个值的路径.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 二叉树中和为某一个值的路径

# TODO 哈哈，失败的作品。

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree(object):
    def __init__(self, data=None):
        self.root = Node(data, None, None)

    def levelscan(self):
        """
        层次遍历二叉树。也即是广度优先遍历二叉树。
        :return:
        """
        if self.root is None:
            return
        else:
            queue = [self.root]
            while queue:
                temp = queue.pop(0)
                print(temp.data, end='\t')
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        print()


def run(root, currsum, value, inlist=[], outlist=[]):
    if root is not None:
        currsum += root.data
        inlist.append(root.data)
        if currsum < value:
            run(root.left, currsum, value, inlist, outlist)
            run(root.right, currsum, value, inlist, outlist)

        if currsum == value:
            if root.left is not None and root.right is not None:
                addlist = inlist
                outlist.extend(addlist)
        inlist.pop(len(inlist)-1)


if __name__ == '__main__':
    tree = Tree(10)
    tree.root.left = Node(5)
    tree.root.right = Node(12)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(7)
    resultpath = []
    inlist = []
    run(tree.root, 10, 22,inlist, resultpath)
    print(resultpath)