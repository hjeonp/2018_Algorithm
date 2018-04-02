def Insertion_Sort_Recursive(arr, p, q):
	if(p==q): return
	Insertion_Sort_Recursive(arr, p, q-1)
	last = arr[q-1]
	j = q-2
	while(j>=0 and arr[j] > last):
		arr[j+1] = arr[j]
		j = j-1
	arr[j+1] = last

array = [3, 6, 1, 7, 8, 2, 5, 4, 0, 9]
Insertion_Sort_Recursive(array, 0, len(array)-1)
print(array)