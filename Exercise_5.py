# Python program for implementation of Quicksort


#Time Complexity : O(n log n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this :
        
# Function to do Quick sort 
def quickSortIterative(arr,low,high): 
    
    #write your code here
   
    
	size = high - low + 1
	stack = [0] * size

	top = -1

	# push initial values of low and high to stack
	top = top + 1
	stack[top] = low
	top = top + 1
	stack[top] = high

    # pop the values until stack is empty
	while top >= 0:
		high = stack[top]
		top = top - 1
		low = stack[top]
		top = top - 1

		# set pivot element in correct position
		p = partition(arr,low,high)

		# push elements on left side of pivot if any to stack
		if p-1 > low:
			top = top + 1
			stack[top] = low
			top = top + 1
			stack[top] = p-1

		# push elements on right side of pivot if any to stack
		if p+1 < high:
			top = top + 1
			stack[top] = p+1
			top = top + 1
			stack[top] = high
          

# This function is same in both iterative and recursive
def partition(arr,low,high):
  
  
    #write your code here
    pivot_index = low
    pivot = arr[pivot_index]

    while low < high: # do this only until low and high cross
            # compare low with pivot and increment until low is greater than pivot
            while low < len(arr) and arr[low] <= pivot:
                  low += 1
            # compare high with pivot and decrement until high is less than pivot
            while arr[high] > pivot:  
                  high -= 1
            # swap low and high until they cross
            if low < high:
               swap(arr,low,high)

    # swap pivot and high once low and high crosses 
    swap(arr,pivot_index,high)       

    return high 


def swap(arr,pivot_index,high):

    if pivot_index!=high:
	    temp = arr[pivot_index]
	    arr[pivot_index] = arr[high]
	    arr[high] = temp  

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 



