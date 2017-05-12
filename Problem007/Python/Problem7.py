def getNthPrime(n):
	if n == 1 :
		return 2

	primes = []
	primes.append(2)

	number=3
	while len(primes) < n:
		j = 0
		isPrime = True
		while(primes[j] * primes [j] <= number ):
			if( number % primes[j]  == 0):
				isPrime = False
				break
			else:
				j += 1

		if isPrime :
			primes.append(number)

		number += 2

	#print (primes)
	return primes[n-1]

def main():
	print( getNthPrime(10001))

if __name__ == '__main__':
	main()