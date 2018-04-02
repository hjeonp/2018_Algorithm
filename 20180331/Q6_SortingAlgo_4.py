data = input()
data = [int(i) for i in data.split()]

def parr(array):
	for i in array:
		print('{:4d}'.format(i), end="")

def bin(x, target, start, end):
	if start > end: return start

	mid = (start+end) // 2
	if(x[mid] < target):
		return bin(x, target, mid+1, end)
	elif(x[mid] > target):
		return bin(x, target, start, mid-1)
	else: return m 

def insertionsort(target, x):
	if target > len(x) - 1: return

	p = bin(x[0:target], x[target], 0, target-1)
	print("Insertion point: {}".format(p))

	tmp = x[target]
	for i in range(target, p, -1):
		x[i] = x[i-1]
	x[p] = tmp

	parr(x); print()
	insertionsort(target+1, x)

insertionsort(1, data)
