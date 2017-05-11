def generatePrimes(upperLimit):
	primes = []

	# the unique even prime number
	primes.append(2)

	#check for all numbers from 3 to upper limit
	for i in range(3, upperLimit+1, +2):
		j = 0
		#if i is not divisible by any prime factor less or equals than its squared root it is a prime number
		#We assume it is a prime number
		isPrime = True
		#until reaching the square root of the number 
		while (primes[j] * primes [j] <= i):
			#check if i is divisible by j-th previously found prime factor
			if (i % primes [j] == 0):
				isPrime=False
				break
			#if i was not divisible, check fot the next previously found prime factor 
			j += 1

		# if i was not divisible for any previously found prime factor, add tho the prime factor list
		if isPrime == True:
			primes.append(i)

	return primes

#def main():
#	print(generatePrimes(20))

#if __name__ == "__main__":
#	main()