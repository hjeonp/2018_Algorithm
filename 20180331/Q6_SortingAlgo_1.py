data = input()
data = [int(i) for i in data.split()]

def parr(array):
	for i in array:
		print('{:4d}'.format(i), end="")

def bubbleSort(x):
        length = len(x)-1
        for i in range(length):
            for j in range(length-i):
                if x[j] > x[j+1]:
                    x[j], x[j+1] = x[j+1], x[j]
            parr(x); print()

bubbleSort(data)
