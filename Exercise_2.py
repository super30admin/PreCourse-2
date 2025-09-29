# Time Complexity : O(n log n) average, O(n²) worst case
# Space Complexity : O(log n) due to recursion stack
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : No, but remember to handle base case properly

# Python program for implementation of Quicksort Sort 
def partition(arr,low,high):
    # Choose rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element (right position of pivot)
    i = low - 1
    
    # Iterate through all elements
    for j in range(low, high):
        # If current element is smaller than or equal to pivot, swap them
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pivotIndex = partition(arr, low, high)
        
        quickSort(arr, low, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
