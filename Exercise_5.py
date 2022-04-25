# Python program for implementation of Quicksort

"""
    Iterative QuickSort also takes O(n log n) time
    where n is total numbers the input array
	In worst case secnario it takes O(n ^ 2) time
"""
# This function is same in both iterative and recursive
def partition(arr, low, high):
    # write your code here
	pindex = low
	pivot = arr[high]

	for i in range(low, high):
		if arr[i] <= pivot:
			arr[i], arr[pindex] = arr[pindex], arr[i]
			pindex += 1
	
	arr[high], arr[pindex] = arr[pindex], arr[high]
	return pindex

def quickSortIterative(arr, low, high):
  # write your code here
	size = high - low + 1
	stack = [0] * (size)

	top = -1

	top = top + 1
	stack[top] = low
	top = top + 1
	stack[top] = high

	while top >= 0:
		high = stack[top]
		top = top - 1
		low= stack[top]
		top = top - 1

		pivot = partition( arr, low, high )

		if pivot - 1 > low:
			top = top + 1
			stack[top] = low
			top = top + 1
			stack[top] = pivot - 1

		if pivot + 1 < high:
			top = top + 1
			stack[top] = pivot + 1
			top = top + 1
			stack[top] = high