def compute():
	stack = []
	alpha = 10
	beta = 5
	for i in range(beta):
		for j in range(alpha):
			if (j == i+1 or j == i+2):
				stack.append(j)
		print("Before Pop: ", stack)
		stack.pop()
		print("After Pop: ", stack)
	return stack
if (__name__ == "__main__"):
	stack = compute() 
	print(stack)
