# Time Complexity: O(n log n)

# Space complexity: O(log n)

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high] # Choose the last element as pivot
    i = low - 1 # Index of smaller element
    for j in range(low, high): # Traverse through all elements and move smaller to the left of pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] # Swap if element <= pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # Place pivot after the last smaller element
    return i + 1 # Return pivot index

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pi = partition(arr, low, high) # Partition the array and get the pivot index
        quickSort(arr, low, pi - 1) # Recursively sort elements before and after partition
        quickSort(arr, pi + 1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
