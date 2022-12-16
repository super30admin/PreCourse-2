package main

import "fmt"

func main() {
	fmt.Println(search([]int{1, 2, 3, 4, 5, 6, 7}, 7))
	fmt.Println(search([]int{1, 2, 3, 4, 5, 6, 7}, 1))
	fmt.Println(search([]int{1, 2, 3, 4, 5, 6, 7}, 3))
	fmt.Println(search([]int{1, 2, 3, 4, 5, 6, 7}, 0))
}

// time: o(logn)
// space: o(1)
func search(nums []int, x int) int {
	left := 0
	right := len(nums) - 1
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] == x {
			return mid
		} else if nums[mid] > x {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return -1
}
