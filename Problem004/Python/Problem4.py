import math

def getLargestPalindrome(numDigits):
	maxNumber = 10 ** numDigits - 1
	minNumber = 10 ** (numDigits - 1)
	maxPalindrome=0
	for i in range(maxNumber, minNumber-1, -1):
		for j in range(i, minNumber-1, -1):
			product = i * j
			if product < maxPalindrome:
				break
			if isPalindrome(product) and product > maxPalindrome:
				maxPalindrome= product

	return maxPalindrome

def isPalindrome(product):
	s = str(product)
	return s[::-1]==s

def main():
	print(getLargestPalindrome(3))


if __name__ == "__main__":
	main()