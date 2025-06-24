# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

import random
def partition(arr,low,high):
    #write your code here
    pivot_idx = random.randint(low, high, )
    
    pivot = arr[pivot_idx]
    
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]  # Move pivot to end

    i = low - 1 # smallest element index
    
    # traverse all elements in subarray
    for j in range(low, high):
        # if current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap elements at i and j
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # swap pivot to its correct position
    return i + 1  # return the index of pivot after partitioning
    
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pivot_idx = partition(arr, low, high)
        
        quickSort(arr, low, pivot_idx - 1)  
        quickSort(arr, pivot_idx+1, high)
    
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
