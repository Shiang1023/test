def func(n):
	if n==0:
		return 1
	else:
		return n*func(n-1)
number = 5
result = func(number)
print(f"The func of {number} is {result}.")
