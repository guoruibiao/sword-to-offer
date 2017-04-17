# coding: utf8

# @Author: 郭 璞
# @File: 合并两个有序链表.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 合并两个有序的链表。
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Chian(object):
    def __init__(self):
        self.head = None

    def addNode(self, data):
        if self.head is None:
            self.head = Node(data=data, next=None)
        else:
            cursor = self.head
            while cursor.next:
                cursor = cursor.next
            temp = Node(data=data, next=None)
            cursor.next = temp

    def printself(self):
        if self.head:
            cursor = self.head
            while cursor:
                print(cursor.data, end='\t')
                cursor = cursor.next
            print()

    def size(self):
        count = 0
        if self.head is None:
            return count
        else:
            cursor = self.head
            while cursor:
                cursor = cursor.next
                count += 1
            return count


def merge(chain1, chain2):
    """
    合并两个有序的单链表
    :param chain1:
    :param chain2:
    :return:
    """
    first = chain1.head
    second = chain2.head
    chain = Chian()
    while first and second:
        if first.data == second.data:
            chain.addNode(first.data)
            first = first.next
        if first.data < second.data:
            chain.addNode(first.data)
            first = first.next
        else:
            chain.addNode(second.data)
            second = second.next
    while first is not None:
        chain.addNode(first.data)
        first = first.next
    while second is not None:
        chain.addNode(second.data)
        second = second.next
    return chain


def printchain(head):
    if head is None:
        return
    else:
        cursor = head
        while cursor:
            print(cursor.data, end='\t')
            cursor = cursor.next
        print()

if __name__ == '__main__':
    chain1 = Chian()
    chain1.addNode(1)
    chain1.addNode(3)
    chain1.addNode(5)
    chain1.addNode(7)
    chain1.addNode(9)
    chain1.addNode(17)
    chain1.addNode(18)
    chain1.addNode(19)
    chain2 = Chian()
    chain2.addNode(1)
    chain2.addNode(5)
    chain2.addNode(6)
    chain2.addNode(8)
    chain2.addNode(10)
    chain1.printself()
    chain2.printself()
    print('开始合并！')
    chain = merge(chain1, chain2)
    chain.printself()
