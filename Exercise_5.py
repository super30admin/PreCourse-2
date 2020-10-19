# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr,low,high):
	i=low-1 #smaller index taken as -1 
	pivot=arr[high] #Pivot as last element
	for j in range(low, high):
		if arr[j] <= pivot: #if cur element is less or eq to Pivot
			i=i+1 #increase smaller element
			arr[i], arr[j] = arr[j], arr[i] #swap smaller and higher element

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1

def quickSortIterative(arr, l, h):
	size = h - l + 1
	stack = [0] * (size)
	top=-1

	top = top + 1
	stack[top] = l 
	top = top + 1
	stack[top] = h

	while top >= 0: 
		h = stack[top] 
		top = top - 1
		l = stack[top] 
		top = top - 1

	part = partition( arr, l, h )

	if part-1 > l: 
		top = top + 1
		stack[top] = l 
		top = top + 1
		stack[top] = part - 1

	if part + 1 < h: 
		top = top + 1
		stack[top] = part + 1
		top = top + 1
		stack[top] = h 

arr = [4, 3, 5, 2, 1, 3, 2, 3] 
n = len(arr) 
quickSortIterative(arr, 0, n-1) 
print ("Sorted array is:") 
for i in range(n):
	print ("% d" % arr[i])



