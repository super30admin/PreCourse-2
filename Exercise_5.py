#Time Complexity : O(n^2)
#Space Complexity : O(n)
#Did this code successfully run on Leetcode : No, I did not run it on leetcode
#Any problem you faced while coding this : I am not sure on the complexity particularly space complexity


#Your code here along with comments explaining your approach


# Python program for implementation of Quicksort 

# This function is same in both iterative and recursive 
def partition(arr,low,high):
    #This function chooses the pivot as last element
    # here we take the last element and modify the list such that all the elements less than
    # pivot occurs to left of it and all the elements larger than pivot occurs right of it
    # we return the position of the element
    # these two functions occur on same list
    i = (low-1)
    p = arr[high]
    
    for j in range(low, high):
        if arr[j] <= p:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return(i+1)


def quickSortIterative(arr,l,h): 
	# Create an stack 
	size = h - l + 1
	stack = [0] * (size) 

	# initialize top of stack 
	top = -1

	# push initial values of l and h to stack 
	top = top + 1
	stack[top] = l 
	top = top + 1
	stack[top] = h 

	# Keep popping from stack while is not empty 
	while top >= 0: 
		# Pop h and l 
		h = stack[top] 
		top = top - 1
		l = stack[top] 
		top = top - 1
		# Set pivot element at its correct position in 
		# sorted array 
		p = partition( arr, l, h ) 
		# If there are elements on left side of pivot, 
		# then push left side to stack 
		if p-1 > l: 
			top = top + 1
			stack[top] = l 
			top = top + 1
			stack[top] = p - 1
		# If there are elements on right side of pivot, 
		# then push right side to stack 
		if p+1 < h: 
			top = top + 1
			stack[top] = p + 1
			top = top + 1
			stack[top] = h 