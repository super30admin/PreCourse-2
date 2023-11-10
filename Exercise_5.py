# Time Complexity : O(N log N) We divide the array into log N partitions for sorting, worst case for sorted array O(N^2)
# Space Complexity : O(N) / size of stack used
# Python program for implementation of Quicksort (iterative)

# This function is same in both iterative and recursive
def partition(arr, l, h):
  # Chosing pivot as rightmost element
    pivot = arr[h]
    
    left, right = l, h -1
    while left <= right:
        while arr[left] <pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        # Found left an right indices that need to be swaped
        if left < right: # swap only if left is still smaller than right
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
        else:
            # Swap pivot with the left pointer as its the correct index     
            temp = arr[left]
            arr[left] = arr[h]
            arr[h] = temp
 
    return left


def quickSortIterative(arr, l, h):
	#Base case
	if len(arr) <= 1:
		return
	stack = [0]*len(arr)
	
	# top of the stack
	top = -1

	top += 1
	stack[top] = l
	top += 1
	stack[top] = h

	while top >= 0:
		# Pop h and l
		h = stack[top]
		top -= 1
		l = stack[top]
		top -= 1

		# Get partition index from pivot placement
		partition_index = partition( arr, l, h )

		# Push to stack left indices
		if partition_index-1 > l:
			top += 1
			stack[top] = l
			top += 1
			stack[top] = partition_index - 1

		# Push to stack left indices
		if partition_index + 1 < h:
			top += 1
			stack[top] = partition_index + 1
			top += 1
			stack[top] = h

arr = [6,5,4,3]
quickSortIterative(arr,0,len(arr)-1) 
print ("Sorted array is:") 
print(arr)