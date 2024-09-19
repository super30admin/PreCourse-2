# Time Complexity : O(n^2)
# Space Complexity : o(log n)
# Did this code successfully run on Leetcode : No 
# Any problem you faced while coding this : No

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
    #write your code here
    pivot = arr[high] # We choose the last element as pivot
    i = low - 1 # Index of the smaller element

    for j in range (low, high):
        if arr[j] <= pivot: # If the current element is smaller than or equal to the pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Swap arr[i] and arr[j]

    arr[i+1], arr[high] = arr[high], arr[i+1] # Swap the pivot element with the element at i+1 (placing pivot in correct position)
    return i + 1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        pi =  partition(arr, low, high)  
        # Recursively sort elements before and after partition
        quickSort(arr, low, pi -1) # Sort elements before partition
        quickSort(arr, pi + 1, high) # Sort elements after partition
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5, 60] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
