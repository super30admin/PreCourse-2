# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

def partition(arr,low,high):
  
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


def quickSortIterative(arr, l, h):
	stack = []
	stack.append(l)
	stack.append(h)
	while stack:
		h = stack.pop()
		l = stack.pop()
		# set the pivot
		p = partition(arr, l, h)
		# if the pivot is greater than 1, push the left and right subarrays to the stack
		if p - 1 > l:
		  stack.append(l)
		  stack.append(p - 1)
		if p + 1 < h:
		  stack.append(p + 1)
		  stack.append(h)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])