# Time Complexity : O(N log N) We divide the array into log N partitions for sorting
# Space Complexity : O(N) / size of intermediate arrays
# Python program for implementation of MergeSort

def mergeSort(arr):
	#Base case
	if len(arr) <= 1:
		return
	
	mid = len(arr)//2
	left = arr[:mid]
	right = arr[mid:]
	mergeSort(left)
	mergeSort(right)

	# sort on merge
	left_index, right_index, arr_index = 0,0,0

	while left_index < len(left) and right_index < len(right):
		if left[left_index] <= right[right_index]:
			arr[arr_index] = left[left_index]
			left_index += 1
		else:
			arr[arr_index] = right[right_index]
			right_index += 1
		arr_index += 1
	
	# Check in both left and right if there are still some elements to add 
	while left_index < len(left):
		arr[arr_index] = left[left_index]
		left_index += 1
		arr_index += 1

	while right_index < len(right):
		arr[arr_index] = right[right_index]
		right_index += 1
		arr_index += 1


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
