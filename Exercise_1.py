"""
	Problem Statement: Implement Iterative Binary Search

	Time Complexity: 
	binarySearch(): O(log n)

	Space Complexity:
	binarySearch(): O(1)

"""
from typing import List

def binary_search(arr: List[int], l: int, r: int, target: int) -> int:
	"""
	Return the index of that target found in the input array or -1
	"""
	while l <= r:
		mid = (l + r) // 2

		if arr[mid] == target:
			return mid
		if arr[mid] < target:
			l = mid + 1
		else:
			r = mid
	return -1

if __name__ == '__main__':

	arr = [ 2, 3, 4, 10, 40 ] 
	target = 400
	result = binary_search(arr, 0, len(arr)-1, target) 
	
	if result != -1: 
		print(f"Element is present at index {result}") 
	else: 
		print("Element is not present in array")
