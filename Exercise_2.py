""" The quicksort algorithm picks a random pivot and sets the pivot in the right place within the array. 
All elements smaller than the pivot are placed before it and all elements larger are placed after it.
To avoid changing indexes of multiple elements for each comparison with the pivot, we place the pivot at the front of the array.
Then we create a cloud at the front that contains all the elements smaller than it. Now, we swap the front of the element which is the pivot
to its right position within the array. This is continued for all subsections of the array before and after the pivot.
The partition function takes care of this and returns the final position of the pivot within the array so that the subarrays before and after the pivot can continue sorting its elements.
The time complexity for this is O(nlogn) and the space complexity is O(n)."""
# Python program for implementation of Quicksort Sort 
# give you explanation for the approach
import random
def partition(arr,low,high):
	pivot = random.randint(low,high)
	arr[pivot], arr[low] = arr[low], arr[pivot]
	less = low
	for i in range(low+1, high+1):
		if(arr[low]>=arr[i]):
			less += 1
			arr[less],arr[i] = arr[i],arr[less]
	arr[low], arr[less] = arr[less],arr[low]
	return less

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if(low<high):
    	pivot = partition(arr,low,high)
    	quickSort(arr,low,pivot-1)
    	quickSort(arr,pivot+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5, 4, 20, 8] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
