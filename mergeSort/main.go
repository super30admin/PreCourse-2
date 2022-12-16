package main

import "fmt"

func main() {
	x := []int{9, 8, 7, 6, 5, 4, 3, 2, 1, 0}
	mergeSort(x)
	fmt.Println(x)
}

/*
time: o(nlogn)
space: o(n)
*/
func mergeSort(nums []int) {
	var dfs func(left, right int)
	dfs = func(left, right int) {
		// base
		if left >= right {
			return
		}

		// logic
		mid := left + (right-left)/2
		dfs(left, mid)
		dfs(mid+1, right)
		l := left
		r := mid + 1
		merged := []int{}
		for l <= mid && r <= right {
			if nums[l] < nums[r] {
				merged = append(merged, nums[l])
				l++
			} else {
				merged = append(merged, nums[r])
				r++
			}
		}
		for l <= mid {
			merged = append(merged, nums[l])
			l++
		}
		for r <= right {
			merged = append(merged, nums[r])
			r++
		}

		idxUsedToWriteInOrig := left
		for i := 0; i < len(merged); i++ {
			nums[idxUsedToWriteInOrig] = merged[i]
			idxUsedToWriteInOrig++
		}
	}
	dfs(0, len(nums)-1)

}
