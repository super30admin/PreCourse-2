# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# Time Complexity : O(n^2)
# Space Complexity :O(N)
# Did this code successfully run on Leetcode : Online GDB
# Any problem you faced while coding this : None

def partition(arr, low, high):
    # Choose the pivot as the last element
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)  # Place pivot in correct position
    return i + 1

def swap(arr, i, j):
    # Swap elements at indices i and j
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    # Recursively sort subarrays
    if low < high:
        part = partition(arr, low, high)
        quickSort(arr, low, part - 1)  # Sort left subarray
        quickSort(arr, part + 1, high) # Sort right subarray
        
# Driver code to test the quicksort implementation:
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)

# Sort the entire array using quicksort.
quickSort(arr, 0, n - 1)

# Print the sorted array.
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])