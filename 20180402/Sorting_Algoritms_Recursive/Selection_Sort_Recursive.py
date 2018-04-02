def Selection_Sort_Recursive(arr, p, q):
	if(p==q): return
	max = p
	for i in range(p+1,  q+1):
		if arr[max] < arr[i]: max = i
	arr[q], arr[max] = arr[max], arr[q]
	Selection_Sort_Recursive(arr, p, q-1)

array = [3, 6, 1, 7, 8, 2, 5, 4, 0, 9]
Selection_Sort_Recursive(array, 0, len(array)-1)
print(array)