# Python program for implementation of Quicksort Sort

"""
    QuickSort takes O(n log n) time
    where n is total numbers the input array
	In worst case secnario it takes O(n ^ 2) time
"""
# give you explanation for the approach
def partition(arr, low, high):
    # write your code here
	pindex = low
	pivot = arr[high]

	for i in range(low, high):
		if arr[i] <= pivot:
			arr[i], arr[pindex] = arr[pindex], arr[i]
			pindex += 1
	
	arr[high], arr[pindex] = arr[pindex], arr[high]
	return pindex

# Function to do Quick sort
def quickSort(arr, low, high):
    # write your code here
    if low < high:
        pindex = partition(arr, low, high)
        quickSort(arr, low, pindex - 1)
        quickSort(arr, pindex + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print(f"Sorted array is: {arr}")
