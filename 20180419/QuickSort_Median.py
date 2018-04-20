def Quick_Sort(arr, p, r):
	global partition_num

	q = (p+r) // 2; pv = r - 1

	if arr[p] > arr[q]: arr[p], arr[q] = arr[q], arr[p]
	if arr[q] > arr[r]: arr[q], arr[r] = arr[r], arr[q]
	if arr[p] > arr[q]: arr[p], arr[q] = arr[q], arr[p]

	if r-p+1 > 3: 
		arr[q], arr[pv] = arr[pv], arr[q]
		partition_num += 1; q = Partition(arr, p, r);
		Quick_Sort(arr, p, q-1)
		Quick_Sort(arr, q+1, r)

def Partition(arr, p, r):
	q = (p+r) // 2; i = p; j = p+1; pv = r-1;
	while j < pv:
		if arr[j] <= arr[pv]:
			i += 1; arr[i], arr[j] = arr[j], arr[i]
		j += 1

	arr[i+1], arr[pv] = arr[pv], arr[i+1]
	return i+1

partition_num = 0

n = int(input())
f = open('{}.txt'.format(n), 'r')
array = [int(x) for x in f.readline().split()]

Quick_Sort(array, 0, len(array)-1)

print("num of partition:  {}".format(partition_num))
print(array)
