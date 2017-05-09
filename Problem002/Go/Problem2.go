package main

import ( 
	"fmt"
) 

func main(){
	var limit = 4000000
	fmt.Println(getFibonacciSum(limit))
}

func getFibonacciSum(limit int) int {
	if limit < 2 {
		return 0
	}

	var sum, prev, current int = 0, 0, 1

	for current < limit {
		var temp int  = current
		current = current + prev
		prev = temp

		if current % 2 ==0 {
			sum += current
		}

	}

	return sum

}