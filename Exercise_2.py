# Time Complexity : O(n^2) for worst case which is rare, O(nlogn) for average case
# Space Complexity : O(1) or constant auxiliary space complexity as no extra space is needed. O(n) overall space complexity for the array and the elements are swapped in place
# Did this code successfully run on Leetcode : Code ran successfully.
# Any problem you faced while coding this : No problems


# Your code here along with comments explaining your approach

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    pivot = arr[high] # Making pivot as the last element
    ptr = low # Make the pointer start at index low
    for i in range(low,high+1): # Loop in range of all indexes from low to high including high
        if arr[i] <= pivot:
            arr[i], arr[ptr] = arr[ptr], arr[i] # Swap values at current ptr and i
            if i!= high:
                ptr+=1 # Increment ptr for next iteration except if it is the last i.e rightmost index
    return ptr

# Function to do Quick sort 
def quickSort(arr,low,high):
    
    
    #write your code here
    if len(arr) == 1:
        return arr #Terminating condition to get out of recursion. When arr length is 1 it means all elements are sorted and each partition will have only 1 element
    elif low < high:
        p = partition(arr,low,high) # Call partition and find out the ptr value after partition
        quickSort(arr, low, p-1) # Recursively sort the left side of the partition
        quickSort(arr,p+1,high) # Recursively sort the right side of the partition
    
    return arr
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
