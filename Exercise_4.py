# Python program for implementation of MergeSort 
# Time Complexity : O(n log n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : No. Could not find this problem (with 1 argument) on geeks or leetcode
# Any problem you faced while coding this : Yes. While implementing the merging logic.
def mergeSort(arr):
  
  #write your code here
  # dividing the array
	if len(arr) > 1:
		mid = len(arr) // 2
		lhs = arr[0: mid]
		rhs = arr[mid:]
		# dividing the lhs of the array until only one element is left in the array
		mergeSort(lhs)
		# dividing the rhs of the array until only one element is left in the array
		mergeSort(rhs)

    # merging the array
		# index for lhs and rhs
		i, j = 0,0
		# index for the merged array
		k = 0
		# merge_list =[]
		while i < len(lhs) and j < len(rhs):
			# if the left side element is smaller than the right hand side, add into the array
			if lhs[i] < rhs[j]:
				arr[k] = lhs[i]
				# merge_list.append(lhs[i])
				# increment the left element
				i += 1
			# else add right side element into the array
			else:
				arr[k] = rhs[j]
				# merge_list.append(rhs[j])
				# increment the right element
				j +=1 
			# increment the merged array to get the next element
			k += 1
		# merging the remaning left side element at the end of the list
		while i < len(lhs):
			arr[k] = lhs[i]
			# merge_list.append(lhs[i])
			i += 1
			k += 1
		# merging the remaning right side element at the end of the list
		while j < len(rhs):
			arr[k] = rhs[j]
			# merge_list.append(rhs[j])
			j +=1
			k +=1


# Code to print the list 
def printList(arr): 
    
    #write your code here
	print(arr)

# driver code to test the above code 
arr = [12, 11, 13, 5, 6, 7]  
print("Given array is", arr)  
printList(arr) 
mergeSort(arr) 
print("Sorted array is: ",arr) 
printList(arr) 
