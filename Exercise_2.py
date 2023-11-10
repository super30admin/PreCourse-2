# Python program for implementation of Quicksort Sort
#Time Complexity : O(NlogN)
#Space Complexity : O(N)
#Any problem you faced while coding this : No


# This implementation utilizes pivot as the last element in the arr list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" arr relative to the pivot


def partition(arr,low,high):
	# Last element will be the pivot and the first element the pointer
	pivot, ptr = arr[high], low
	for i in range(low, high):
		if arr[i] <= pivot:
			# Swapping values smaller than the pivot to the front
			arr[i], arr[ptr] = arr[ptr], arr[i]
			ptr += 1
	# Finally swappping the last element with the pointer indexed arr
	arr[ptr], arr[high] = arr[high], arr[ptr]
	return ptr

# With quickSort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.


def quickSort(arr,low,high):
	if len(arr) == 1: # Terminating Condition for recursion
		return arr
	if low < high:
		pi = partition(arr,low,high)
		quickSort(arr,low, pi-1) # Recursively sorting the left values
		quickSort(arr,pi+1, high) # Recursively sorting the right values
	return arr


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
