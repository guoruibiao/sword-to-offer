# coding: utf8

# @Author: 郭 璞
# @File: 包含min函数得栈.py                                                                 
# @Time: 2017/4/16                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 一个栈，实现min函数，并且min，pop，push操作的时间复杂度都得为O(1)。

class Stack(object):
    """
    定义一个辅助栈，每次push数据的时候在辅助栈中只是添加最小的元素。
    """
    def __init__(self):
        self.main = []
        self.helper = []

    def push(self, data):
        if self.main ==[]:
            self.main.append(data)
            self.helper.append(data)
        else:
            temp = self.main[-1]
            if temp <= data:
                self.helper.append(temp)
            else:
                self.helper.append(data)
            self.main.append(data)

    def pop(self):
        if self.main == []:
            print('栈空了，再也弹不出数据了呢！')
        else:
            self.helper.pop(len(self.helper)-1)
            return self.main.pop(len(self.main)-1)

    def min(self):
        """
        求得目前栈中的最小元素的值。
        :return:
        """
        return self.helper[-1]


if __name__ == '__main__':
    # 对入栈出栈进行测试！
    stack = Stack()
    stack.push(3)
    stack.push(5)
    stack.push(7)
    stack.push(1)
    print(stack.main)
    print(stack.helper)
    print(stack.pop())
    print(stack.main)
    print(stack.helper)
    print(stack.pop())
    print(stack.main)
    print(stack.helper)
    print(stack.pop())
    print(stack.main)
    print(stack.helper)
    print(stack.pop())
    print(stack.main)
    print(stack.helper)
