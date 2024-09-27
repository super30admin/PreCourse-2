# -*- coding: utf-8 -*-
"""
Python implementation of Merge Sort

Time Complexity : O(nLogn)

"""

# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		m = int(len(arr)/2)
		# Dividing the given array into 2 halves
        
		L = arr[:m] #left array takes from beginnning to midpoint
		R = arr[m:] #right array takes midpoint to end of given array
		mergeSort(L) #Sort the left array
		mergeSort(R) #Sort the second array

		i = j = k = 0 #indexes
		while i < len(L) and j < len(R): #run through both arrays to sort
			if L[i] < R[j]: #Comparing first element of Left and right array
				arr[k] = L[i] #Storing the smallest sorted result in arr[k]
				i += 1 #increment the left array index
			else:
				arr[k] = R[j] #storing the smallest elem in Right array in arr[k]
				j += 1 #increment the right array index
			k += 1 #increment final array index

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# Code to print the list

def printList(arr):
	for i in range(len(arr)):
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