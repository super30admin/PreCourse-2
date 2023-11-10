# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

# Your code here along with comments explaining your approach

# Python program for implementation of MergeSort 
def mergeSort(arr):

  #write your code here

	if len(arr) > 1:
		mid = len(arr)//2 # Finding the mid of the array, Dividing the array elements into two halves and sorting them
		l = arr[:mid]
		r = arr[mid:]
		mergeSort(l)
		mergeSort(l)

		i = j = k = 0

		while i < len(l) and j < len(r): # copying data to two arrays l and r
			if l[i] < r[j]:
				arr[k] = l[i]
				i += 1
			else:
				arr[k] = r[j]
				j += 1
			k += 1

		while i < len(l): # verifying if any element was left
			arr[k] = l[i]
			i += 1
			k += 1

		while j < len(r):
			arr[k] = r[j]
			j += 1
			k += 1

# Code to print the list 
def printList(arr): 

    #write your code here
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
