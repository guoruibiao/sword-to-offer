# coding: utf8

def sort(ls, left, right):
	pivot = ls[left]
	while left < right:
		while left < right and ls[right] >= pivot:
			right -= 1
		ls[left] = ls[right]
		while  left < right and ls[left] <= pivot:
			left += 1
		ls[right] = ls[left]
	ls[left] = pivot
	return left

def quicksort(ls,left, right):
	if left < right :
		pivot = sort(ls, left, right)
		quicksort(ls, left, pivot-1)
		quicksort(ls, pivot+1, right)

def beautify_version(ls):
	if ls == []:
		return []
	else:
		temp = ls[0]
		left = beautify_version([x for x in ls[1:] if x < ls[0]])
		right = beautify_version([x for x in ls[1:] if x >= ls[0]])
		return left + [temp] + right


def qiucksortinoneline(ls):
	"""
    一行代码实现的快速排序算法
	"""
	return [] if ls == [] else qiucksortinoneline([x for x in ls[1:] if x < ls[0]]) + [ls[0]] + qiucksortinoneline([x for x in ls[1:] if x >= ls[0]])


def quick(ls):
	return [] if ls == [] else quick([x for x in ls[1:] if x < ls[0]]) + [ls[0]]+quick([x for x in ls[1:] if x>=ls[0]])

if __name__ == '__main__':
	ls = [3,5,7,9,1,4,6,2,8]
	print('排序前： ', ls)
	# quicksort(ls, 0, len(ls)-1)
	# ls = qiucksortinoneline(ls)
	# qiucksortinoneline(ls)
	# ls = beautify_version(ls)
	ls = quick(ls)
	print('排序后： ', ls)
