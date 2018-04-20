def powerset(data, s, e):
	n = len(data); sum = 0
	for i in range(s, e+1):
		sum += combination(n, i)

def factorial(n):
	if(n == 1): return 1
	else: return n*factorial(n-1)

def combination(a, b):
	return factorial(a)*factorial(b)/factorial(a-b)