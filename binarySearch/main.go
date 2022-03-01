package main

import (
	"fmt"
)

// time: o(logN)-- since we cut the search size by half each iteration
// space: o(1)
func binarySearch(nums []int, lookup int) int {
	if len(nums) == 0 {
		return -1
	}
	left := 0
	right := len(nums) - 1

	for left <= right {
		mid := left + ((right - left) / 2)
		if nums[mid] == lookup {
			return mid
		} else if lookup > nums[mid] {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return -1
}

func main() {
	result := binarySearch([]int{2, 3, 4, 10, 40}, 10)
	if result != -1 {
		fmt.Println("Element is present at index: ", result)
	} else {
		fmt.Println("Element is not present in array")
	}
}
