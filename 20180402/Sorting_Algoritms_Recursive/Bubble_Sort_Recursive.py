def Bubble_Sort_Recursive(arr, p, q):
	if(p==q): return
	for i in range(p, q):
		if arr[i] > arr[i+1]: 
			arr[i], arr[i+1] = arr[i+1], arr[i]
	Bubble_Sort_Recursive(arr, p, q-1)

array = [3, 6, 1, 7, 8, 2, 5, 4, 0, 9]
Bubble_Sort_Recursive(array, 0, len(array)-1)
print(array)
