package main

import ( 
	"fmt"
) 

func main(){
	 var limit = 1000
	fmt.Printf("The sum of all the multiples of 3 or 5 below %d is: %d\n",limit,(geometricSolution(limit)))
}

func geometricSolution(limit int) int {
	//Substract the numbers that are divisible by 3 and 5 in order to avoid being counted twice
	return sumDivisibleBy(3,limit-1)+sumDivisibleBy(5,limit-1)-sumDivisibleBy(15,limit-1)
}

func sumDivisibleBy(m, greatest int) int {
	var n int = greatest/m
	return m * ( n * ( n + 1 ) / 2 )
}
