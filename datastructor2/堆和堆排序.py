# coding: utf8

# @Author: 郭 璞
# @File: 堆和堆排序.py                                                                 
# @Time: 2017/4/18                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 堆和堆排序实现。

class MaxHeap(object):
    """
    创建一个大顶堆。用数组（列表）作为存储容器来存储数据。
    """
    def __init__(self, size):
        self.heap = []
        # 先对容器进行初始化
        for index in range(size):
            self.heap.append(0)
        self.MAXSIZE = size
        self.currsize = 0

    def insert(self, data):
        """
        插入元素的时候，先放到这个“完全二叉树”的末尾位置。然后让它和其父节点进行大小比较：
            如果父节点大， 那么说明这个插入值放到这个位置是合理的；
            如果当前节点的值更大，说明需要和父节点交换位置，然后进行新一轮的比较。
            直到比较到了根节点，（根节点没有父节点了，此时循环比较的过程就可以结束了）。
        当然了，如果当前堆还没有数据，那么直接把这个数据放到根节点的位置即可。
        :param data:
        :return:
        """
        if self.currsize == self.MAXSIZE:
            print('插入失败，堆空间已满！')
            return False
        else:
            self.currsize += 1
            flag = self.currsize -1
            while flag > 0:
                parent = int((flag-1)/2)
                if self.heap[parent] > data :
                    self.heap[flag] = data
                    return True
                else:
                    self.heap[flag] = self.heap[parent]
                    flag = parent
            # 如果循环条件没满足，说明现在堆是空的，直接在根节点上赋值即可。
            self.heap[0] = data
            return True

    def siftdown(self, flag):
        """
        给定一个位置，对堆的结构进行调整。
        :param flag:
        :return:
        """
        want = flag
        x = self.heap[flag]

        while want < self.currsize:
            lchild = 2*want +1
            rchild = 2*want +2
            if lchild > self.currsize:
                # 没有孩子节点，直接放即可
                self.heap[want] = x
            else:
                # 有左右孩子节点, 找到待换位置
                if lchild < self.currsize:
                    maxchildposition = lchild if self.heap[lchild] > self.heap[rchild] else rchild
                else:
                    # 至少可以有左孩子
                    maxchildposition = lchild
                # 开始调换数据
                if self.heap[maxchildposition] < x:
                    self.heap[want] = x
                    return
                else:
                    self.heap[want] = self.heap[maxchildposition]
                    want = maxchildposition

    def deletetop(self):
        if self.currsize < 0:
            print('堆空，无法再进行数据删除了！')
            return
        else:
            target = self.heap[0]
            substitute = self.heap[self.currsize-1]
            self.currsize -= 1
            self.heap[0] = substitute
            self.siftdown(0)
            return target

if __name__ == '__main__':
    maxheap = MaxHeap(7)
    for index in range(1, 8):
        maxheap.insert(index)
    # 测试弹出数据
    for index in range(1, 8):
        print(maxheap.deletetop())
