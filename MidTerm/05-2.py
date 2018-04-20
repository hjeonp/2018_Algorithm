def InsertionSort(arr):
	if(len(arr) == 0): return

	min = 0

	for i in range(1, len(arr)):
		if(arr[i] < arr[min]):
			min = i
		arr[0], arr[min] = arr[min], arr[0]
	InsertionSort(arr[1:])

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
InsertionSort(arr)
print(arr)