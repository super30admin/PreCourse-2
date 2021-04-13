# Python program for implementation of Quicksort

"""
Intuition:  Select a pivot element. All the elements on the left of this pivot should be less than the pivot element.
All the elements on the right of this pivot element should be greater than the pivot element
Stack is used to add the indexes and from (L, pivot -1) and (pivot +1, R)

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

def quickSortIterative(arr, low, high):

	#Initialize Stack
	stack = [0] * 100
	top = 0
	stack[top] = low
	top += 1
	stack[top] = high

	while top >= 0:

		high = stack[top]
		top = top - 1
		low = stack[top]
		top = top - 1

		pivot = partition( arr, low, high )

		#Pushing (LOW, pivot-1) to stack
		if pivot-1 > low:
			top += 1
			stack[top] = low
			top += 1
			stack[top] = pivot - 1

		#Pushing (pivot + 1, High) to stack
		if pivot+1 < high:
			top += 1
			stack[top] = pivot + 1
			top += 1
			stack[top] = high

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %arr[i]), 
  
 
