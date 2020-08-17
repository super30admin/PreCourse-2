
# Python program for implementation of MergeSort.
# STEPS:
# Recurively divide the array into two halves - left and right.
# compare elements of the left and right sorted subarrays.
# combine the two sorted subarrays to obtain a sorted array.
# Time complexity - O(nlogn) -> Divides arrays into two halves. -> Merge the two halves by traversing both the arrays together.
# Space complexity - O(n) -> auxillary space
def merge(low, mid, high, arr):
	'''
		Merge the left and right sorted arrays.
	'''
	l = mid - low + 1
	r = high - mid 

	left, right = [], []
	# compare the elements of left and right array, and add them to the merged list.
	for i in range(l): 
		left.append(arr[low+i])

	for i in range(r):
		right.append(arr[mid+1+i])

	i, j, k = 0, 0, low
	# merge the left and right array
	while i<l and j<r:
		if left[i] < right[j]:
			arr[k] = left[i] 
			k+=1
			i+=1
		else:
			arr[k] = right[j]
			k+=1
			j+=1

	# if the left or right subarrays have remaining elements, add them to the original array.
	while i<l:
		arr[k] = left[i]
		k+=1
		i+=1

	while j<r:
		arr[k] = right[j]
		k+=1
		j+=1

def mSort(low, high, arr):
	if low<high:
		mid = low + (high-low)//2
		mSort(low, mid, arr)
		mSort(mid+1, high, arr)
		merge(low, mid, high, arr)

def mergeSort(arr):
  # write your code here
  n = len(arr)
  return mSort(0, n-1, arr)

# Code to print the list 
def printList(arr): 
    #write your code here
    n = len(arr)
    for i in range(n):
    	print(arr[i], end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
