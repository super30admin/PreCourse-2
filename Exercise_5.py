# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
	#write your code here
	# always selecting arr[low] as pivot
	# elements to left of pivot must be smaller and to the right must be larger
	
	# print((low, high))
	pivotindex = low
	pivot = arr[pivotindex]
	while low < high:
		# first larger element from the left
		while low < len(arr) and arr[low] <= pivot:
			low += 1
		# first smaller element from the right
		while arr[high] > pivot:
			high -= 1
		# swap so that smaller on left of pivot and larger on right of pivot
		if low < high:
			arr[low], arr[high] = arr[high], arr[low]
	# put pivot in correct place - swap with high
	arr[high], arr[pivotindex] = arr[pivotindex], arr[high]
	return high


def quickSortIterative(arr, low, high):
	#write your code here
	stack = [low, high]

	while stack:
		_high = stack.pop()
		_low = stack.pop()

		p = partition(arr, _low, _high)

		if p - 1 > _low:
			stack.append(_low)
			stack.append(p-1)

		if p + 1 < high:
			stack.append(p+1)
			stack.append(_high)

# Driver code
# arr = [10, 7, 8, 9, 1, 5] 
# n = len(arr) 
# quickSortIterative(arr,0,n-1) 
# print ("Sorted array is:") 
# for i in range(n): 
# 	print ("%d" %arr[i])