# Python program for implementation of Quicksort Sort 
''' Time complexity : O(n log n)
Space Complexity: O(log n)


Did this code successfully run on Leetcode : 
Any problem you faced while coding this : No '''  
# give you explanation for the approach
def partition(arr,low,high):
    #divide the array
    i = (low-1)          
    pivot = arr[high]     # pivot 
    for j in range(low, high): 
        # If current element is smaller or equal to pivot 
        if arr[j] <= pivot: 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 


  

# Function to do Quick sort 
#sort
def quickSort(arr, low, high): 
    if len(arr) == 1: 
        return arr 
    if low < high: 
  
        # part_index is partitioning index
        part_index = partition(arr, low, high) 
        #sort to right and left of partition 
        quickSort(arr, low, part_index-1) 
        quickSort(arr, part_index+1, high) 

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
