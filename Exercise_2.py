# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
	#write your code here
	# always selecting arr[low] as pivot
	# elements to left of pivot must be smaller and to the right must be larger
	
	# print((low, high))
	pivotindex = low
	pivot = arr[pivotindex]
	while low < high:
		# first larger element from the left
		while low < len(arr) and arr[low] <= pivot:
			low += 1
		# first smaller element from the right
		while arr[high] > pivot:
			high -= 1
		# swap so that smaller on left of pivot and larger on right of pivot
		if low < high:
			arr[low], arr[high] = arr[high], arr[low]
	# put pivot in correct place - swap with high
	arr[high], arr[pivotindex] = arr[pivotindex], arr[high]
	return high

# Function to do Quick sort 
def quickSort(arr,low,high): 
	#write your code here
	# call recursively partition on left anf right subarrays
	if low < high:
		mid = partition(arr, low, high)
		quickSort(arr, low, mid-1)
		quickSort(arr, mid+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %arr[i])
