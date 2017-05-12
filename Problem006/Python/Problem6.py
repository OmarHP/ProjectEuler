import math

def sumFirstNNumbers(n):
	return n * (n + 1) / 2

def sumSquaresOfFirstNNumbers(n):
	return n * (2 * n + 1) * (n + 1) / 6

def main():
	print( math.pow(sumFirstNNumbers(100), 2) - sumSquaresOfFirstNNumbers(100))

if __name__ == '__main__':
	main()