# coding: utf8

# @Author: 郭 璞
# @File: 两个队列实现一个栈.py                                                                 
# @Time: 2017/4/15                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 两个队列实现一个栈

class Stack(object):

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def pop(self):
        """
        出栈实现： 如果队列1中元素个数不为零，把队列1中的元素依次添加到队列2中，然后对于队列2从左至右往外取出数据即可。
        :return:
        """
        while self.q1:
            self.q2.append(self.q1.pop(0))
        try:
            return self.q2.pop()
        except:
            print("栈空咯！")

    def push(self, data):
        """
        入栈实现：如果队列2不为空，先把队列2中的元素从左至右依次添加到队列1的右边，然后再放入新的元素。
        :param data:
        :return:
        """
        while self.q2:
            self.q1.append(self.q2.pop(0))
        self.q1.append(data)

if __name__ == '__main__':
    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

