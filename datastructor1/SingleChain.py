# coding: utf8

# @Author: 郭 璞
# @File: SingleChain.py                                                                 
# @Time: 2017/4/5                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 单链表实现

class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LianBiao(object):

    def __init__(self):
        self.root = None

    # 给单链表添加元素节点
    def addNode(self, data):
        if self.root==None:
            self.root = Node(data=data, next=None)
            return self.root
        else:
            # 有头结点，则需要遍历到尾部节点，进行链表增加操作
            cursor = self.root
            while cursor.next!= None:
                cursor = cursor.next
            cursor.next = Node(data=data, next=None)
            return self.root

    # 在链表的尾部添加新节点，底层调用addNode方法即可
    def append(self, value):
        self.addNode(data=value)

    # 在链表首部添加节点
    def prepend(self, value):
        if self.root == None:
            self.root = Node(value, None)
        else:
            newroot = Node(value, None)
            # 更新root索引
            newroot.next = self.root
            self.root = newroot

    # 在链表的指定位置添加节点
    def insert(self, index, value):
        if self.root == None:
            return
        if index<=0 or index >self.size():
            print('index %d 非法， 应该审视一下您的插入节点在整个链表的位置！')
            return
        elif index==1:
            # 如果index==1， 则在链表首部添加即可
            self.prepend(value)
        elif index == self.size()+1:
            # 如果index正好比当前链表长度大一，则添加在尾部即可
            self.append(value)
        else:
            # 如此，在链表中部添加新节点，直接进行添加即可。需要使用计数器来维护插入未知
            counter = 2
            pre = self.root
            cursor = self.root.next
            while cursor!=None:
                if counter == index:
                    temp = Node(value, None)
                    pre.next = temp
                    temp.next = cursor
                    break
                else:
                    counter += 1
                    pre = cursor
                    cursor = cursor.next

    # 删除指定位置上的节点
    def delNode(self, index):
        if self.root == None:
            return
        if index<=0 or index > self.size():
            return
        # 对第一个位置需要小心处理
        if index == 1:
            self.root = self.root.next
        else:
            pre = self.root
            cursor = pre.next
            counter = 2
            while cursor!= None:
                if index == counter:
                    print('can be here!')
                    pre.next = cursor.next
                    break
                else:
                    pre = cursor
                    cursor = cursor.next
                    counter += 1

    # 删除值为value的链表节点元素
    def delValue(self, value):
        if self.root == None:
            return
        # 对第一个位置需要小心处理
        if self.root.data == value:
            self.root = self.root.next
        else:
            pre = self.root
            cursor = pre.next
            while cursor!=None:
                if cursor.data == value:
                    pre.next = cursor.next
                    # 千万记得更新这个节点，否则会出现死循环。。。
                    cursor = cursor.next
                    continue
                else:
                    pre = cursor
                    cursor = cursor.next

    # 判断链表是否为空
    def isempty(self):
        if self.root == None or self.size()==0:
            return True
        else:
            return False

    # 删除链表及其内部所有元素
    def truncate(self):
        if self.root == None or self.size()==0:
            return
        else:
            cursor = self.root
            while cursor!= None:
                cursor.data = None
                cursor = cursor.next
            self.root = None
            cursor = None

    # 获取指定位置的节点的值
    def getvalue(self, index):
        if self.root is None or self.size()==0:
            print('当前链表为空！')
            return None
        if index<=0 or index>self.size():
            print("index %d不合法！"%index)
            return None
        else:
            counter = 1
            cursor = self.root
            while cursor is not None:
                if index == counter:
                    return cursor.data
                else:
                    counter += 1
                    cursor = cursor.next

    # 获取链表尾部的值，且不删除该尾部节点
    def peek(self):
        return self.getvalue(self.size())

    # 获取链表尾部节点的值，并删除该尾部节点
    def pop(self):
        if self.root is None or self.size()==0:
            print('当前链表已经为空！')
            return None
        elif self.size()==1:
            top = self.root.data
            self.root = None
            return top
        else:
            pre = self.root
            cursor = pre.next
            while cursor.next is not None:
                pre = cursor
                cursor = cursor.next
            top = cursor.data
            cursor = None
            pre.next = None
            return top

    # 单链表逆序实现
    def reverse(self):
        if self.root is None:
            return
        if self.size()==1:
            return
        else:
            # post = None
            pre = None
            cursor = self.root
            while cursor is not None:
                # print('逆序操作逆序操作')
                post = cursor.next
                cursor.next = pre
                pre = cursor
                cursor = post
            # 千万不要忘记了把逆序后的头结点赋值给root，否则无法正确显示
            self.root = pre

    # 删除链表中的重复元素
    def delDuplecate(self):
        # 使用一个map来存放即可，类似于变形的“桶排序”
        dic = {}
        if self.root == None:
            return
        if self.size() == 1:
            return
        pre = self.root
        cursor = pre.next
        dic = {}
        # 为字典赋值
        temp = self.root
        while temp!=None:
            dic[str(temp.data)] = 0
            temp = temp.next
        temp = None
        # 开始实施删除重复元素的操作
        while cursor!=None:
            if dic[str(cursor.data)] == 1:
                pre.next = cursor.next
                cursor = cursor.next
            else:
                dic[str(cursor.data)] += 1
                pre = cursor
                cursor = cursor.next


    # 修改指定位置节点的值
    def updateNode(self, index, value):
        if self.root == None:
            return
        if index<0 or index>self.size():
            return
        if index == 1:
            self.root.data = value
            return
        else:
            cursor = self.root.next
            counter = 2
            while cursor!=None:
                if counter == index:
                    cursor.data = value
                    break
                cursor = cursor.next
                counter += 1


    # 获取单链表的大小
    def size(self):
        counter = 0
        if self.root == None:
            return counter
        else:
            cursor = self.root
            while cursor!=None:
                counter +=1
                cursor = cursor.next
            return counter


    # 打印链表自身元素
    def print(self):
        if(self.root==None):
            return
        else:
            cursor = self.root
            while cursor!=None:
                print(cursor.data, end='\t')
                cursor = cursor.next
            print()


