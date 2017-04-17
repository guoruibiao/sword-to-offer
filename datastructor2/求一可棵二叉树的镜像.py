# coding: utf8

# @Author: 郭 璞
# @File: 求一可棵二叉树的镜像.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 求一可棵二叉树的镜像
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


def mirror(root):
    """
    求一棵二叉树的镜像树
    :return:
    """
    if root is None:
        return
    else:
        root.left, root.right = root.right, root.left
        mirror(root.left)
        mirror(root.right)


if __name__ == '__main__':
    tree = Tree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print('二叉树逆转之前：')
    tree.levelscan()
    # 开始镜像逆转
    mirror(tree.root)
    print('二叉树逆转之后：')
    tree.levelscan()