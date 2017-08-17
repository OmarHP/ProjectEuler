import math

def getLargestPrimeFactor(n):

	lastFactor = 1
	factor = 2

	while (n % factor == 0):
		n = n // factor
		lastFactor = factor

	factor = 3
	maxFactor = int( math.sqrt( n ) )
	while ( n > 1 and factor <= maxFactor ):
		if(n % factor == 0):
			n = n // factor
			lastFactor = factor
			while ( n % factor == 0 ):
				n = n // factor
			maxFactor = int( math.sqrt( n ) )
		factor += 2
	if n > 1:
		return n

	return lastFactor

def main():
	print(getLargestPrimeFactor(600851475143))
	#print(getLargestPrimeFactor(13195))
	#print(getLargestPrimeFactor(13195))
	#print(getLargestPrimeFactor(22))

if __name__ == "__main__":
	main()