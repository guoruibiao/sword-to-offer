# coding: utf8
# @Description: 别人实现的可打印编码的霍夫曼树

import struct

codeDict = {}  # 全局字典key=字符，value=数字
encodeDict = {}
filename = None
listForEveryByte = []


class Node:
    def __init__(self, right=None, left=None, parent=None, weight=0, charcode=None):
        self.right = right
        self.left = left
        self.parent = parent
        self.weight = weight
        self.charcode = charcode


# 按权值排序
def sort(list):
    return sorted(list, key=lambda node: node.weight)


# 构建哈夫曼树
def Huffman(listOfNode):
    listOfNode = sort(listOfNode)
    while len(listOfNode) != 1:
        a, b = listOfNode[0], listOfNode[1]
        new = Node()
        new.weight, new.left, new.right = a.weight + b.weight, a, b
        a.parent, b.parent = new, new
        listOfNode.remove(a), listOfNode.remove(b)
        listOfNode.append(new)
        listOfNode = sort(listOfNode)
    return listOfNode


def inPutFile():
    global filename
    global listForEveryByte
    filename = input("请输入要压缩的文件：")
    global codeDict
    with open(filename, 'rb') as f:
        data = f.read()
        for Byte in data:
            codeDict.setdefault(Byte, 0)  # 每个字节出现的次数默认为0
            codeDict[Byte] += 1
            listForEveryByte.append(Byte)


def outputCompressedFile():
    global listForEveryByte
    fileString = ""
    with open(filename.split(".")[0] + ".jbj", "wb") as f:
        for Byte in listForEveryByte:
            fileString += encodeDict[Byte]  # 构成一个长字符序列
        leng = len(fileString)
        more = 16 - leng % 16
        fileString = fileString + "0" * more  # 空位用0补齐
        # print(fileString)

        leng = len(fileString)
        i, j = 0, 16
        while j <= leng:
            k = fileString[i:j]
            a = int(k, 2)
            # print(a)
            # print(repr(struct.pack(">H",a)))
            f.write(struct.pack(">H", a))
            # f.write(str(a))
            i = i + 16
            j = j + 16


def encode(head, listOfNode):
    global encodeDict
    for e in listOfNode:
        ep = e
        encodeDict.setdefault(e.charcode, "")
        while ep != head:

            if ep.parent.left == ep:
                encodeDict[e.charcode] = "1" + encodeDict[e.charcode]
            else:
                encodeDict[e.charcode] = "0" + encodeDict[e.charcode]
            ep = ep.parent


if __name__ == '__main__':
    inPutFile()
    listOfNode = []
    for e in codeDict.keys():
        listOfNode.append(Node(weight=codeDict[e], charcode=e))
    head = Huffman(listOfNode)[0]  # 构建哈夫曼树，head称为树的根节点
    encode(head, listOfNode)

    for i in encodeDict.keys():
        print(i, encodeDict[i])
        # outputCompressedFile()