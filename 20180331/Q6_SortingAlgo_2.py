data = input()
data = [int(i) for i in data.split()]

def parr(array):
	for i in array:
		print('{:4d}'.format(i), end="")

def selectionsort(x):
	for i in range(len(x)-1):
		minn = i 
		for j in range(i+1, len(x)):
			if x[minn] >= x[j]:
				minn = j
		x[i], x[minn] = x[minn], x[i]
		parr(x); print()

selectionsort(data)
parr(data); print()
