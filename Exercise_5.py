# Time Complexity :log(n^2)for worst case and O(n *log n) for average case
	# Space Complexity : O(1)
	
	# Python program for implementation of Iterative Quicksort
	
	# This function is same in both iterative and recursive
	def partition(arr, l, h):
	pivot, curr_element = arr[h], l
	
	# traverse the array and swap the elements that are lesser than the pivot element
	for i in range(l, h):
	if arr[i] <= pivot:
	arr[i], arr[curr_element] = arr[curr_element], arr[i]
	curr_element += 1
	
	# At last, swap the last element with the pivot so that we get havles of the array
	arr[curr_element], arr[h] = arr[h], arr[curr_element]
	return curr_element
	
	
	def quickSortIterative(arr, l, h):
	
	# find length of array and initialize a stack the same size as the arr
	x = h - l + 1
	stack = [0]*x
	
	# initialize the top
	top = -1
	
	# Add low and high elements onto the stack
	top += 1
	stack[top] = l
	top += 1
	stack[top] = h
	
	# starting a loop to go over all the elements of the stack
	while top >= 0:
	# pop the low and high elements then call the partition to start the sorting of elements
	h = stack[top]
	top -= 1
	l = stack[top]
	top -= 1
	
	pi = partition(arr, l, h)
	
	# If there are elements which are lesser than the low, then add those elements to the stack
	if pi - 1 > l:
	top += 1
	stack[top] = 1
	top += 1
	stack[top] = pi - 1
	
	# IF there are elements which are greater than the high, then add those elements to the stack
	if pi + 1 < h:
	top += 1
	stack[top] = pi + 1
	top += 1
	stack[top] = h
	
	
	
	# Driver code to test above
	arr = [10, 7, 8, 9, 1, 5]
	n = len(arr)
	quickSortIterative(arr, 0, n - 1)
	print("Sorted array is:")
	for i in range(n):
	print("%d" % arr[i]),
