# coding: utf8

# @Author: 郭 璞
# @File: 链表中倒数第K个数.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 求出单链表中的倒数第K个节点的元素的值

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
                print(cursor.data)
                cursor = cursor.next

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

    def indexOfReverseK(self, k):
        """
        咱们默认负数没有意义，虽然对于负数的情况可以使用正序链表来解决。
        :param k:
        :return:
        """
        if self.head is None:
            return
        if self.head and k <= 0:
            # 因为倒数第0个元素没有意义，所以直接返回即可。
            return None
        if self.size() < k:
            print('链表没那么长，老哥！')
            return

        if self.size() == k:
            return self.head.data
        else:
            # 有两个思路一个是双指针方式，另一个采用逆序链表再正序查找第k个元素，接下来分别实现之。
            # return self.doublepointer(k)
            return self.reverseway(k)

    def doublepointer(self, k):
        first, second = self.head, self.head
        for index in range(k):
            first = first.next
        while first:
            first = first.next
            second = second.next
        return second.data


    def reverse(self):
        if self.head is None:
            return
        if self.size() == 1:
            return self.head
        else:
            cursor = self.head
            pre = None
            post = None
            while cursor:
                post = cursor.next
                cursor.next = pre
                pre = cursor
                cursor = post
        self.head = pre


    def reverseway(self, k):
        # 先把原来的链表逆序，然后正序查找到第K个元素，最后别忘了将链表逆序回来。
        self.reverse()
        counter = 1
        cursor = self.head
        result = None
        while cursor:
            if counter == k:
                result = cursor.data
                break
            counter += 1
            cursor = cursor.next
        self.reverse()
        return result





if __name__ == '__main__':
    chain = Chian()
    chain.addNode(0)
    chain.addNode(1)
    chain.addNode(2)
    chain.addNode(3)
    chain.printself()
    # chain.reverse()
    # chain.printself()
    print("链表的大小：", chain.size())
    thek = chain.indexOfReverseK(4)
    print("倒数第K个元素的值为：", thek)
    doublepointerwayk = chain.indexOfReverseK(0)
    print("采用双指针的形式实现的倒数第K个元素的值为：", doublepointerwayk)
    reversewayk = chain.indexOfReverseK(3)
    print("采用逆序算法实现的倒数第K个元素的值为： ", reversewayk)
