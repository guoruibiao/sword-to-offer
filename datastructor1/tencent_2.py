# coding: utf8

# @Author: 郭 璞
# @File: tencent_2.py                                                                 
# @Time: 2017/4/3                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 腾讯笔试第二题，完美解决。类似于26进制的题型

# get the input content
def getInput():
    return input()

# slice the input str into a list which is the piece of 16
def slice(s):
    slices = []
    length = len(s)
    # get the times for looping
    times = int(length/16)
    for index in range(0, times):
        slices.append(s[index*16: index*16+16])
    return slices

  # make a dict as key-value to map the details
def initdict():
    dic = {
      'a': '61','b': '62','c': '63','d': '64','e': '65','f': '66','g': '67','h': '68','i': '69','j': '6a','k': '6b',
      'l': '6c','m': '6d','n': '6e','o': '6f','p': '70','q': '71','r': '72','s': '73','t': '74','u': '75','v': '76',
      'w': '77','x': '78','y': '79','z':'7a'
    }
    return dic

  # for printing the result
def myprint():
    slices = slice(getInput())
    levels = len(slices)
    dic = initdict()
    for levelnum in range(0, levels):
      if levelnum == 0:
          print ("0000000"+str(10*levelnum), "  ", "  ".join([dic[key] for key in slices[levelnum]]), "  ", slices[levelnum])
      else:
          print ("000000"+str(10*levelnum), "  ", "  ".join([dic[key] for key in slices[levelnum]]), "  ", slices[levelnum])
# run  # abcdefghijklmnopqrstuvwxyzabcdefghij
myprint()
