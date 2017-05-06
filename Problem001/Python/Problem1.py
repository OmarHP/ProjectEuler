def bruteForceSolution(limit):
	sum = 0
	for i in range(limit):
		if i%3==0 or i%5==0:
			sum+=i
	return sum

def geometricSolution(limit):

	#Substract the numbers that are divisible by 3 and 5 in order to avoid being counted twice
	return sumDivisibleBy(3, limit-1)+sumDivisibleBy(5, limit-1)-sumDivisibleBy(15, limit-1)

def sumDivisibleBy(m, greatest):
	n = greatest // m
	return m * ( n * ( n + 1 ) / 2)

def main():
	limit = 1000
	print("The sum of all the multiples of 3 or 5 below " + str(limit) +" is: "+str(geometricSolution(limit)))

if __name__ == "__main__":
	main()
