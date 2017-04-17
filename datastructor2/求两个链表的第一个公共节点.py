# coding: utf8

# @Author: 郭 璞
# @File: 求两个链表的第一个公共节点.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 求两个链表的第一个公共节点。暴力法O(mn)，所以空间换时间用栈特性，出栈的时候最后一个不等的节点就是公共节点了。
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

def sharedNode(chain1, chain2):
    s1 = []
    cursor = chain1.head
    while cursor:
        s1.append(cursor.data)
        cursor = cursor.next
    s2 = []
    cursor = chain2.head
    while cursor:
        s2.append(cursor.data)
        cursor = cursor.next
    # 出栈，找最后一个不相等的节点值
    while s1 and s2:
        temp1, temp2 = s1.pop(), s2.pop()
        if temp1 == temp2:
            target = temp1
        else:
            return target

def withoutStack(chian1, chian2):
    size1 = chian1.size()
    size2 = chian2.size()
    # 默认chian1更长
    first = chian1.head
    second = chian2.head
    index = 0
    while index<size1-size2:
        first = first.next
        index += 1
    # 现在开始找第一个相等的节点
    while first and second:
        if first.data == second.data:
            return first.data
        else:
            first = first.next
            second = second.next


if __name__ == '__main__':
    chian1 = Chian()
    chian1.addNode(1)
    chian1.addNode(3)
    chian1.addNode(5)
    chian1.addNode(7)
    chian1.addNode(9)
    chian2 = Chian()
    chian2.addNode(2)
    chian2.addNode(5)
    chian2.addNode(7)
    chian2.addNode(9)
    # 测试求解
    result = sharedNode(chian1, chian2)
    print(result)
    result = withoutStack(chian1, chian2)
    print(result)
