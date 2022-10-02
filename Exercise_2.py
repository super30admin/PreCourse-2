# Time Complexity : O (nlogn)
# Space Complexity :O(n)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :Yes, coding the partition part was tough.

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    # we will take the first element of the array as the pivot value
    pivot = arr[low]
    # Pointers for the left end and right ends of the array
    i = low
    j = high
    # loop through until i crosses j
    while i < j:
        #  Increment the value of i until we find an element greater than the pivot 
        while i < j and arr[i]<= pivot:
            i = i+1
        # Decrement the value of j while we find an element less than the pivot
        while arr[j]>pivot:
            j = j-1
        # Swap those two elements
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    # Swap the pivot with the element at the j pointer. 
    arr[low],arr[j] = arr[j], pivot
    # return the pivot index.
    return j
        
    
  
  
    
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        # Finding the pivot index using partition function
        pi = partition(arr, low, high)
        # sorting the left part of the pivot index
        quickSort(arr, low, pi-1)
        # sorting the right part of the pivot index
        quickSort(arr, pi+1, high)
    
    
  
# Driver code to test above 
arr = [890, 345, 56, 34, 23, 34, 34, 56, 89, 100, 1] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
