# coding: utf8

# @Author: 郭 璞
# @File: 重建二叉树.py                                                                 
# @Time: 2017/4/15                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 根据前序遍历序列，中序遍历序列，重建一棵二叉树
class Node(object):

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def generate(pre=[], mid=[]):
    if len(pre) == 0:
        return None
    temp = pre[0]
    # index = -1
    # for i in range(len(mid)):
    #     if mid[i] == temp:
    #         index = i
    #         break
    # 找到pre头在中序中的位置，以此来分割成左右子树
    index = mid.index(temp)

    left = generate(pre[1:index+1], mid[:index])
    right = generate(pre[index+1:], mid[index+1:])
    return Node(temp, left, right)

def levelscan(root):
    queue = [root]
    while queue:
        cur = queue.pop(0)
        print(cur.data)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)



if __name__ == '__main__':
    pre = [1,2,4,7,3,5,6,8]
    mid = [4,7,2,1,5,3,8,6]
    root = generate(pre, mid)
    levelscan(root)
