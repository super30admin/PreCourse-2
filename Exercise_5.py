# Python program for implementation of Quicksort

"""
Intuition:  Select a pivot element. All the elements on the left of this pivot should be less than the pivot element.
All the elements on the right of this pivot element should be greater than the pivot element

Time Complexity : O(nlog n), Worst case: O(n^2) This depends on the pivot
Space Complexity : O(1)
"""

def partition(arr, low, high):
	#write your code here
	flag = 0
	pivot = low

	while flag != 1:

		while arr[pivot] <= arr[high] and (pivot != high):
			high -= 1

		if pivot == high:
			flag = 1
		elif arr[pivot] > arr[high]:
			arr[pivot], arr[high] = arr[high], arr[pivot]
			pivot = high

		if flag != 0:

			while arr[low] <= arr[pivot] and (pivot != low):
				low += 1

			if pivot == low:
				flag = 1
			elif arr[pivot] < arr[low]:
				arr[pivot], arr[low] = arr[low], arr[pivot]
				pivot = low
	return pivot

def quickSortIterative(arr, l, h):

	#Initialize Stack
	size = h - l + 1
	stack = [0] * (size)
 	top = 0
	stack[top] = l
	top += 1
	stack[top] = h
 
 	while top >= 0:
 
		h = stack[top]
		top = top - 1
		l = stack[top]
		top = top - 1
 
		p = partition( arr, l, h )
 
		# If there are elements on left side of pivot,
		# then push left side to stack
		if p-1 > l:
			top += 1
			stack[top] = l
			top += 1
			stack[top] = p - 1
 
		# If there are elements on right side of pivot,
		# then push right side to stack
		if p+1 < h:
			top += 1
			stack[top] = p + 1
			top += 1
			stack[top] = h

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %arr[i]), 
  
 
