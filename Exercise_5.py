# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
	i = l
	j = h - 1
	pivot = arr[h]

	while i <= j:
		if arr[i] > pivot:
			arr[i], arr[j] = arr[j], arr[i]
			j -= 1
		else:
			i += 1

	arr[i], arr[h] = arr[h], arr[i]
	return i


def quickSortIterative(arr, l, h):
  #write your code here
	stack = [(l, h)]
	while stack:
		l, h = stack.pop()
		p = partition(arr, l, h)
		if l < p-1:
			stack.append((l, p-1))
		if p+1 < h:
			stack.append((p+1, h))



  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %arr[i]), 
  
