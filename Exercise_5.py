# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
"""
time complexity - Average and best case - O(NlogN)
                  Worst Case - O(n^2) - When already sorted.

Space Complexity - O(1) - since it is an in place sorting algorithm
                          with no extra space.
"""
def partition(arr, l, h):
	i = (l-1)
	pivot = arr[h]
	for j in range(l,h):
		if arr[j]<=pivot:
			i+=1
			arr[i],arr[j] = arr[j],arr[i]
	arr[i+1],arr[h] = arr[h],arr[i+1]
	return i+1
def quickSortIterative(arr, l, h):
	n = h-l+1
	stack = [0]*n
	top = -1
	top+=1
	stack[top] = l
	top+=1
	stack[top] = h

	while top>=0:
		h = stack[top]
		top-=1
		l = stack[top]
		top-=1
		position = partition(arr,l,h)
		if position-1 > l:
			top+=1
			stack[top] = l
			top+=1
			stack[top] = position-1

		if position+1 < h:
			top+=1
			stack[top] = position+1
			top+=1
			stack[top] = h

arr = [2,5,3,8,6,5,4,7]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
   print (arr[i],end=" ")