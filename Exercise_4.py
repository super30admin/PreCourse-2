# Python program for implementation of MergeSort 
def mergeSort(arr):
	if len(arr) >= 2:

		mid = int(len(arr)/2)

		# split into left and right, sort left and right recursively
		left, right = arr[:mid], arr[mid:]
		mergeSort(left)
		mergeSort(right)

		# merging
		# smaller element comes first
		i, j, k = 0, 0, 0
		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1
		
		# comaprisons over
		# append all remaining
		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1

	
# Code to print the list 
def printList(arr): 
	print(arr)
	
# driver code to test the above code 
if __name__ == '__main__': 
	arr = [12, 11, 13, 5, 6, 7]  
	print ("Given array is", end="\n")  
	printList(arr) 
	mergeSort(arr) 
	print("Sorted array is: ", end="\n") 
	printList(arr) 
