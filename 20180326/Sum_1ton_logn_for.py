def sum1ton(input_data):
	N = input_data
	mul = 1
	ans = 0

	while(N):
		temp = 0
		if(N%2 == 1):
			temp += N

		temp += (N//2)*(N//2)
		ans += temp * mul

		N //= 2
		mul *= 2

	return ans

input_data = int(input())
print(sum1ton(input_data))