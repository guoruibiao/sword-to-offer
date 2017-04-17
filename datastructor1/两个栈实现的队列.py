# coding: utf8

# @Author: 郭 璞
# @File: 两个栈实现的队列.py                                                                 
# @Time: 2017/4/15                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 使用两个栈构造一个队列

class Queue(object):
    """
    两个栈实现一个先进先出的队列
    """
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, data):
        """
        入队列实现, 如果栈2中元素不为空，则把栈2中元素倒腾到栈1中，对栈1进行添加操作
        :param data:
        :return:
        """
        while self.s2:
            self.s1.append(self.s2.pop())
        self.s1.append(data)


    def dequeue(self):
        """
        出队列实现，如果栈1不为空，则把栈1中元素全部倒腾到栈2中，对栈2进行弹出操作
        :return:
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        try:
            return self.s2.pop()
        except:
            print('队列空咯！')

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(7)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())