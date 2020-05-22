# Time Complexity : O(n log n) where n is the number of nodes
# Space Complexity : O(h) = O(log n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Python program for implementation of MergeSort

'''
I have implemented a separated function for merge operation.Then used mergesort to recursively divide  array
into left and right, and then performing the merge operation

'''


def merge(A, L, R):
	i,j,k = 0,0,0

	while (i< len(L) and j < len(R)):

		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1

		elif R[j] < L[i]:
			A[k] = R[j]
			j += 1

		k += 1

	while (i < len(L)):
		A[k] = L[i]

		i += 1
		k += 1

	while (j < len(R)):
		A[k] = R[j]

		j += 1
		k += 1

	return arr



# Python program for implementation of MergeSort 
def mergeSort(arr):

	if len(arr) < 2:
		return
	mid = int((len(arr)-1)//2)
	L = arr[:mid+1]
	R = arr[mid+1:]

	mergeSort(L)
	mergeSort(R)

	return merge(arr, L, R)

  
  #write your code here

  
# Code to print the list 
def printList(arr):

	for i in arr:
		print(i)
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
