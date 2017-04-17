# coding: utf8

# @Author: 郭 璞
# @File: find_oddnumber_in_array.py                                                                 
# @Time: 2017/4/13                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 以O(1)空间复杂度找到O(n)数组中出现奇数的那个数的下标

def find(array):
    """
    仅适用于数据连在一起的情况，如ls = [1,1,2,2,3,3,4,4,5,5,6,6,7,8,8,9,9]
    :param array:
    :return:
    """
    temp = array[0]
    index = 1
    while index<len(array)-1:
        if temp == array[index]:
            temp = array[index+1]
            index += 2
        else:
            return index-1


def common(array):
    """
    呵呵，仅仅是找到了那个数，mmp
    思路： 第一个数和第二个数异或运算，得到的结果再次参与到异或运算，最终得到的结果就是数组中仅仅出现一次的那个数。
    :param array:
    :return:
    """
    position = array[0]
    for index in range(1, len(array)):
        position ^= array[index]
    return position

##############################################################对于一个数组中两个仅出现一次的处理
def get_binary_expression(number):
    binarystr = []
    while number!= 0:
        shang = int(number /2 )
        yushu = number - shang*2
        binarystr.append(str(yushu))
        number = shang
    binarystr.reverse()
    return ''.join(binarystr)

def get_noone_position(s):
    # 先反序，为了找到下标
    s = [item for item in s]
    s.reverse()
    # print(s)
    s = ''.join(s)
    for index in range(len(s)):
        if int(s[index])==1:
            return index
        else:
            continue



def split(array):
    postfix = common(array)
    flag = get_noone_position(get_binary_expression(postfix))

    print(array)
    subarr1 = []
    subarr2 = []
    # 根据第position位置上是否为1来分割数组
    for item in array:
        tempflag = get_noone_position(get_binary_expression(item))
        # print(get_binary_expression(item))
        if tempflag == flag:
            subarr1.append(item)
        else:
            subarr2.append(item)
    print(subarr1)
    print(subarr2)

    num1 = common(subarr1)
    num2 = common(subarr2)
    return num1, num2



if __name__ == '__main__':
    ls = [1,1,2,2,3,3,4,4,5,5,6,6,7,8,8,9,9]
    position = find(ls)
    print("{} 出现的下标位置为：{}".format(ls[position], position))

    array = [1,2,3,4,5,6,7,8,7,6,5,4,3,2,1]
    result = common(array)
    print(result)

    # result = get_binary_expression(7)
    # print(result)
    # print(get_noone_position(result))

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 6, 5, 4, 3, 2, 1]
    num1, num2 = split(array)
    print("Num1: {}, Num2: {}".format(num1, num2))
