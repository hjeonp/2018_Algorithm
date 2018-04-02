N = int(input())
data = open("{}.txt".format(N), 'r')
data = data.readline()
data = [int(i) for i in data.split()]

def parr(array):
	for i in array:
		print('{:4d}'.format(i), end=" ")

def insertionsort(x):
	for i in range(1, len(x)):
		j = i - 1; key = x[i]
		while(x[j] > key and j>= 0):
			x[j+1] = x[j]
			j = j-1
		x[j+1] = key
		parr(x); print()

parr(data); print()
insertionsort(data)

parr(data); print()