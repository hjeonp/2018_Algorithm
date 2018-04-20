#tmp = input()
#arr = [int(x) for x in tmp.split()]
arr = [2,3,4,5,6,7,8,9]
arr = [0] + arr

def Max_Heapify(arr, i):
	length = len(arr)
	if(i*2 > length - 1): return

	if(i*2+1 > length-1): k = i*2
	else: 
		if(arr[i*2] > arr[i*2+1]):  k = i*2
		else: k = i*2+1

	if arr[i] >= arr[k]: return
	arr[i], arr[k] = arr[k], arr[i]

	Max_Heapify(arr, k)

Max_Heapify(arr, 1)
print(arr)