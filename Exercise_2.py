# Python program for implementation of Quicksort Sort 
# Any problem you faced while coding this : No
# Time Complexity: O(n2) -> worst case
# Time Complexity: O(nlogn) -> best and avg case
# Space Complexity: O(logn) -> call stack

# give you explanation for the approach
# Quick sort is divide and conquer approach.
# Last element is choose as the pivot
# Store the elements leess than pivot in the left subarray, greater than the pivot in right subarray
# Call quicksort recursively on left subarray, call quicksort recursively on right subarray, until array size is 1. 

def partition(arr,low,high):
   
    #write your code here
    i = low
    j = high - 1
    p = arr[high]

    while i<j:
    	while i<high and arr[i]<p:
    		i+=1
    	while j>low and arr[j]>=p:
    		j-=1

    	if i<j:
    		arr[i], arr[j] = arr[j], arr[i]

    if arr[i]>p:
    	arr[i], arr[high] = arr[high], arr[i]

    return i  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low<high:
        partition_pos = partition(arr, low, high)
        quickSort(arr, low, partition_pos-1)
        quickSort(arr, partition_pos+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
