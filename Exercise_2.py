# Python program for implementation of Quicksort Sort 
# Worst case time complexity: O(n^2)
# Average case time complexity: O(nlogn)
  
# The last element in the list has been used as a pivot
# Elements smaller than the pivot are put in front using a pointer
def partition(arr,low,high):
    pivot, ptrIdx = arr[high], low
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i], arr[ptrIdx] = arr[ptrIdx], arr[i]
            ptrIdx += 1
    # Swapping pointer with the pivot
    arr[ptrIdx], arr[high] = arr[high], arr[ptrIdx]
    return ptrIdx

# Function to do Quick sort 
def quickSort(arr,low,high):
    # Base case
    if len(arr) == 1:
        return arr
    if low < high:
        pIdx = partition(arr, low, high)
        quickSort(arr, low, pIdx - 1) # Sorting the left partition
        quickSort(arr, pIdx + 1, high) # Sorting the right partition
    return arr

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
