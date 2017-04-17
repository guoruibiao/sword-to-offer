# coding: utf8

# @Author: 郭 璞
# @File: 判断一棵二叉树是否为另一棵的子结构.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 判断一棵二叉树是否为另一棵的子结构，即子树。我的做法：遍历获取层次序列，判断序列是否在大树的序列中即可。

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




def getlevelstr(node):
    """
    层次遍历出二叉树的序列，返回一个字符串来代替
    :param node:
    :return:
    """
    result = ""
    queue = [node]
    while queue:
        temp = queue.pop(0)
        result += str(temp.data)
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
    return result

def getchildstr(tree1root, tree2, tree1lists = []):
    """
    判断tree2是否为tree1的子树，其实就是判断层次遍历得到的结果中.根节点相同的两棵小树的遍历结果是否一致。
    :param tree1:
    :param tree2:
    :return:
    """
    # 查找tree1中节点和tree2根节点相等的节点。
    if tree1root is None:
        return
    else:
        current = tree1root
        if current.data == tree2.root.data:
            tree1lists.append(getlevelstr(current))
        # 当前“根”不符合要求，也得继续往下走啊
        if current.left:
            getchildstr(current.left, tree2, tree1lists)
        if current.right:
            getchildstr(current.right, tree2, tree1lists)



if __name__ == '__main__':
    tree1 = Tree(8)
    tree1.root.left = Node(8)
    tree1.root.right = Node(7)
    tree1.root.left.left = Node(9)
    tree1.root.left.right = Node(2)
    tree1.root.left.right.left = Node(4)
    tree1.root.left.right.right = Node(7)
    tree1.root.left.right.right.left = Node(9)
    tree2 = Tree(8)
    tree2.root.left = Node(9)
    tree2.root.right = Node(2)
    tree2.root.right.left = Node(4)
    tree2.root.right.right = Node(7)

    # tree1.levelscan()
    # tree1.root = tree1.root.left
    # tree1.levelscan()
    # tree2.levelscan()

    # print(getlevelstr(tree1.root))

    tree1lists = []
    getchildstr(tree1.root, tree2, tree1lists)
    print(tree1lists)
    tree2str = getlevelstr(tree2.root)
    # 针对小树，其实还有可能是大树中子树的一部分，所以按照字符串包含与否来判断即可
    flag = False
    for tree1str in tree1lists:
        if tree2str in tree1str:
            flag = True
            break
    if flag:
        print('true')
    else:
        print('false')


