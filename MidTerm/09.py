def B(str, n):
	if(n == len(str)): return
	else:
		print(str[len(str)-n-1], end='')
		B(str, n+1)

B('abcde', 0)