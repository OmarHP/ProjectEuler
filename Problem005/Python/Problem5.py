
from GeneratePrimes import generatePrimes
import math

def getSmallestEvenlyDivisible(upperLimit):
	primes=generatePrimes(upperLimit)
	product = 1
	#for each posible factor 
	for factor in primes:
		#calculate the max exponent for factor takent into accout the upper limit
		exp = int( math.log(upperLimit) / math.log(factor) )
		product *= math.pow(factor, exp)
	return product


def main():
	print (getSmallestEvenlyDivisible(20))


if __name__ == '__main__':
	main()