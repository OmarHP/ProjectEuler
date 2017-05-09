
def getFibonacciSum(limit):
	if (limit < 2):
		return 0
	sum, prev, current = 0, 0, 1 
	while(current < limit):
		temp = current
		current = prev + current
		prev = temp
		if(current%2 == 0):
			sum += current
	return sum

def main():
	print(getFibonacciSum(4000000))

if __name__ == "__main__":
	main()