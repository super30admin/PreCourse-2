# Python program for implementation of Quicksort Sort 

# Time Complexity:
# Best Case: O(n log n) - When the pivot divides the array into two equal halves.
# Worst Case: O(n^2) - When the pivot is the smallest or largest element repeatedly.
# Average Case: O(n log n) - On average, partitions are reasonably balanced.

# Space Complexity:
# Recursive Call Stack: O(log n) in the best case, O(n) in the worst case.
# In-Place Sorting: O(1) - No additional memory is used for the array.

#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
  
# give you explanation for the approach
def partition(arr,low,high):
    
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1
  
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        x = partition(arr, low, high)
        quickSort(arr, low, x - 1)
        quickSort(arr, x + 1, high)

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
