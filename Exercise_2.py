# Time Complexity : log(n^2) for worst case and O(n * log n) for average case
	# Space Complexity : O(1)
	
	# Python program for implementation of Quicksort Sort
	
	# partition the array after selecting the pivot as the last element of the array
	def partition(arr, low, high):
	pivot, curr_element = arr[high], low
	
	# traverse the array and swap the elements that are lesser than the pivot element
	for i in range(low, high):
	if arr[i] <= pivot:
	arr[i], arr[curr_element] = arr[curr_element], arr[i]
	curr_element += 1
	
	# At last, swap the last element with the pivot so that we get havles of the array
	arr[curr_element], arr[high] = arr[high], arr[curr_element]
	return curr_element
	
	
	# write your code here
	
	
	# Function to do Quick sort
	def quickSort(arr, low, high):
	if len(arr) == 1:
	return arr
	else:
	if low < high:
	# call the partition function to get the middle element
	pi = partition(arr,low, high)
	
	# Then recursively call the quick sort function on both the half arrays
	quickSort(arr,low,pi-1)
	quickSort(arr,pi+1,high)
	return arr
	
	# write your code here
	
	# Driver code to test above
	arr = [10, 7, 8, 9, 1, 5]
	n = len(arr)
	quickSort(arr, 0, n - 1)
	print("Sorted array is:")
	for i in range(n):
	print("%d" % arr[i]),