if __name__ == '__main__':
    # 创建一个链表对象
    lianbiao = LianBiao()
    # 判断当前链表是否为空
    print("链表为空%d"%lianbiao.isempty())
    # 判断当前链表是否为空
    lianbiao.addNode(1)
    print("链表为空%d"%lianbiao.isempty())
    # 添加一些节点，方便操作
    lianbiao.addNode(2)
    lianbiao.addNode(3)
    lianbiao.addNode(4)
    lianbiao.addNode(6)
    lianbiao.addNode(5)
    lianbiao.addNode(6)
    lianbiao.addNode(7)
    lianbiao.addNode(3)
    # 打印当前链表所有值
    print('打印当前链表所有值')
    lianbiao.print()
    # 测试对链表求size的操作
    print("链表的size: "+str(lianbiao.size()))
    # 测试指定位置节点值的获取
    print('测试指定位置节点值的获取')
    print(lianbiao.getvalue(1))
    print(lianbiao.getvalue(lianbiao.size()))
    print(lianbiao.getvalue(7))
    # 测试删除链表中指定值， 可重复性删除
    print('测试删除链表中指定值， 可重复性删除')
    lianbiao.delNode(4)
    lianbiao.print()
    lianbiao.delValue(3)
    lianbiao.print()
    # 去除链表中的重复元素
    print('去除链表中的重复元素')
    lianbiao.delDuplecate()
    lianbiao.print()
    # 指定位置的链表元素的更新测试
    print('指定位置的链表元素的更新测试')
    lianbiao.updateNode(6, 99)
    lianbiao.print()
    # 测试在链表首部添加节点
    print('测试在链表首部添加节点')
    lianbiao.prepend(77)
    lianbiao.prepend(108)
    lianbiao.print()
    # 测试在链表尾部添加节点
    print('测试在链表尾部添加节点')
    lianbiao.append(99)
    lianbiao.append(100)
    lianbiao.print()
    # 测试指定下标的插入操作
    print('测试指定下标的插入操作')
    lianbiao.insert(1, 10010)
    lianbiao.insert(3, 333)
    lianbiao.insert(lianbiao.size(), 99999)
    lianbiao.print()
    # 测试peek 操作
    print('测试peek 操作')
    print(lianbiao.peek())
    lianbiao.print()
    # 测试pop 操作
    print('测试pop 操作')
    print(lianbiao.pop())
    lianbiao.print()
    # 测试单链表的逆序输出
    print('测试单链表的逆序输出')
    lianbiao.reverse()
    lianbiao.print()
    # 测试链表的truncate操作
    print('测试链表的truncate操作')
    lianbiao.truncate()
    lianbiao.print()
